import { fileURLToPath } from "url";
import { dirname, join } from "path";
import { writeFileSync, mkdirSync } from "fs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Configuration
const SITE_URL = "https://d2gpxm7g9jp1jd.cloudfront.net";
const OUTPUT_DIR = join(__dirname, "..", "public");

// Route configuration with priorities and change frequencies
const routeConfig = {
  "/": { priority: 1.0, changefreq: "weekly" },
  "/contact": { priority: 0.9, changefreq: "monthly" },
  "/air-conditioning-installation": { priority: 0.8, changefreq: "monthly" },
  "/air-conditioning-repair": { priority: 0.8, changefreq: "monthly" },
  "/air-conditioning-services": { priority: 0.8, changefreq: "monthly" },
  "/heating-installation": { priority: 0.8, changefreq: "monthly" },
  "/heating-maintenance": { priority: 0.8, changefreq: "monthly" },
  "/heating-repair": { priority: 0.8, changefreq: "monthly" },
  "/heating-services": { priority: 0.8, changefreq: "monthly" },
  "/plumbing-services": { priority: 0.8, changefreq: "monthly" },
  "/dryer-vent-rotobrush-cleaning-services": {
    priority: 0.7,
    changefreq: "monthly",
  },
  "/duct-cleaning-services": { priority: 0.7, changefreq: "monthly" },
  "/grease-pumping-services": { priority: 0.7, changefreq: "monthly" },
  "/service-area": { priority: 0.7, changefreq: "monthly" },
  "/reviews": { priority: 0.7, changefreq: "weekly" },
  "/gallery": { priority: 0.6, changefreq: "weekly" },
  "/faq": { priority: 0.6, changefreq: "monthly" },
};

function generateSitemap() {
  const today = new Date().toISOString().split("T")[0];

  const urls = Object.entries(routeConfig)
    .map(([path, config]) => {
      return `  <url>
    <loc>${SITE_URL}${path}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${config.changefreq}</changefreq>
    <priority>${config.priority}</priority>
  </url>`;
    })
    .join("\n  \n");

  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  
${urls}
  
</urlset>`;

  return sitemap;
}

function generateRobotsTxt() {
  return `# Robots.txt for Sierra Vista HVAC Services

User-agent: *
Allow: /

# Sitemap location
Sitemap: ${SITE_URL}/sitemap.xml

# Disallow admin or private paths (add if needed)
# Disallow: /admin/
# Disallow: /private/
`;
}

// Main execution
try {
  console.log("🔨 Generating SEO files...");

  // Ensure public directory exists
  mkdirSync(OUTPUT_DIR, { recursive: true });

  // Generate sitemap.xml
  const sitemap = generateSitemap();
  const sitemapPath = join(OUTPUT_DIR, "sitemap.xml");
  writeFileSync(sitemapPath, sitemap, "utf-8");
  console.log("✅ Generated sitemap.xml");

  // Generate robots.txt
  const robotsTxt = generateRobotsTxt();
  const robotsPath = join(OUTPUT_DIR, "robots.txt");
  writeFileSync(robotsPath, robotsTxt, "utf-8");
  console.log("✅ Generated robots.txt");

  console.log(`📍 Site URL: ${SITE_URL}`);
  console.log(`📄 ${Object.keys(routeConfig).length} pages in sitemap`);
  console.log("✨ SEO files generated successfully!");
} catch (error) {
  console.error("❌ Error generating SEO files:", error);
  process.exit(1);
}
