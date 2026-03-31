<template>
  <div class="page-container">
    <h1>Gallery</h1>
    <p>View our completed projects and work</p>
    <!-- Content to be populated -->
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Gallery | Sierra Vista Plumbing, Inc.',
  image: '/download/files/2022/10/1666359764724_img_20220907_153739863_hdr.jpg',
  url: '/gallery'
})
</script>

<style scoped>
.page-container {
  padding: 2rem;
}
</style>
