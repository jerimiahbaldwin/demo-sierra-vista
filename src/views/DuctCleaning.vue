<!-- 
  PAGE CLAIMED BY AI AGENT
  This page is currently being worked on and should not be modified by other agents.
  Modeled after HouseFix WordPress template: https://housefix.wpengine.com/rtl-demo/
-->
<template>
  <div class="duct-cleaning-page">
    <!-- Hero Section -->
    <section class="hero-section"
      :style="{ backgroundImage: `url(/download/files/shutterstock/2024/04/shutterstock_1122500891_1712000690_e1684083920b7e1f47254466fef9260743.jpg)` }">
      <div class="hero-overlay"></div>
      <div class="container">
        <div class="hero-content">
          <h1 class="hero-title">Enjoy Clean Air in Your Property</h1>
          <p class="hero-subtitle">Get duct cleaning services in Sierra Vista, AZ</p>
          <router-link to="/contact" class="btn btn-primary">Schedule Service</router-link>
        </div>
      </div>
    </section>

    <!-- Introduction Section -->
    <section class="intro-section">
      <div class="container">
        <div class="intro-content">
          <h2>Professional Duct Cleaning Services</h2>
          <p class="lead">Dusty, debris-filled ducts can cause all kinds of issues from rising energy bills to chronic
            health problems. If you're looking for a duct cleaning specialist in Sierra Vista, AZ, turn to Sierra Vista
            Plumbing, Inc. We offer high-quality duct cleaning services. You can trust us to clear out anything that's
            preventing clean air from flowing through your ducts properly.</p>
          <router-link to="/contact" class="btn btn-secondary">Get In Touch With Us</router-link>
        </div>
      </div>
    </section>

    <!-- Benefits Section -->
    <section class="benefits-section">
      <div class="container">
        <div class="section-header">
          <h2>Discover The Benefits Of Cleaning Out Your Air Ducts</h2>
          <p>Nobody wants to breathe in air that's coming out of filthy ducts. Fortunately, you can depend on us to
            cover all your duct cleaning needs.</p>
        </div>
        <div class="benefits-grid">
          <div class="benefit-card">
            <div class="benefit-icon">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
            </div>
            <h3>Clean Living Environment</h3>
            <p>Make sure that you have a clean living environment free from dust and debris buildup.</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h3>Remove Allergens</h3>
            <p>Remove allergens from your indoor air that can trigger allergic reactions and breathing issues.</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
              </svg>
            </div>
            <h3>Reduce Respiratory Symptoms</h3>
            <p>Get rid of irritants that can worsen respiratory symptoms and improve indoor air quality.</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3>Boost HVAC Efficiency</h3>
            <p>Boost the efficiency of your HVAC system and lower your energy bills with cleaner ducts.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Service Areas Section -->
    <section class="service-areas-section">
      <div class="container">
        <div class="service-areas-grid">
          <div class="service-areas-content">
            <h2>Service Areas</h2>
            <p>We proudly serve the following areas:</p>
            <ul class="areas-list">
              <li>Sierra Vista, AZ</li>
              <li>Bisbee, AZ</li>
              <li>Benson, AZ</li>
              <li>Huachuca City, AZ</li>
              <li>Whetstone, AZ</li>
            </ul>
          </div>
          <div class="service-areas-map">
            <iframe src="https://www.google.com/maps/d/embed?mid=1DhEpFEog4WlGWnUYPf9svdSSQFZs3YUb" width="100%"
              height="480" style="border:0;" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
            </iframe>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="container">
        <div class="cta-content">
          <h2>Ready For Cleaner Air?</h2>
          <p>Contact Sierra Vista Plumbing, Inc. today to schedule your duct cleaning service</p>
          <div class="cta-buttons">
            <router-link to="/contact" class="btn btn-primary">Contact Us</router-link>
            <a href="tel:5204172105" class="btn btn-white">Call: (520) 417-2105</a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Duct Cleaning Services | Sierra Vista, AZ | Sierra Vista Plumbing, Inc.',
  description: 'We offer high-quality duct cleaning services. You can trust us to clear out anything that\'s preventing clean air from flowing through your ducts properly.',
  image: '/download/files/shutterstock/2024/04/shutterstock_1122500891_1712000690_e1684083920b7e1f47254466fef9260743.jpg',
  url: '/duct-cleaning-services'
})
</script>

<style scoped>
/* Hero Section */
.hero-section {
  position: relative;
  min-height: 500px;
  display: flex;
  align-items: center;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  color: white;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(169, 14, 24, 0.85) 0%, rgba(0, 0, 0, 0.7) 100%);
}

.hero-content {
  position: relative;
  z-index: 1;
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  opacity: 0.95;
}

/* Introduction Section */
.intro-section {
  padding: 5rem 0;
  background: #f8f9fa;
}

.intro-content {
  max-width: 800px;
  margin: 0 auto;
  text-align: center;
}

.intro-content h2 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1.5rem;
}

.lead {
  font-size: 1.125rem;
  line-height: 1.8;
  color: #555;
  margin-bottom: 2rem;
}

/* Benefits Section */
.benefits-section {
  padding: 5rem 0;
  background: white;
}

.section-header {
  text-align: center;
  max-width: 800px;
  margin: 0 auto 4rem;
}

.section-header h2 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1rem;
}

.section-header p {
  font-size: 1.125rem;
  color: #666;
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.benefit-card {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.benefit-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.benefit-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto 1.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #a90e18;
  color: white;
  border-radius: 50%;
}

.benefit-icon svg {
  width: 40px;
  height: 40px;
}

.benefit-card h3 {
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 1rem;
}

.benefit-card p {
  color: #666;
  line-height: 1.6;
}

/* Service Areas Section */
.service-areas-section {
  padding: 5rem 0;
  background: #f8f9fa;
}

.service-areas-grid {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 3rem;
  align-items: start;
}

.service-areas-content h2 {
  font-size: 2rem;
  color: #333;
  margin-bottom: 1rem;
}

.service-areas-content p {
  font-size: 1.125rem;
  color: #666;
  margin-bottom: 1.5rem;
}

.areas-list {
  list-style: none;
  padding: 0;
}

.areas-list li {
  padding: 0.75rem 0;
  border-bottom: 1px solid #ddd;
  color: #555;
  font-size: 1.125rem;
}

.areas-list li:last-child {
  border-bottom: none;
}

.service-areas-map iframe {
  border-radius: 8px;
}

/* CTA Section */
.cta-section {
  background: linear-gradient(135deg, #a90e18 0%, #770a12 100%);
  color: white;
  padding: 5rem 0;
  text-align: center;
}

.cta-content h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.cta-content p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  opacity: 0.95;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Buttons */
.btn {
  display: inline-block;
  padding: 1rem 2rem;
  font-size: 1.125rem;
  font-weight: 600;
  text-decoration: none;
  border-radius: 4px;
  transition: all 0.3s ease;
  border: 2px solid transparent;
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
  background: #333;
  color: white;
}

.btn-secondary:hover {
  background: #555;
}

.btn-white {
  background: white;
  color: #a90e18;
  border-color: white;
}

.btn-white:hover {
  background: transparent;
  color: white;
  border-color: white;
}

/* Container */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }

  .hero-subtitle {
    font-size: 1.125rem;
  }

  .intro-content h2,
  .section-header h2 {
    font-size: 1.875rem;
  }

  .service-areas-grid {
    grid-template-columns: 1fr;
  }

  .benefits-grid {
    grid-template-columns: 1fr;
  }

  .cta-buttons {
    flex-direction: column;
    align-items: stretch;
  }

  .btn {
    width: 100%;
    text-align: center;
  }
}
</style>
