# URL Mapping - SEO Preservation

This document maps all URLs from the original sierravistaplumbing.com site to the new Vue.js application routes.

## All URLs Preserved (17 pages)

| Original URL | Vue Route | Component | Aliases |
|-------------|-----------|-----------|---------|
| `/` or `/index.html` | `/` | Home.vue | `/index.html`, `/index` |
| `/air-conditioning-installation` or `/air-conditioning-installation.html` or `/air-conditioning-installation/` | `/air-conditioning-installation` | AirConditioningInstallation.vue | `/air-conditioning-installation.html` |
| `/air-conditioning-repair` or `/air-conditioning-repair.html` or `/air-conditioning-repair/` | `/air-conditioning-repair` | AirConditioningRepair.vue | `/air-conditioning-repair.html` |
| `/air-conditioning-services` or `/air-conditioning-services.html` or `/air-conditioning-services/` | `/air-conditioning-services` | AirConditioningServices.vue | `/air-conditioning-services.html` |
| `/heating-installation` or `/heating-installation.html` or `/heating-installation/` | `/heating-installation` | HeatingInstallation.vue | `/heating-installation.html` |
| `/heating-maintenance` or `/heating-maintenance.html` or `/heating-maintenance/` | `/heating-maintenance` | HeatingMaintenance.vue | `/heating-maintenance.html` |
| `/heating-repair` or `/heating-repair.html` or `/heating-repair/` | `/heating-repair` | HeatingRepair.vue | `/heating-repair.html` |
| `/heating-services` or `/heating-services.html` or `/heating-services/` | `/heating-services` | HeatingServices.vue | `/heating-services.html` |
| `/dryer-vent-rotobrush-cleaning-services` or `/dryer-vent-rotobrush-cleaning-services.html` or `/dryer-vent-rotobrush-cleaning-services/` | `/dryer-vent-rotobrush-cleaning-services` | DryerVentCleaning.vue | `/dryer-vent-rotobrush-cleaning-services.html` |
| `/duct-cleaning-services` or `/duct-cleaning-services.html` or `/duct-cleaning-services/` | `/duct-cleaning-services` | DuctCleaning.vue | `/duct-cleaning-services.html` |
| `/plumbing-services` or `/plumbing-services.html` or `/plumbing-services/` | `/plumbing-services` | PlumbingServices.vue | `/plumbing-services.html` |
| `/grease-pumping-services` or `/grease-pumping-services.html` or `/grease-pumping-services/` | `/grease-pumping-services` | GreasePumping.vue | `/grease-pumping-services.html` |
| `/gallery` or `/gallery.html` or `/gallery/` | `/gallery` | Gallery.vue | `/gallery.html` |
| `/reviews` or `/reviews.html` or `/reviews/` | `/reviews` | Reviews.vue | `/reviews.html` |
| `/faq` or `/faq.html` or `/faq/` | `/faq` | FAQ.vue | `/faq.html` |
| `/service-area` or `/service-area.html` or `/service-area/` | `/service-area` | ServiceArea.vue | `/service-area.html` |
| `/contact` or `/contact/` | `/contact` | Contact.vue | - |

## SEO Considerations

### URL Formats Supported
- **Clean URLs**: `/page-name` (primary)
- **Legacy HTML**: `/page-name.html` (via route alias)
- **Trailing Slash**: `/page-name/` (handled by Vue Router history mode)

### Benefits
- ✅ All backlinks preserved
- ✅ Search engine rankings maintained
- ✅ No 404 errors from old URLs
- ✅ Clean URL structure for new links
- ✅ Automatic trailing slash handling

### Notes
- All routes use Vue Router's HTML5 history mode
- CloudFront and S3 must be configured to serve index.html for all paths
- .html aliases ensure backward compatibility with old site structure
