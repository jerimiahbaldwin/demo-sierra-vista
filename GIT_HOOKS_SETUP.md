# Git Hooks Setup

## Pre-Push Hook

A pre-push hook has been configured to run the build process before allowing code to be pushed to the remote repository. This helps catch build errors locally before they trigger CI/CD failures.

### What it does

- Runs `npm run build` before each push
- If the build fails, the push is blocked
- If the build succeeds, the push proceeds normally

### Hook Location

The hook is located at: `.git/hooks/pre-push`

### How to Test

Try pushing code with a syntax error in a Vue file - the hook will catch it and prevent the push.

### Bypassing the Hook (not recommended)

If you absolutely need to bypass the hook:
```bash
git push --no-verify
```

However, this is not recommended as it defeats the purpose of having the hook.

## Build Issues Fixed

### Issue 1: FAQ.vue Template Error (GitHub Actions #4, #5, #15, #16)

**Problem:** The FAQ.vue file had duplicate opening `<template>` tags but only one closing tag, causing parse errors.

**Error Message:**
```
[vite:vue] [plugin vite:vue] src/views/FAQ.vue (1:1): Element is missing end tag.
```

**Solution:** Removed the duplicate `<template>` tag on line 1.

**Files Changed:**
- `src/views/FAQ.vue` - Fixed template syntax error

### Testing Locally

Before pushing, you can manually test the build:

```bash
npm run build
```

This will:
1. Generate the sitemap and robots.txt
2. Build the Vue application with Vite
3. Report any errors if they exist

### CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/deploy.yml`) runs these same checks automatically on push to master/main branches:

1. Checkout code
2. Setup Node.js
3. Install dependencies with `npm ci`
4. **Build the application** ← This is where the errors were caught
5. Deploy to S3
6. Invalidate CloudFront cache

The pre-push hook ensures you catch any build issues at step #4 before they reach GitHub Actions.
