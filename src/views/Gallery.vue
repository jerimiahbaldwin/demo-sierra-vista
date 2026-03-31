<!-- 
  🔒 PAGE CLAIMED BY AI AGENT
  This page is currently being worked on and should not be modified by other agents.
  Modeled after HouseFix WordPress template: https://housefix.wpengine.com/rtl-demo/
-->
<template>
  <div class="gallery-page">
    <!-- Hero Section -->
    <section class="hero-section"
      :style="{ backgroundImage: `url(/download/files/2022/10/1666359764724_img_20220907_153739863_hdr.jpg)` }">
      <div class="hero-overlay"></div>
      <div class="container">
        <div class="hero-content">
          <h1 class="hero-title">See Our Work</h1>
          <p class="hero-subtitle">Quality plumbing, heating, and cooling installations across Sierra Vista, AZ</p>
          <router-link to="/contact" class="btn btn-primary">Contact Us</router-link>
        </div>
      </div>
    </section>

    <!-- Introduction Section -->
    <section class="intro-section">
      <div class="container">
        <div class="intro-content">
          <h2>Professional Workmanship, Every Time</h2>
          <p class="lead">Take a look at some of our recent projects. With over 30 years of experience serving Sierra
            Vista and surrounding areas, we take pride in delivering quality installations and repairs. From complex
            HVAC systems to plumbing installations, our team handles every job with precision and care.</p>
        </div>
      </div>
    </section>

    <!-- Gallery Grid Section -->
    <section class="gallery-section">
      <div class="container">
        <div class="gallery-grid">
          <div v-for="(image, index) in galleryImages" :key="index" class="gallery-item"
            @click="openLightbox(index)">
            <div class="gallery-image-wrapper">
              <img :src="image.src" :alt="image.alt" class="gallery-image" loading="lazy" />
              <div class="gallery-overlay">
                <span class="view-icon">🔍</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Call to Action Section -->
    <section class="cta-section">
      <div class="container">
        <div class="cta-content">
          <h2>Ready to Start Your Project?</h2>
          <p>Contact us today for a free estimate on your plumbing, heating, or cooling needs.</p>
          <div class="cta-buttons">
            <a href="tel:5204172105" class="btn btn-primary">Call (520) 417-2105</a>
            <router-link to="/contact" class="btn btn-secondary">Request Estimate</router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Lightbox Modal -->
    <Teleport to="body">
      <div v-if="lightboxOpen" class="lightbox-modal" @click="closeLightbox">
        <button class="lightbox-close" @click.stop="closeLightbox">×</button>
        <button class="lightbox-prev" @click.stop="prevImage">‹</button>
        <button class="lightbox-next" @click.stop="nextImage">›</button>
        <div class="lightbox-content" @click.stop>
          <img :src="galleryImages[currentImageIndex].src" :alt="galleryImages[currentImageIndex].alt"
            class="lightbox-image" />
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Gallery | Sierra Vista Plumbing, Inc.',
  description: 'View our completed plumbing, heating, and air conditioning projects in Sierra Vista, AZ.',
  image: '/download/files/2022/10/1666359764724_img_20220907_153739863_hdr.jpg',
  url: '/gallery'
})

// Gallery images from the original site
const galleryImages = ref([
  {
    src: '/download/files/2022/10/1666359764724_img_20220907_153739863_hdr.jpg',
    alt: 'Professional HVAC installation'
  },
  {
    src: '/download/files/2022/10/1666359733654_img_20220927_161503744.jpg',
    alt: 'Plumbing service work'
  },
  {
    src: '/download/files/2022/10/1666359712804_img_20221006_115232764_hdr.jpg',
    alt: 'Heating system installation'
  },
  {
    src: '/download/files/2022/10/1666359691774_img_20220818_133724178.jpg',
    alt: 'Air conditioning repair'
  },
  {
    src: '/download/files/2020/07/23032354_783282055177141_8220129623951181476_n.jpg',
    alt: 'Commercial plumbing project'
  },
  {
    src: '/download/files/2020/07/1594751965643_20993095_751868368318510_8596883855423348288_n.jpg',
    alt: 'Residential HVAC work'
  },
  {
    src: '/download/files/2020/07/1594751975274_11175045_408957012609649_5451107137263283625_n.jpg',
    alt: 'Water heater installation'
  },
  {
    src: '/download/files/2020/07/1594751982538_11174980_407674432737907_8458628633811084202_n.jpg',
    alt: 'Duct cleaning service'
  },
  {
    src: '/download/files/2020/07/11167661_407673876071296_4966435864999835686_n.jpg',
    alt: 'Plumbing repair work'
  },
  {
    src: '/download/files/2020/07/11161339_408956759276341_7087623468737370888_n.jpg',
    alt: 'HVAC maintenance'
  },
  {
    src: '/download/files/2020/07/11108209_407675206071163_2777012138834212744_n.jpg',
    alt: 'Heating system repair'
  },
  {
    src: '/download/files/2020/07/11010289_411761418995875_4699240810552992315_n.jpg',
    alt: 'Air conditioning installation'
  },
  {
    src: '/download/files/2020/07/10389027_374375896067761_499326307120328047_n.jpg',
    alt: 'Commercial HVAC project'
  },
  {
    src: '/download/files/2020/07/23031361_783282038510476_1138368765012781407_n.jpg',
    alt: 'Plumbing installation'
  }
])

// Lightbox functionality
const lightboxOpen = ref(false)
const currentImageIndex = ref(0)

const openLightbox = (index) => {
  currentImageIndex.value = index
  lightboxOpen.value = true
  document.body.style.overflow = 'hidden'
}

const closeLightbox = () => {
  lightboxOpen.value = false
  document.body.style.overflow = ''
}

const nextImage = () => {
  currentImageIndex.value = (currentImageIndex.value + 1) % galleryImages.value.length
}

const prevImage = () => {
  currentImageIndex.value = (currentImageIndex.value - 1 + galleryImages.value.length) % galleryImages.value.length
}

// Keyboard navigation
import { onMounted, onUnmounted } from 'vue'

const handleKeydown = (e) => {
  if (!lightboxOpen.value) return
  if (e.key === 'Escape') closeLightbox()
  if (e.key === 'ArrowRight') nextImage()
  if (e.key === 'ArrowLeft') prevImage()
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
  document.body.style.overflow = ''
})
</script>

<style scoped>
/* Hero Section */
.hero-section {
  position: relative;
  height: 500px;
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(169, 14, 24, 0.85) 0%, rgba(0, 0, 0, 0.7) 100%);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 1;
}

.hero-content {
  text-align: center;
  color: white;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  font-weight: 300;
}

/* Buttons */
.btn {
  display: inline-block;
  padding: 1rem 2.5rem;
  font-size: 1.1rem;
  font-weight: 600;
  text-decoration: none;
  border-radius: 5px;
  transition: all 0.3s ease;
  cursor: pointer;
  border: none;
}

.btn-primary {
  background: #a90e18;
  color: white;
}

.btn-primary:hover {
  background: #8a0b14;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(169, 14, 24, 0.3);
}

.btn-secondary {
  background: white;
  color: #a90e18;
  border: 2px solid #a90e18;
  margin-left: 1rem;
}

.btn-secondary:hover {
  background: #a90e18;
  color: white;
}

/* Introduction Section */
.intro-section {
  padding: 5rem 0;
  background: #f8f9fa;
}

.intro-content {
  text-align: center;
  max-width: 900px;
  margin: 0 auto;
}

.intro-content h2 {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 1.5rem;
  font-weight: 700;
}

.lead {
  font-size: 1.2rem;
  line-height: 1.8;
  color: #5a6c7d;
}

/* Gallery Section */
.gallery-section {
  padding: 5rem 0;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

.gallery-item {
  cursor: pointer;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.gallery-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.gallery-image-wrapper {
  position: relative;
  width: 100%;
  padding-bottom: 100%;
  /* 1:1 Aspect Ratio */
  overflow: hidden;
}

.gallery-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.gallery-item:hover .gallery-image {
  transform: scale(1.1);
}

.gallery-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(169, 14, 24, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.gallery-item:hover .gallery-overlay {
  opacity: 1;
}

.view-icon {
  font-size: 3rem;
  color: white;
}

/* Call to Action Section */
.cta-section {
  background: linear-gradient(135deg, #a90e18 0%, #6d0912 100%);
  padding: 5rem 0;
  text-align: center;
}

.cta-content h2 {
  color: white;
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.cta-content p {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.3rem;
  margin-bottom: 2rem;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Lightbox Modal */
.lightbox-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.95);
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.lightbox-content {
  max-width: 90vw;
  max-height: 90vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox-image {
  max-width: 100%;
  max-height: 90vh;
  object-fit: contain;
  border-radius: 8px;
}

.lightbox-close,
.lightbox-prev,
.lightbox-next {
  position: absolute;
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  font-size: 3rem;
  cursor: pointer;
  padding: 1rem 1.5rem;
  transition: background 0.3s ease;
  backdrop-filter: blur(10px);
}

.lightbox-close:hover,
.lightbox-prev:hover,
.lightbox-next:hover {
  background: rgba(255, 255, 255, 0.3);
}

.lightbox-close {
  top: 1rem;
  right: 1rem;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  padding: 0;
  line-height: 1;
}

.lightbox-prev {
  left: 1rem;
  top: 50%;
  transform: translateY(-50%);
  border-radius: 5px;
}

.lightbox-next {
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  border-radius: 5px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }

  .hero-subtitle {
    font-size: 1.2rem;
  }

  .intro-content h2,
  .cta-content h2 {
    font-size: 2rem;
  }

  .gallery-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
  }

  .btn-secondary {
    margin-left: 0;
    margin-top: 1rem;
  }

  .cta-buttons {
    flex-direction: column;
    align-items: center;
  }

  .lightbox-prev,
  .lightbox-next {
    font-size: 2rem;
    padding: 0.5rem 1rem;
  }

  .lightbox-close {
    width: 50px;
    height: 50px;
    font-size: 2rem;
  }
}
</style>
