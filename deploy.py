#!/usr/bin/env python3
"""
AWS Deployment Script - Deploy static website to S3 and CloudFront
"""
import os
import json
import time
from pathlib import Path

# Load environment variables from .env file
env_file = Path(".env")
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()

try:
    import boto3
    from botocore.exceptions import ClientError
except ImportError:
    print("Installing required package: boto3...")
    import subprocess

    subprocess.check_call(["pip", "install", "boto3"])
    import boto3
    from botocore.exceptions import ClientError

# Configuration
BUCKET_NAME = "demo-sierra-vista"
REGION = os.environ.get("AWS_REGION", "us-east-1")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

print("=" * 60)
print("AWS Static Website Deployment")
print("=" * 60)
print(f"Bucket name: {BUCKET_NAME}")
print(f"Region: {REGION}")
print()

# Initialize AWS clients
s3 = boto3.client(
    "s3",
    region_name=REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

cloudfront = boto3.client(
    "cloudfront",
    region_name=REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

# Step 1: Create S3 bucket
print("Step 1: Creating S3 bucket...")
try:
    if REGION == "us-east-1":
        s3.create_bucket(Bucket=BUCKET_NAME)
    else:
        s3.create_bucket(
            Bucket=BUCKET_NAME, CreateBucketConfiguration={"LocationConstraint": REGION}
        )
    print(f"✓ Bucket '{BUCKET_NAME}' created successfully")
except ClientError as e:
    if e.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
        print(f"✓ Bucket '{BUCKET_NAME}' already exists")
    else:
        print(f"✗ Error creating bucket: {e}")
        raise

# Step 2: Configure bucket for public access
print("\nStep 2: Configuring public access...")
try:
    s3.delete_public_access_block(Bucket=BUCKET_NAME)
    print("✓ Public access block removed")
except ClientError as e:
    print(f"⚠ Warning: {e}")

# Step 3: Set bucket policy
print("\nStep 3: Setting bucket policy...")
bucket_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*",
        }
    ],
}

try:
    s3.put_bucket_policy(Bucket=BUCKET_NAME, Policy=json.dumps(bucket_policy))
    print("✓ Bucket policy set successfully")
except ClientError as e:
    print(f"✗ Error setting bucket policy: {e}")

# Step 4: Enable static website hosting
print("\nStep 4: Enabling static website hosting...")
try:
    s3.put_bucket_website(
        Bucket=BUCKET_NAME,
        WebsiteConfiguration={
            "IndexDocument": {"Suffix": "index.html"},
            "ErrorDocument": {"Key": "index.html"},
        },
    )
    print("✓ Static website hosting enabled")
except ClientError as e:
    print(f"✗ Error enabling website hosting: {e}")

# Step 5: Upload files
print("\nStep 5: Uploading files...")
files_to_upload = [
    ("index.html", "text/html"),
    ("README.md", "text/markdown"),
]

for filename, content_type in files_to_upload:
    if Path(filename).exists():
        try:
            s3.upload_file(
                filename, BUCKET_NAME, filename, ExtraArgs={"ContentType": content_type}
            )
            print(f"✓ Uploaded {filename}")
        except ClientError as e:
            print(f"✗ Error uploading {filename}: {e}")
    else:
        print(f"⚠ File {filename} not found, skipping")

# Step 6: Create CloudFront distribution
print("\nStep 6: Creating CloudFront distribution...")
website_endpoint = f"{BUCKET_NAME}.s3-website-{REGION}.amazonaws.com"

try:
    # Check if distribution already exists
    existing_distributions = cloudfront.list_distributions()
    distribution_id = None
    distribution_domain = None

    if (
        "DistributionList" in existing_distributions
        and "Items" in existing_distributions["DistributionList"]
    ):
        for dist in existing_distributions["DistributionList"]["Items"]:
            if "Origins" in dist and "Items" in dist["Origins"]:
                for origin in dist["Origins"]["Items"]:
                    if BUCKET_NAME in origin.get("DomainName", ""):
                        distribution_id = dist["Id"]
                        distribution_domain = dist["DomainName"]
                        print(f"✓ Found existing CloudFront distribution")
                        print(f"  Distribution ID: {distribution_id}")
                        print(f"  Domain: {distribution_domain}")
                        break
            if distribution_id:
                break

    if not distribution_id:
        print("Creating new CloudFront distribution...")
        caller_reference = f"{BUCKET_NAME}-{int(time.time())}"

        distribution_config = {
            "CallerReference": caller_reference,
            "Comment": f"Distribution for {BUCKET_NAME}",
            "Enabled": True,
            "Origins": {
                "Quantity": 1,
                "Items": [
                    {
                        "Id": f"{BUCKET_NAME}-origin",
                        "DomainName": website_endpoint,
                        "CustomOriginConfig": {
                            "HTTPPort": 80,
                            "HTTPSPort": 443,
                            "OriginProtocolPolicy": "http-only",
                        },
                    }
                ],
            },
            "DefaultRootObject": "index.html",
            "DefaultCacheBehavior": {
                "TargetOriginId": f"{BUCKET_NAME}-origin",
                "ViewerProtocolPolicy": "redirect-to-https",
                "AllowedMethods": {
                    "Quantity": 2,
                    "Items": ["GET", "HEAD"],
                    "CachedMethods": {"Quantity": 2, "Items": ["GET", "HEAD"]},
                },
                "ForwardedValues": {
                    "QueryString": False,
                    "Cookies": {"Forward": "none"},
                },
                "MinTTL": 0,
                "Compress": True,
            },
        }

        response = cloudfront.create_distribution(
            DistributionConfig=distribution_config
        )
        distribution_id = response["Distribution"]["Id"]
        distribution_domain = response["Distribution"]["DomainName"]
        print(f"✓ CloudFront distribution created")
        print(f"  Distribution ID: {distribution_id}")
        print(f"  Domain: {distribution_domain}")
        print("  Note: It may take 15-20 minutes for the distribution to deploy")

except ClientError as e:
    print(f"✗ Error with CloudFront: {e}")
    print("⚠ Continuing without CloudFront distribution")
    distribution_domain = None

# Step 7: Verify deployment
print("\nStep 7: Testing website...")
s3_website_url = f"http://{website_endpoint}"

import urllib.request

try:
    response = urllib.request.urlopen(s3_website_url, timeout=10)
    if response.status == 200:
        print(f"✓ Website is accessible")
        print(f"  Status: {response.status}")
        content = response.read()
        print(f"  Content length: {len(content)} bytes")
except Exception as e:
    print(f"⚠ Could not verify website (may need time to propagate): {e}")

# Summary
print("\n" + "=" * 60)
print("Deployment Complete!")
print("=" * 60)
print(f"S3 Website URL: {s3_website_url}")
print(f"S3 Bucket: {BUCKET_NAME}")
if distribution_domain:
    print(f"CloudFront URL: https://{distribution_domain}")
    print("(CloudFront may take 15-20 minutes to fully deploy)")
print("=" * 60)
