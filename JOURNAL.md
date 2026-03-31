# Website Build Journal

> **Note**: Keep all journal entries to a single line for brevity and clarity.

## Steps to Build the Website

- **Step 1**: Initialized Git repository (March 30, 2026)
- **Step 2**: Created .gitignore file to exclude .env and other sensitive files (March 30, 2026)
- **Step 3**: Brought over .env file with access credentials for GitHub and AWS (March 30, 2026)
- **Step 4**: Created GitHub repository 'demo-sierra-vista' and configured remote origin (March 30, 2026)
- **Step 5**: Created Hello World HTML page (index.html) and README.md, then pushed to GitHub (March 30, 2026)
- **Step 6**: Deployed to AWS with S3 bucket (demo-sierra-vista) and CloudFront distribution (E3A6BY8E3ZRJJ7) - S3: http://demo-sierra-vista.s3-website-us-east-1.amazonaws.com | CloudFront: https://d2gpxm7g9jp1jd.cloudfront.net (March 30, 2026)
- **Step 7**: Converted to Vue.js 3 project with Vite, npm dependencies, and dev server at http://localhost:3000 (March 30, 2026)
- **Step 8**: Created .instructions.md file with GitHub Copilot instructions requiring journal updates for all meaningful AI-assisted actions (March 30, 2026)
- **Step 9**: Created GitHub Actions CI/CD pipeline (.github/workflows/deploy.yml) for automated Vue build, S3 deployment, and CloudFront cache invalidation on main branch push (March 30, 2026)
- **Step 10**: Configured GitHub repository secrets (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY) programmatically using setup-github-secrets.py script with credentials from .env file (March 30, 2026)
- **Step 11**: Tested CI/CD pipeline by adding deployment indicator to Vue home page and pushing to master branch, triggering first automated GitHub Actions deployment (March 30, 2026)
- **Step 10**: Downloaded complete sierravistaplumbing.com website (56 files: HTML pages, CSS, JavaScript, images) to download/ folder with Python scripts (download-site.py, fix-absolute-urls.py) and converted all absolute URLs to relative paths for local browsing (March 30, 2026)
- **Step 11**: Redesigned Vue App.vue homepage using HouseFix template (https://housefix.wpengine.com/rtl-demo/) as design guide, incorporating Sierra Vista Plumbing content and local images from download/ directory - includes responsive layout with hero section, services grid, stats, about section, CTA, contact form, and footer (March 30, 2026)
- **Step 12**: Added Design Reference section to .instructions.md documenting HouseFix WordPress template as the design model for future pages and features (March 30, 2026)
- **Step 13**: Installed Vue Router 4 and created complete routing structure with 17 stub pages preserving all URLs from original site: Home (/), Air Conditioning Services (installation, repair, services), Heating Services (installation, maintenance, repair, services), Duct Cleaning, Dryer Vent Cleaning, Plumbing Services, Grease Pumping, Gallery, Reviews, FAQ, Service Area, and Contact (March 30, 2026)
- **Step 14**: Refactored App.vue from single-page homepage to layout component with sticky header navigation (including dropdown menus for service categories), router-view for page content, and shared footer - all service pages now have dedicated routes for SEO preservation (March 30, 2026)
- **Step 15**: Added route aliases in router to handle legacy .html URLs (e.g., /gallery.html → /gallery) ensuring all backlinks from original sierravistaplumbing.com site continue to work without 404 errors, preserving existing SEO value and search engine rankings (March 30, 2026)
- **Step 16**: Created URL_MAPPING.md documentation listing all 17 preserved URLs with their route mappings, aliases, and SEO preservation strategy for reference and verification (March 30, 2026)
- **Step 17**: Restored full homepage design to src/views/Home.vue (hero section, stats, services grid, about section, CTA, contact form) after router refactoring had replaced it with placeholder content (March 30, 2026)
