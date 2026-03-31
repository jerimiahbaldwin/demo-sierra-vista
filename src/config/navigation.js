// Navigation menu configuration
export const navigationMenu = [
  { path: "/", label: "Home", type: "link" },
  {
    label: "Heating",
    type: "dropdown",
    items: [
      { path: "/heating-services", label: "Heating Services" },
      { path: "/heating-installation", label: "Installation" },
      { path: "/heating-repair", label: "Repair" },
      { path: "/heating-maintenance", label: "Maintenance" },
    ],
  },
  {
    label: "Air Conditioning",
    type: "dropdown",
    items: [
      {
        path: "/air-conditioning-services",
        label: "AC Services",
      },
      { path: "/air-conditioning-installation", label: "Installation" },
      { path: "/air-conditioning-repair", label: "Repair" },
    ],
  },
  {
    label: "Other Services",
    type: "dropdown",
    items: [
      { path: "/plumbing-services", label: "Plumbing" },
      { path: "/duct-cleaning-services", label: "Duct Cleaning" },
      {
        path: "/dryer-vent-rotobrush-cleaning-services",
        label: "Dryer Vent Cleaning",
      },
      { path: "/grease-pumping-services", label: "Grease Pumping" },
    ],
  },
  { path: "/contact", label: "Contact", type: "link" },
];

// Company contact information
export const contactInfo = {
  phone: "(520) 417-2105",
  phoneRaw: "5204172105",
  address: {
    street: "4847 South Hwy 92",
    city: "Sierra Vista",
    state: "AZ",
    zip: "85650",
  },
  social: {
    facebook:
      "http://www.facebook.com/Sierra-Vista-Plumbing-Inc-Hvac-363355883836429",
    googleMaps:
      "https://maps.google.com/maps?daddr=4847 South Hwy 92, Sierra Vista, AZ 85650",
  },
};
