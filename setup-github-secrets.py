#!/usr/bin/env python3
"""
Configure GitHub Repository Secrets
Automatically adds AWS credentials as secrets to the GitHub repository
"""
import os
import json
import base64
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

# Check for required modules
try:
    import requests
    from nacl import encoding, public
except ImportError:
    print("Installing required packages...")
    import subprocess

    subprocess.check_call(["pip", "install", "requests", "pynacl"])
    import requests
    from nacl import encoding, public

# Configuration
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO_OWNER = "jerimiahbaldwin"
REPO_NAME = "demo-sierra-vista"
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

if not GITHUB_TOKEN:
    print("❌ Error: GITHUB_TOKEN not found in environment")
    exit(1)

if not AWS_ACCESS_KEY_ID or not AWS_SECRET_ACCESS_KEY:
    print("❌ Error: AWS credentials not found in environment")
    exit(1)

print("=" * 60)
print("GitHub Repository Secrets Configuration")
print("=" * 60)
print(f"Repository: {REPO_OWNER}/{REPO_NAME}")
print()

# GitHub API headers
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28",
}


def get_public_key():
    """Get the repository's public key for encrypting secrets"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/secrets/public-key"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ Error getting public key: {response.status_code}")
        print(response.text)
        exit(1)


def encrypt_secret(public_key: str, secret_value: str) -> str:
    """Encrypt a secret using the repository's public key"""
    public_key_obj = public.PublicKey(
        public_key.encode("utf-8"), encoding.Base64Encoder()
    )
    sealed_box = public.SealedBox(public_key_obj)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return base64.b64encode(encrypted).decode("utf-8")


def create_or_update_secret(
    secret_name: str, secret_value: str, key_id: str, public_key: str
):
    """Create or update a repository secret"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/secrets/{secret_name}"

    encrypted_value = encrypt_secret(public_key, secret_value)

    data = {"encrypted_value": encrypted_value, "key_id": key_id}

    response = requests.put(url, headers=headers, json=data)

    if response.status_code in [201, 204]:
        status = "created" if response.status_code == 201 else "updated"
        print(f"✅ Secret '{secret_name}' {status} successfully")
        return True
    else:
        print(f"❌ Error setting secret '{secret_name}': {response.status_code}")
        print(response.text)
        return False


# Main execution
print("Step 1: Getting repository public key...")
key_data = get_public_key()
public_key = key_data["key"]
key_id = key_data["key_id"]
print(f"✅ Public key retrieved (Key ID: {key_id})")
print()

print("Step 2: Adding AWS credentials as secrets...")
secrets = {
    "AWS_ACCESS_KEY_ID": AWS_ACCESS_KEY_ID,
    "AWS_SECRET_ACCESS_KEY": AWS_SECRET_ACCESS_KEY,
}

success_count = 0
for secret_name, secret_value in secrets.items():
    if create_or_update_secret(secret_name, secret_value, key_id, public_key):
        success_count += 1

print()
print("=" * 60)
print(f"Configuration Complete! ({success_count}/{len(secrets)} secrets configured)")
print("=" * 60)
print()
print("✅ Your GitHub repository is now configured with AWS credentials")
print("✅ GitHub Actions workflow can now deploy automatically")
print()
print("Next steps:")
print("1. Commit and push the workflow file to trigger deployment")
print("2. Check the 'Actions' tab in GitHub to monitor deployments")
print()
