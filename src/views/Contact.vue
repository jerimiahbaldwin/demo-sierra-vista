<template>
  <div class="page-container">
    <h1>Contact Us</h1>
    <p>Get in touch with Sierra Vista Plumbing</p>
    <!-- Content to be populated -->
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Contact A Plumber in Sierra Vista, AZ | Sierra Vista Plumbing, Inc.',
  description: 'We provide plumbing and HVAC services in Sierra Vista, AZ. We look forward to working in your home or commercial space soon. Give us a call at (520) 417-2105.',
  url: '/contact'
})
</script>

<style scoped>
.page-container {
  padding: 2rem;
}
</style>
