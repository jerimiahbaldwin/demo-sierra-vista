<!-- 
  PAGE CLAIMED BY AI AGENT
  This page is currently being worked on and should not be modified by other agents.
  Modeled after HouseFix WordPress template: https://housefix.wpengine.com/rtl-demo/
-->
<template>
  <div class="service-area-page">
    <section class="hero-section" :style="{ backgroundImage: `url(/download/files/2019/02/1551296179350_bigstock_124843106.jpg)` }">
      <div class="hero-overlay"></div>
      <div class="container">
        <div class="hero-content">
          <h1 class="hero-title">Service Area</h1>
          <p class="hero-subtitle">Reliable plumbing and HVAC support across Cochise County</p>
          <a href="tel:5204172105" class="btn btn-primary">Call (520) 417-2105</a>
        </div>
      </div>
    </section>

    <section class="coverage-section">
      <div class="container">
        <div class="section-header">
          <h2>Where We Work</h2>
          <p>
            Sierra Vista Plumbing, Inc. proudly serves homeowners and businesses throughout our surrounding communities.
          </p>
        </div>
        <div class="coverage-grid">
          <article class="coverage-card" v-for="area in serviceAreas" :key="area.city">
            <h3>{{ area.city }}</h3>
            <p>{{ area.description }}</p>
          </article>
        </div>
      </div>
    </section>

    <section class="map-section">
      <div class="container">
        <div class="map-layout">
          <div class="map-copy">
            <h2>Find Us On The Map</h2>
            <p>
              Visit us at our Sierra Vista office or contact us to schedule service at your property. We provide prompt
              response times and dependable workmanship.
            </p>
            <ul class="office-details">
              <li><strong>Main Office:</strong> 4847 South Hwy 92, Sierra Vista, AZ 85650</li>
              <li><strong>Primary Phone:</strong> <a href="tel:5204172105">(520) 417-2105</a></li>
              <li><strong>Second Office:</strong> <a href="tel:5205592534">(520) 559-2534</a></li>
            </ul>
            <router-link to="/contact" class="btn btn-secondary">Request An Estimate</router-link>
          </div>
          <div class="map-frame">
            <iframe
              src="https://www.google.com/maps/d/embed?mid=1DhEpFEog4WlGWnUYPf9svdSSQFZs3YUb"
              width="100%"
              height="480"
              style="border:0;"
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              title="Sierra Vista Plumbing service area map"
            ></iframe>
          </div>
        </div>
      </div>
    </section>

    <section class="cta-section">
      <div class="container">
        <div class="cta-card">
          <h2>Need Service In Your Area?</h2>
          <p>Call now to confirm availability and book an appointment with Sierra Vista Plumbing, Inc.</p>
          <div class="cta-actions">
            <a href="tel:5204172105" class="btn btn-primary">Call Now</a>
            <router-link to="/contact" class="btn btn-white">Contact Us</router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Service Area | Sierra Vista Plumbing, Inc.',
  description: 'Sierra Vista Plumbing, Inc. serves Sierra Vista, Bisbee, Benson, Huachuca City and Whetstone with dependable plumbing and HVAC services.',
  image: '/download/files/2019/02/1551296179350_bigstock_124843106.jpg',
  url: '/service-area'
})

const serviceAreas = [
  {
    city: 'Sierra Vista, AZ',
    description: 'Our primary service hub with full residential and commercial plumbing and HVAC support.'
  },
  {
    city: 'Bisbee, AZ',
    description: 'Trusted repairs, maintenance and installation services for homes and local businesses.'
  },
  {
    city: 'Benson, AZ',
    description: 'Fast response for heating, cooling and plumbing needs throughout the Benson area.'
  },
  {
    city: 'Huachuca City, AZ',
    description: 'Reliable service appointments from licensed technicians committed to quality work.'
  },
  {
    city: 'Whetstone, AZ',
    description: 'Routine service and urgent repairs to keep your systems running safely and efficiently.'
  }
]
</script>

<style scoped>
.hero-section {
  position: relative;
  min-height: 460px;
  display: flex;
  align-items: center;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  color: #fff;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(169, 14, 24, 0.82), rgba(15, 15, 15, 0.76));
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 760px;
}

.hero-title {
  font-size: 3rem;
  line-height: 1.1;
  margin-bottom: 1rem;
}

.hero-subtitle {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  opacity: 0.95;
}

.coverage-section {
  padding: 5rem 0;
  background: #f7f7f6;
}

.section-header {
  text-align: center;
  max-width: 740px;
  margin: 0 auto 2.5rem;
}

.section-header h2 {
  font-size: 2.3rem;
  color: #2f2f2f;
  margin-bottom: 0.8rem;
}

.section-header p {
  color: #5f5f5f;
  line-height: 1.7;
}

.coverage-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.25rem;
}

.coverage-card {
  background: #fff;
  border: 1px solid #ece8e5;
  border-top: 4px solid #a90e18;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.04);
}

.coverage-card h3 {
  color: #1f1f1f;
  margin-bottom: 0.6rem;
  font-size: 1.1rem;
}

.coverage-card p {
  color: #636363;
  line-height: 1.65;
}

.map-section {
  padding: 5rem 0;
  background: #fff;
}

.map-layout {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 2rem;
  align-items: start;
}

.map-copy h2 {
  font-size: 2rem;
  color: #2f2f2f;
  margin-bottom: 1rem;
}

.map-copy p {
  color: #616161;
  line-height: 1.7;
  margin-bottom: 1.25rem;
}

.office-details {
  list-style: none;
  padding: 0;
  margin: 0 0 1.5rem;
}

.office-details li {
  margin-bottom: 0.75rem;
  color: #404040;
}

.office-details a {
  color: #a90e18;
}

.map-frame iframe {
  border-radius: 8px;
  box-shadow: 0 14px 30px rgba(0, 0, 0, 0.08);
}

.cta-section {
  padding: 4rem 0 5rem;
  background: linear-gradient(180deg, #f6f2ef 0%, #efe4de 100%);
}

.cta-card {
  background: #1f1f1f;
  color: #fff;
  border-radius: 12px;
  padding: 2.5rem;
  text-align: center;
}

.cta-card h2 {
  font-size: 2rem;
  margin-bottom: 0.75rem;
}

.cta-card p {
  color: #e8e8e8;
  margin-bottom: 1.5rem;
}

.cta-actions {
  display: flex;
  justify-content: center;
  gap: 0.9rem;
  flex-wrap: wrap;
}

@media (max-width: 900px) {
  .hero-title {
    font-size: 2.2rem;
  }

  .map-layout {
    grid-template-columns: 1fr;
  }
}
</style>
