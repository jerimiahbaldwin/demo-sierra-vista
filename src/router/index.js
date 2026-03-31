import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import AirConditioningInstallation from '../views/AirConditioningInstallation.vue'
import AirConditioningRepair from '../views/AirConditioningRepair.vue'
import AirConditioningServices from '../views/AirConditioningServices.vue'
import HeatingInstallation from '../views/HeatingInstallation.vue'
import HeatingMaintenance from '../views/HeatingMaintenance.vue'
import HeatingRepair from '../views/HeatingRepair.vue'
import HeatingServices from '../views/HeatingServices.vue'
import DryerVentCleaning from '../views/DryerVentCleaning.vue'
import DuctCleaning from '../views/DuctCleaning.vue'
import PlumbingServices from '../views/PlumbingServices.vue'
import GreasePumping from '../views/GreasePumping.vue'
import Gallery from '../views/Gallery.vue'
import Reviews from '../views/Reviews.vue'
import FAQ from '../views/FAQ.vue'
import ServiceArea from '../views/ServiceArea.vue'
import Contact from '../views/Contact.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    alias: ['/index.html', '/index']
  },
  {
    path: '/air-conditioning-installation',
    name: 'AirConditioningInstallation',
    component: AirConditioningInstallation,
    alias: '/air-conditioning-installation.html'
  },
  {
    path: '/air-conditioning-repair',
    name: 'AirConditioningRepair',
    component: AirConditioningRepair,
    alias: '/air-conditioning-repair.html'
  },
  {
    path: '/air-conditioning-services',
    name: 'AirConditioningServices',
    component: AirConditioningServices,
    alias: '/air-conditioning-services.html'
  },
  {
    path: '/heating-installation',
    name: 'HeatingInstallation',
    component: HeatingInstallation,
    alias: '/heating-installation.html'
  },
  {
    path: '/heating-maintenance',
    name: 'HeatingMaintenance',
    component: HeatingMaintenance,
    alias: '/heating-maintenance.html'
  },
  {
    path: '/heating-repair',
    name: 'HeatingRepair',
    component: HeatingRepair,
    alias: '/heating-repair.html'
  },
  {
    path: '/heating-services',
    name: 'HeatingServices',
    component: HeatingServices,
    alias: '/heating-services.html'
  },
  {
    path: '/dryer-vent-rotobrush-cleaning-services',
    name: 'DryerVentCleaning',
    component: DryerVentCleaning,
    alias: '/dryer-vent-rotobrush-cleaning-services.html'
  },
  {
    path: '/duct-cleaning-services',
    name: 'DuctCleaning',
    component: DuctCleaning,
    alias: '/duct-cleaning-services.html'
  },
  {
    path: '/plumbing-services',
    name: 'PlumbingServices',
    component: PlumbingServices,
    alias: '/plumbing-services.html'
  },
  {
    path: '/grease-pumping-services',
    name: 'GreasePumping',
    component: GreasePumping,
    alias: '/grease-pumping-services.html'
  },
  {
    path: '/gallery',
    name: 'Gallery',
    component: Gallery,
    alias: '/gallery.html'
  },
  {
    path: '/reviews',
    name: 'Reviews',
    component: Reviews,
    alias: '/reviews.html'
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: FAQ,
    alias: '/faq.html'
  },
  {
    path: '/service-area',
    name: 'ServiceArea',
    component: ServiceArea,
    alias: '/service-area.html'
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router
