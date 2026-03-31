<template>
  <div class="page-container">
    <h1>Reviews</h1>
    <p>See what our customers are saying</p>
    <!-- Content to be populated -->
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Reviews | Sierra Vista Plumbing, Inc.',
  url: '/reviews'
})
</script>

<style scoped>
.page-container {
  padding: 2rem;
}
</style>
