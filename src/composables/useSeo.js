import { useHead } from "@vueuse/head";

/**
 * Composable for managing SEO metadata on individual pages
 * @param {Object} config - SEO configuration
 * @param {string} config.title - Page title
 * @param {string} config.description - Meta description
 * @param {string} config.image - Open Graph image URL
 * @param {string} config.url - Canonical URL (relative path)
 * @param {Object} config.schema - JSON-LD schema object (optional)
 */
export function useSeo(config) {
  const {
    title = "Sierra Vista Plumbing, Inc.",
    description = "Sierra Vista Plumbing, Inc. is a plumber in Sierra Vista, AZ. Our services include HVAC services, plumbing services and so much more! Give us a call today! (520) 417-2105",
    image = "/images/heroes/hvac-units.jpg",
    url = "",
    schema = null,
  } = config;

  const fullUrl = `https://demo-sierra-vista.com${url}`;

  const headConfig = {
    title,
    meta: [
      // Description
      {
        name: "description",
        content: description,
      },
      {
        itemprop: "description",
        content: description,
      },

      // Open Graph
      {
        property: "og:title",
        content: title,
      },
      {
        property: "og:description",
        content: description,
      },
      {
        property: "og:image",
        content: image,
      },
      {
        property: "og:url",
        content: fullUrl,
      },
      {
        property: "og:site_name",
        content: "Sierra Vista Plumbing, Inc.",
      },
      {
        property: "og:type",
        content: "website",
      },
    ],
    link: [
      // Canonical URL
      {
        rel: "canonical",
        href: fullUrl,
      },
    ],
  };

  // Add JSON-LD schema if provided
  if (schema) {
    headConfig.script = [
      {
        type: "application/ld+json",
        children: JSON.stringify(schema),
      },
    ];
  }

  useHead(headConfig);
}

/**
 * Generate the organization schema for the business
 */
export function getOrganizationSchema() {
  return {
    "@context": "http://www.schema.org",
    "@type": "ProfessionalService",
    name: "Sierra Vista Plumbing, Inc",
    url: "https://demo-sierra-vista.com/",
    logo: "/images/logo/sierra-vista-logo.png",
    description:
      "Sierra Vista Plumbing, Inc. is a plumber in Sierra Vista, AZ. Our services include HVAC services, plumbing services and so much more! Give us a call today! (520) 417-2105",
    address: {
      "@type": "PostalAddress",
      streetAddress: "4847 South Hwy 92",
      addressLocality: "Sierra Vista",
      addressRegion: "AZ",
      postalCode: "85650",
      addressCountry: "United States",
    },
    hasMap:
      "https://www.google.com/maps?ll=31.480784,-110.256949&z=15&t=m&hl=en-US&gl=US&mapclient=embed&q=4847+AZ-92+Sierra+Vista,+AZ+85650",
    openingHours: "Mo, Tu, We, Th, Fr 08:00-17:00",
    contactPoint: {
      "@type": "ContactPoint",
      telephone: "(520) 417-2105",
    },
  };
}
