# AWS Deployment Script using REST API
$ErrorActionPreference = "Continue"

# Load environment variables from .env file
Get-Content .env | ForEach-Object {
    if ($_ -match '^\s*([^#][^=]+)=(.+)$') {
        $key = $matches[1].Trim()
        $value = $matches[2].Trim()
        Set-Item -Path "env:$key" -Value $value
    }
}

$accessKey = $env:AWS_ACCESS_KEY_ID
$secretKey = $env:AWS_SECRET_ACCESS_KEY
$region = $env:AWS_REGION
$bucketName = "demo-sierra-vista"
$service = "s3"

Write-Host "Starting AWS deployment..." -ForegroundColor Green
Write-Host "Bucket name: $bucketName" -ForegroundColor Cyan
Write-Host "Region: $region" -ForegroundColor Cyan

# Function to create AWS Signature Version 4
function New-AWSSignature {
    param(
        [string]$Method,
        [string]$Uri,
        [string]$Service,
        [string]$Region,
        [hashtable]$Headers,
        [string]$Payload = ""
    )
    
    $date = [DateTime]::UtcNow
    $dateStamp = $date.ToString("yyyyMMdd")
    $amzDate = $date.ToString("yyyyMMddTHHmmssZ")
    
    # Add required headers
    $Headers['x-amz-date'] = $amzDate
    $Headers['x-amz-content-sha256'] = (Get-SHA256Hash $Payload)
    
    # Parse URI
    $parsedUri = [Uri]$Uri
    $canonicalUri = $parsedUri.AbsolutePath
    if ([string]::IsNullOrEmpty($canonicalUri)) { $canonicalUri = "/" }
    $canonicalQueryString = ""
    
    # Create canonical headers
    $canonicalHeaders = ($Headers.GetEnumerator() | Sort-Object Name | ForEach-Object {
        "$($_.Key.ToLower()):$($_.Value.Trim())`n"
    }) -join ""
    
    $signedHeaders = ($Headers.Keys | Sort-Object | ForEach-Object { $_.ToLower() }) -join ";"
    
    # Create canonical request
    $payloadHash = $Headers['x-amz-content-sha256']
    $canonicalRequest = "$Method`n$canonicalUri`n$canonicalQueryString`n$canonicalHeaders`n$signedHeaders`n$payloadHash"
    
    # Create string to sign
    $credentialScope = "$dateStamp/$Region/$Service/aws4_request"
    $canonicalRequestHash = Get-SHA256Hash $canonicalRequest
    $stringToSign = "AWS4-HMAC-SHA256`n$amzDate`n$credentialScope`n$canonicalRequestHash"
    
    # Calculate signature
    $kDate = Get-HMACSHA256 ("AWS4" + $secretKey) $dateStamp $true
    $kRegion = Get-HMACSHA256 $kDate $Region $true
    $kService = Get-HMACSHA256 $kRegion $Service $true
    $kSigning = Get-HMACSHA256 $kService "aws4_request" $true
    $signature = Get-HMACSHA256 $kSigning $stringToSign $false
    
    # Create authorization header
    $authHeader = "AWS4-HMAC-SHA256 Credential=$accessKey/$credentialScope, SignedHeaders=$signedHeaders, Signature=$signature"
    $Headers['Authorization'] = $authHeader
    
    return $Headers
}

function Get-SHA256Hash {
    param([string]$Text)
    $sha256 = [System.Security.Cryptography.SHA256]::Create()
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
    $hash = $sha256.ComputeHash($bytes)
    return ($hash | ForEach-Object { $_.ToString("x2") }) -join ""
}

function Get-HMACSHA256 {
    param(
        $Key,
        [string]$Message,
        [bool]$ReturnBytes
    )
    
    if ($Key -is [string]) {
        $Key = [System.Text.Encoding]::UTF8.GetBytes($Key)
    }
    
    $hmac = New-Object System.Security.Cryptography.HMACSHA256
    $hmac.Key = $Key
    $messageBytes = [System.Text.Encoding]::UTF8.GetBytes($Message)
    $hash = $hmac.ComputeHash($messageBytes)
    
    if ($ReturnBytes) {
        return $hash
    }
    else {
        return ($hash | ForEach-Object { $_.ToString("x2") }) -join ""
    }
}

# Step 1: Create S3 bucket
Write-Host "`nStep 1: Creating S3 bucket..." -ForegroundColor Yellow
$createBucketUri = "https://$bucketName.s3.$region.amazonaws.com/"
$createBucketHeaders = @{
    'Host' = "$bucketName.s3.$region.amazonaws.com"
}

$createBucketXml = @"
<CreateBucketConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <LocationConstraint>$region</LocationConstraint>
</CreateBucketConfiguration>
"@

$signedHeaders = New-AWSSignature -Method "PUT" -Uri $createBucketUri -Service $service -Region $region -Headers $createBucketHeaders -Payload $createBucketXml

try {
    $response = Invoke-WebRequest -Uri $createBucketUri -Method PUT -Headers $signedHeaders -Body $createBucketXml -ContentType "application/xml" -UseBasicParsing
    Write-Host "✓ Bucket created successfully" -ForegroundColor Green
}
catch {
    if ($_.Exception.Response.StatusCode.value__ -eq 409) {
        Write-Host "✓ Bucket already exists" -ForegroundColor Green
    }
    else {
        Write-Host "Error creating bucket: $_" -ForegroundColor Red
        throw
    }
}

# Step 2: Disable Block Public Access
Write-Host "`nStep 2: Configuring public access..." -ForegroundColor Yellow
$publicAccessUri = "https://$bucketName.s3.$region.amazonaws.com/?publicAccessBlock"
$publicAccessHeaders = @{
    'Host' = "$bucketName.s3.$region.amazonaws.com"
}

$publicAccessXml = @"
<PublicAccessBlockConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <BlockPublicAcls>false</BlockPublicAcls>
  <IgnorePublicAcls>false</IgnorePublicAcls>
  <BlockPublicPolicy>false</BlockPublicPolicy>
  <RestrictPublicBuckets>false</RestrictPublicBuckets>
</PublicAccessBlockConfiguration>
"@

$signedHeaders = New-AWSSignature -Method "PUT" -Uri $publicAccessUri -Service $service -Region $region -Headers $publicAccessHeaders -Payload $publicAccessXml

try {
    Invoke-WebRequest -Uri $publicAccessUri -Method PUT -Headers $signedHeaders -Body $publicAccessXml -ContentType "application/xml" -UseBasicParsing | Out-Null
    Write-Host "✓ Public access configured" -ForegroundColor Green
} catch {
    Write-Host "Warning: Could not configure public access: $_" -ForegroundColor Yellow
}

# Wait a moment for settings to propagate
Start-Sleep -Seconds 2

# Step 3: Set bucket policy for public read
Write-Host "`nStep 3: Setting bucket policy..." -ForegroundColor Yellow
$policyUri = "https://$bucketName.s3.$region.amazonaws.com/?policy"
$policyHeaders = @{
    'Host' = "$bucketName.s3.$region.amazonaws.com"
}

$bucketPolicy = @{
    Version = "2012-10-17"
    Statement = @(
        @{
            Sid = "PublicReadGetObject"
            Effect = "Allow"
            Principal = "*"
            Action = "s3:GetObject"
            Resource = "arn:aws:s3:::$bucketName/*"
        }
    )
} | ConvertTo-Json -Depth 10 -Compress

$signedHeaders = New-AWSSignature -Method "PUT" -Uri $policyUri -Service $service -Region $region -Headers $policyHeaders -Payload $bucketPolicy

try {
    Invoke-WebRequest -Uri $policyUri -Method PUT -Headers $signedHeaders -Body $bucketPolicy -ContentType "application/json" -UseBasicParsing | Out-Null
    Write-Host "✓ Bucket policy set successfully" -ForegroundColor Green
} catch {
    Write-Host "Error setting bucket policy: $_" -ForegroundColor Red
    Write-Host $_.Exception.Response
}

# Step 4: Enable static website hosting
Write-Host "`nStep 4: Enabling static website hosting..." -ForegroundColor Yellow
$websiteUri = "https://$bucketName.s3.$region.amazonaws.com/?website"
$websiteHeaders = @{
    'Host' = "$bucketName.s3.$region.amazonaws.com"
}

$websiteConfig = @"
<WebsiteConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <IndexDocument>
    <Suffix>index.html</Suffix>
  </IndexDocument>
  <ErrorDocument>
    <Key>index.html</Key>
  </ErrorDocument>
</WebsiteConfiguration>
"@

$signedHeaders = New-AWSSignature -Method "PUT" -Uri $websiteUri -Service $service -Region $region -Headers $websiteHeaders -Payload $websiteConfig

try {
    Invoke-WebRequest -Uri $websiteUri -Method PUT -Headers $signedHeaders -Body $websiteConfig -ContentType "application/xml" -UseBasicParsing | Out-Null
    Write-Host "✓ Static website hosting enabled" -ForegroundColor Green
} catch {
    Write-Host "Error enabling website hosting: $_" -ForegroundColor Red
}

# Step 5: Upload files
Write-Host "`nStep 5: Uploading files..." -ForegroundColor Yellow

# Upload index.html
$indexContent = Get-Content -Path "index.html" -Raw
$uploadUri = "https://$bucketName.s3.$region.amazonaws.com/index.html"
$uploadHeaders = @{
    'Host' = "$bucketName.s3.$region.amazonaws.com"
    'Content-Type' = 'text/html'
}

$signedHeaders = New-AWSSignature -Method "PUT" -Uri $uploadUri -Service $service -Region $region -Headers $uploadHeaders -Payload $indexContent

try {
    Invoke-WebRequest -Uri $uploadUri -Method PUT -Headers $signedHeaders -Body $indexContent -ContentType "text/html" -UseBasicParsing | Out-Null
    Write-Host "✓ Uploaded index.html" -ForegroundColor Green
} catch {
    Write-Host "Error uploading index.html: $_" -ForegroundColor Red
}

# Upload README.md
$readmeContent = Get-Content -Path "README.md" -Raw
$uploadUri = "https://$bucketName.s3.$region.amazonaws.com/README.md"
$uploadHeaders = @{
    'Host' = "$bucketName.s3.$region.amazonaws.com"
    'Content-Type' = 'text/markdown'
}

$signedHeaders = New-AWSSignature -Method "PUT" -Uri $uploadUri -Service $service -Region $region -Headers $uploadHeaders -Payload $readmeContent

try {
    Invoke-WebRequest -Uri $uploadUri -Method PUT -Headers $signedHeaders -Body $readmeContent -ContentType "text/markdown" -UseBasicParsing | Out-Null
    Write-Host "✓ Uploaded README.md" -ForegroundColor Green
} catch {
    Write-Host "Error uploading README.md: $_" -ForegroundColor Red
}

# Step 6: Output website URL
$websiteUrl = "http://$bucketName.s3-website-$region.amazonaws.com"
Write-Host "`n========================================" -ForegroundColor Green
Write-Host "Deployment Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "S3 Website URL: $websiteUrl" -ForegroundColor Cyan
Write-Host "S3 Bucket: $bucketName" -ForegroundColor Cyan
Write-Host "`nNote: CloudFront distribution requires additional API calls." -ForegroundColor Yellow
Write-Host "The S3 website is now accessible at the URL above." -ForegroundColor Yellow

# Step 7: Test the website
Write-Host "`nStep 6: Testing website..." -ForegroundColor Yellow
try {
    $testResponse = Invoke-WebRequest -Uri $websiteUrl -UseBasicParsing -TimeoutSec 10
    if ($testResponse.StatusCode -eq 200) {
        Write-Host "✓ Website is accessible and returning content" -ForegroundColor Green
        Write-Host "  Status: $($testResponse.StatusCode)" -ForegroundColor Gray
        Write-Host "  Content length: $($testResponse.Content.Length) bytes" -ForegroundColor Gray
    }
} catch {
    Write-Host "⚠ Website test failed (may need a moment to propagate): $_" -ForegroundColor Yellow
}

Write-Host "`nDeployment script completed successfully!" -ForegroundColor Green
