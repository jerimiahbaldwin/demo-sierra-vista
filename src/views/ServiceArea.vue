<template>
  <div class="page-container">
    <h1>Service Area</h1>
    <p>Areas we serve in Arizona</p>
    <!-- Content to be populated -->
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Service Area | Sierra Vista Plumbing, Inc.',
  url: '/service-area'
})
</script>

<style scoped>
.page-container {
  padding: 2rem;
}
</style>
