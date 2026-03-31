# GitHub Actions Setup Guide

## Overview

This project uses GitHub Actions for automated deployment to AWS S3 and CloudFront distribution invalidation.

## Prerequisites

- GitHub repository with the code
- AWS account with S3 bucket and CloudFront distribution already set up
- AWS IAM credentials with appropriate permissions

## Setting Up GitHub Secrets

✅ **GitHub secrets have been automatically configured!**

The AWS credentials from your `.env` file have been securely added to your GitHub repository using the `setup-github-secrets.py` script.

**Configured secrets:**

- `AWS_ACCESS_KEY_ID` ✅
- `AWS_SECRET_ACCESS_KEY` ✅

### Manual Setup (if needed)

If you need to update or reconfigure secrets manually:

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** or edit existing secrets
4. Add/update the following secrets:

   **Secret 1:**
   - Name: `AWS_ACCESS_KEY_ID`
   - Value: Your AWS access key ID

   **Secret 2:**
   - Name: `AWS_SECRET_ACCESS_KEY`
   - Value: Your AWS secret access key

## Required AWS IAM Permissions

Your AWS credentials should have the following permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::demo-sierra-vista",
        "arn:aws:s3:::demo-sierra-vista/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": ["cloudfront:CreateInvalidation"],
      "Resource": "*"
    }
  ]
}
```

## Workflow Trigger

The deployment workflow automatically triggers when:

- Code is pushed to the `main` branch
- Manually triggered from the Actions tab

## Monitoring Deployments

1. Go to the **Actions** tab in your GitHub repository
2. Click on the latest workflow run to see deployment progress
3. Each step shows real-time logs

## Testing

After the workflow completes:

- **S3 URL**: http://demo-sierra-vista.s3-website-us-east-1.amazonaws.com
- **CloudFront URL**: https://d2gpxm7g9jp1jd.cloudfront.net

CloudFront cache invalidation typically takes 1-2 minutes to propagate.

## Troubleshooting

### Workflow fails with authentication error

- Verify GitHub secrets are correctly set
- Check AWS credentials have not expired
- Ensure IAM permissions are correct

### Deployment succeeds but site doesn't update

- Check the CloudFront invalidation step completed successfully
- Wait 1-2 minutes for cache invalidation to propagate
- Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)

### Build fails

- Check `package.json` dependencies are correct
- Verify Node.js version compatibility
- Review build logs in Actions tab
