#!/usr/bin/env python3
"""Check CloudFront distribution status"""
import os
from pathlib import Path

# Load environment variables
env_file = Path(".env")
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()

import boto3

cloudfront = boto3.client(
    "cloudfront",
    region_name=os.environ.get("AWS_REGION", "us-east-1"),
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
)

distributions = cloudfront.list_distributions()
if "DistributionList" in distributions and "Items" in distributions["DistributionList"]:
    for dist in distributions["DistributionList"]["Items"]:
        if "demo-sierra-vista" in str(dist.get("Origins", {}).get("Items", [])):
            print(f"Distribution ID: {dist['Id']}")
            print(f"Domain: {dist['DomainName']}")
            print(f"Status: {dist['Status']}")
            print(f"Enabled: {dist['Enabled']}")
            print(f"URL: https://{dist['DomainName']}")
