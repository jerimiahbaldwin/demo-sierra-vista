<template>
  <div class="page-container">
    <h1>Frequently Asked Questions</h1>
    <p>Find answers to common questions</p>
    <!-- Content to be populated -->
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'FAQ | Sierra Vista Plumbing, Inc.',
  image: '/download/wp-content/uploads//b2b/stock/v2/bigstock/bath-wrench-plumling-7068036.jpg',
  url: '/faq'
})
</script>

<style scoped>
.page-container {
  padding: 2rem;
}
</style>
