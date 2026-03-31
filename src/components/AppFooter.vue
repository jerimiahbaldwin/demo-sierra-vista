<template>
  <footer class="site-footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-col">
          <h4>About Us</h4>
          <p>Sierra Vista Plumbing, Inc. provides professional plumbing and HVAC services to Sierra Vista, AZ and
            surrounding areas.</p>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><router-link to="/plumbing-services">Plumbing Services</router-link></li>
            <li><router-link to="/heating-services">Heating Services</router-link></li>
            <li><router-link to="/air-conditioning-services">Air Conditioning</router-link></li>
            <li><router-link to="/duct-cleaning-services">Duct Cleaning</router-link></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contact</h4>
          <p>
            {{ contactInfo.address.street }}<br>
            {{ contactInfo.address.city }}, {{ contactInfo.address.state }} {{ contactInfo.address.zip }}
          </p>
          <p><a :href="`tel:${contactInfo.phoneRaw}`">{{ contactInfo.phone }}</a></p>
        </div>
        <div class="footer-col">
          <h4>Follow Us</h4>
          <div class="social-links">
            <a :href="contactInfo.social.facebook" target="_blank" class="social-icon">Facebook</a>
            <a :href="contactInfo.social.googleMaps" target="_blank" class="social-icon">Google</a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; {{ currentYear }} Sierra Vista Plumbing, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { computed } from 'vue'
import { contactInfo } from '../config/navigation'

const currentYear = computed(() => new Date().getFullYear())
</script>
