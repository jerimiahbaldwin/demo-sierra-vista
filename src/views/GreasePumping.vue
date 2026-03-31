<!-- 🔒 PAGE CLAIMED: This page is currently being populated with content by an AI agent. Please do not modify. -->
<template>
  <div class="grease-pumping-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-image">
        <img
          src="/images/services/grease-pumping.jpg"
          alt="Professional commercial grease trap pumping service" />
        <div class="hero-overlay">
          <div class="hero-content">
            <h1>Is Your Grease Trap Filled to the Brim?</h1>
            <h2>Count on us for grease pumping services in Sierra Vista, AZ</h2>
            <router-link to="/contact" class="cta-button">Schedule Service Now</router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Introduction Section -->
    <section class="intro-section">
      <div class="container">
        <div class="intro-content">
          <p class="lead">
            It doesn't have to be a hassle to empty your restaurant's grease trap. For reliable grease pumping services,
            depend on Sierra Vista Plumbing, Inc. We have experience pumping out grease traps for restaurants throughout
            the Sierra Vista, AZ area. We can get rid of any solid and liquid waste caught in your grease trap.
          </p>
          <p class="cta-text">
            Connect with us now to make an appointment for grease trap pumping services.
          </p>
        </div>
      </div>
    </section>

    <!-- Why It's Important Section -->
    <section class="importance-section">
      <div class="container">
        <div class="section-header">
          <h2>Don't Wait to Clear Out Your Full Grease Trap</h2>
          <p>Getting grease trap pumping services is an important part of maintaining a safe environment in your
            restaurant.</p>
        </div>

        <div class="reasons-grid">
          <div class="reason-card">
            <div class="reason-icon">🔥</div>
            <h3>Fire Safety</h3>
            <p>Irregular pumping can lead to a higher fire risk in your commercial kitchen</p>
          </div>

          <div class="reason-card">
            <div class="reason-icon">👃</div>
            <h3>Odor Control</h3>
            <p>Old grease and debris can cause unpleasant smells in your kitchen and dining areas</p>
          </div>

          <div class="reason-card">
            <div class="reason-icon">💧</div>
            <h3>Prevent Spills</h3>
            <p>Full grease traps have a higher chance of spilling and creating hazardous conditions</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Benefits Section -->
    <section class="benefits-section">
      <div class="container">
        <h2>Professional Grease Trap Pumping You Can Trust</h2>
        <div class="benefits-list">
          <div class="benefit-item">
            <div class="benefit-icon">✓</div>
            <div class="benefit-text">
              <h3>Experienced Team</h3>
              <p>Years of experience serving restaurants and commercial kitchens in Sierra Vista</p>
            </div>
          </div>

          <div class="benefit-item">
            <div class="benefit-icon">✓</div>
            <div class="benefit-text">
              <h3>Complete Waste Removal</h3>
              <p>We remove all solid and liquid waste from your grease trap efficiently</p>
            </div>
          </div>

          <div class="benefit-item">
            <div class="benefit-icon">✓</div>
            <div class="benefit-text">
              <h3>Reliable Service</h3>
              <p>Scheduled maintenance to keep your restaurant running smoothly</p>
            </div>
          </div>

          <div class="benefit-item">
            <div class="benefit-icon">✓</div>
            <div class="benefit-text">
              <h3>Code Compliance</h3>
              <p>Ensure your restaurant meets all local health and safety regulations</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Call to Action Section -->
    <section class="cta-section">
      <div class="container">
        <h2>Keep Your Restaurant Safe & Compliant</h2>
        <p>Don't let a full grease trap become a safety hazard or health code violation.</p>
        <router-link to="/contact" class="cta-button large">Contact Us Today</router-link>
        <p class="phone-cta">Call Now: <a href="tel:520-417-2105">(520) 417-2105</a></p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Grease Pumping Services | Sierra Vista, AZ | Sierra Vista Plumbing, Inc.',
  description: 'We have experience pumping out grease traps for restaurants in Sierra Vista, AZ. We can get rid of any solid and liquid waste caught in your grease trap.',
  image: '/images/services/grease-pumping.jpg',
  url: '/grease-pumping-services'
})
</script>

<style scoped>
.grease-pumping-page {
  width: 100%;
}

/* Hero Section */
.hero-section {
  position: relative;
  height: 600px;
  overflow: hidden;
}

.hero-image {
  position: relative;
  width: 100%;
  height: 100%;
}

.hero-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.7));
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-content {
  text-align: center;
  color: white;
  max-width: 900px;
  padding: 2rem;
}

.hero-content h1 {
  font-size: 3.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  line-height: 1.2;
}

.hero-content h2 {
  font-size: 1.5rem;
  font-weight: 400;
  margin-bottom: 2rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

/* Introduction Section */
.intro-section {
  padding: 5rem 2rem;
  background: #f8f9fa;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

.intro-content {
  text-align: center;
  max-width: 900px;
  margin: 0 auto;
}

.lead {
  font-size: 1.25rem;
  line-height: 1.8;
  color: #333;
  margin-bottom: 2rem;
}

.cta-text {
  font-size: 1.1rem;
  color: #a90e18;
  font-weight: 600;
}

/* Importance Section */
.importance-section {
  padding: 5rem 2rem;
  background: white;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-header h2 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1rem;
}

.section-header p {
  font-size: 1.2rem;
  color: #666;
  max-width: 800px;
  margin: 0 auto;
}

.reasons-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2.5rem;
  margin-top: 3rem;
}

.reason-card {
  text-align: center;
  padding: 2.5rem 2rem;
  background: #f8f9fa;
  border-radius: 12px;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.reason-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 8px 24px rgba(169, 14, 24, 0.15);
}

.reason-icon {
  font-size: 4rem;
  margin-bottom: 1.5rem;
}

.reason-card h3 {
  color: #a90e18;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.reason-card p {
  color: #666;
  font-size: 1.05rem;
  line-height: 1.6;
}

/* Benefits Section */
.benefits-section {
  padding: 5rem 2rem;
  background: linear-gradient(135deg, #f8f9fa, #e9ecef);
}

.benefits-section h2 {
  text-align: center;
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 3rem;
}

.benefits-list {
  max-width: 900px;
  margin: 0 auto;
}

.benefit-item {
  display: flex;
  align-items: flex-start;
  margin-bottom: 2.5rem;
  padding: 2rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease;
}

.benefit-item:hover {
  transform: translateX(8px);
}

.benefit-icon {
  font-size: 2rem;
  color: #a90e18;
  font-weight: bold;
  margin-right: 1.5rem;
  flex-shrink: 0;
}

.benefit-text h3 {
  color: #333;
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
}

.benefit-text p {
  color: #666;
  font-size: 1.05rem;
  line-height: 1.6;
}

/* CTA Section */
.cta-section {
  background: linear-gradient(135deg, #a90e18, #8a0b13);
  color: white;
  padding: 5rem 2rem;
  text-align: center;
}

.cta-section h2 {
  font-size: 2.8rem;
  margin-bottom: 1rem;
}

.cta-section p {
  font-size: 1.2rem;
  margin-bottom: 2.5rem;
}

.cta-button {
  display: inline-block;
  background: #a90e18;
  color: white;
  padding: 1rem 2.5rem;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.cta-button:hover {
  background: #8a0b13;
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

.cta-button.large {
  background: white;
  color: #a90e18;
  padding: 1.3rem 3.5rem;
  font-size: 1.3rem;
}

.cta-button.large:hover {
  background: #f8f9fa;
  color: #8a0b13;
}

.phone-cta {
  margin-top: 2rem;
  font-size: 1.3rem;
}

.phone-cta a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  border-bottom: 2px solid white;
  transition: border-color 0.3s ease;
}

.phone-cta a:hover {
  border-bottom-color: #f8f9fa;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-section {
    height: 450px;
  }

  .hero-content h1 {
    font-size: 2.2rem;
  }

  .hero-content h2 {
    font-size: 1.2rem;
  }

  .section-header h2,
  .benefits-section h2,
  .cta-section h2 {
    font-size: 2rem;
  }

  .reasons-grid {
    grid-template-columns: 1fr;
  }

  .benefit-item {
    flex-direction: column;
    text-align: center;
  }

  .benefit-icon {
    margin-right: 0;
    margin-bottom: 1rem;
  }
}

@media (max-width: 480px) {
  .hero-content h1 {
    font-size: 1.8rem;
  }

  .intro-section,
  .importance-section,
  .benefits-section,
  .cta-section {
    padding: 3rem 1.5rem;
  }
}
</style>
