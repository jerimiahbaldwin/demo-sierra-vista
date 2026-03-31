<template>
  <div class="ac-installation-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <div class="container">
          <h1 class="hero-title">Arrange for an Air Conditioning Installation in Sierra Vista, AZ</h1>
          <p class="hero-subtitle">Stay Cool This Summer</p>
          <div class="hero-buttons">
            <a href="/contact" class="btn btn-primary">Schedule Installation</a>
            <a href="tel:520-417-2105" class="btn btn-secondary">Call: (520) 417-2105</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Main Content Section -->
    <section class="content-section">
      <div class="container">
        <div class="content-grid">
          <div class="content-text">
            <h2>Professional AC Installation Services</h2>
            <p>Beat the heat with an air conditioning installation from Sierra Vista Plumbing, Inc. We'll set up your 
              new air conditioning system right away. Don't sweat through another day. We'll perform the installation 
              you need swiftly and effectively.</p>
            <p><strong>Call 520-417-2105 now to schedule an air conditioning installation in Sierra Vista, AZ.</strong></p>
          </div>
          <div class="content-image">
            <img src="/download/wp-content/uploads/b2b/stock/v2/bigstock/air-conditioner-on-backyard-31978166.jpg"
              alt="Air conditioner installation on backyard" />
          </div>
        </div>
      </div>
    </section>

    <!-- Benefits Section -->
    <section class="benefits-section">
      <div class="container">
        <h2>What Are the Benefits of Getting a New Air Conditioner?</h2>
        <p class="section-intro">Investing in a new air conditioning system provides numerous advantages for your home and family.</p>

        <div class="benefits-grid">
          <div class="benefit-card">
            <div class="benefit-icon">❄️</div>
            <h3>Comfortable Environment</h3>
            <p>Enjoy a more comfortable environment throughout your entire home, even during the hottest summer days.</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">🏠</div>
            <h3>Temperature Control</h3>
            <p>Keep your belongings at a controlled temperature, protecting furniture, electronics, and valuables from heat damage.</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">💰</div>
            <h3>Energy Savings</h3>
            <p>Save money with a more efficient system that reduces your energy bills while keeping you cool.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Installation Process Section -->
    <section class="process-section">
      <div class="container">
        <h2>Plan Your AC Installation Without a Hassle</h2>
        <div class="process-content">
          <div class="process-image">
            <img src="/download/wp-content/uploads/b2b/stock/v2/bigstock/air-conditioner-on-backyard-31978166.jpg"
              alt="Professional AC installation setup" />
          </div>
          <div class="process-text">
            <p>Whether you're constructing a new home or replacing your old air conditioner, you can count on us to 
              take care of your AC installation. Investing in your AC system pays off in the long run.</p>
            <p>With a new and more efficient air conditioning unit, you can save money on repairs and maintenance. 
              Our experienced technicians ensure proper installation for optimal performance and longevity.</p>
            <div class="process-cta">
              <p><strong>Contact us today to request an AC installation in Sierra Vista, AZ.</strong></p>
              <a href="/contact" class="btn btn-primary btn-lg">Get Started</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Why Choose Us Section -->
    <section class="why-choose-section">
      <div class="container">
        <h2>Why Choose Sierra Vista Plumbing for AC Installation?</h2>
        <div class="features-grid">
          <div class="feature-item">
            <div class="feature-number">01</div>
            <h3>Expert Technicians</h3>
            <p>Our skilled HVAC contractors have years of experience in AC installation</p>
          </div>
          <div class="feature-item">
            <div class="feature-number">02</div>
            <h3>Quality Equipment</h3>
            <p>We install only high-quality, energy-efficient air conditioning systems</p>
          </div>
          <div class="feature-item">
            <div class="feature-number">03</div>
            <h3>Fast Service</h3>
            <p>We complete your installation swiftly and effectively to get you cooling quickly</p>
          </div>
          <div class="feature-item">
            <div class="feature-number">04</div>
            <h3>Fair Pricing</h3>
            <p>Competitive rates with transparent pricing and no hidden fees</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="container">
        <h2>Ready for a New Air Conditioning System?</h2>
        <p>Call 520-417-2105 today for professional AC installation in Sierra Vista, AZ</p>
        <div class="cta-buttons">
          <a href="/contact" class="btn btn-primary btn-lg">Contact Us</a>
          <a href="tel:520-417-2105" class="btn btn-secondary btn-lg">Call Now</a>
        </div>
      </div>
    </section>

    <!-- Emergency Service Banner -->
    <section class="emergency-banner">
      <div class="container">
        <div class="emergency-content">
          <h3>24/7 Emergency Service Available</h3>
          <p>Family Owned and Operated</p>
          <p>Second Office: 520-559-2534</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Air Conditioning Installation Services | Sierra Vista, AZ | Sierra Vista Plumbing, Inc.',
  description: 'Beat the heat with an air conditioning installation from Sierra Vista Plumbing, Inc. We\'ll set up your new air conditioning system right away.',
  image: '/download/wp-content/uploads/b2b/stock/v2/bigstock/air-conditioner-on-backyard-31978166.jpg',
  url: '/air-conditioning-installation'
})
</script>

<style scoped>
.ac-installation-page {
  width: 100%;
}

/* Hero Section */
.hero-section {
  position: relative;
  height: 500px;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  background-image: url('/download/wp-content/uploads/b2b/stock/v2/bigstock/air-conditioner-on-backyard-31978166.jpg');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  text-align: center;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(26, 26, 46, 0.75);
}

.hero-content {
  position: relative;
  z-index: 1;
}

.hero-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  font-weight: 300;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Container */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* Buttons */
.btn {
  display: inline-block;
  padding: 0.875rem 2rem;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.btn-primary {
  background-color: #a90e18;
  color: white;
  border-color: #a90e18;
}

.btn-primary:hover {
  background-color: #8a0b13;
  border-color: #8a0b13;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(169, 14, 24, 0.3);
}

.btn-secondary {
  background-color: transparent;
  color: white;
  border-color: white;
}

.btn-secondary:hover {
  background-color: white;
  color: #a90e18;
}

.btn-lg {
  padding: 1.125rem 2.5rem;
  font-size: 1.125rem;
}

/* Content Section */
.content-section {
  padding: 5rem 0;
  background: white;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.content-text h2 {
  font-size: 2.5rem;
  color: #a90e18;
  margin-bottom: 1.5rem;
}

.content-text p {
  font-size: 1.125rem;
  line-height: 1.8;
  margin-bottom: 1rem;
  color: #333;
}

.content-image img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

/* Benefits Section */
.benefits-section {
  padding: 5rem 0;
  background: #f8f9fa;
}

.benefits-section h2 {
  text-align: center;
  font-size: 2.5rem;
  color: #1a1a2e;
  margin-bottom: 1rem;
}

.section-intro {
  text-align: center;
  font-size: 1.25rem;
  color: #666;
  margin-bottom: 3rem;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.benefit-card {
  background: white;
  padding: 2.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.benefit-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.benefit-icon {
  font-size: 3.5rem;
  margin-bottom: 1.5rem;
}

.benefit-card h3 {
  font-size: 1.5rem;
  color: #a90e18;
  margin-bottom: 1rem;
}

.benefit-card p {
  font-size: 1rem;
  color: #666;
  line-height: 1.6;
}

/* Process Section */
.process-section {
  padding: 5rem 0;
  background: white;
}

.process-section h2 {
  text-align: center;
  font-size: 2.5rem;
  color: #a90e18;
  margin-bottom: 3rem;
}

.process-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.process-image img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.process-text p {
  font-size: 1.125rem;
  line-height: 1.8;
  color: #333;
  margin-bottom: 1.5rem;
}

.process-cta {
  margin-top: 2rem;
  padding: 2rem;
  background: #f8f9fa;
  border-radius: 8px;
  text-align: center;
}

.process-cta p {
  margin-bottom: 1.5rem;
  font-size: 1.25rem;
  color: #1a1a2e;
}

/* Why Choose Section */
.why-choose-section {
  padding: 5rem 0;
  background: #1a1a2e;
  color: white;
}

.why-choose-section h2 {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 3rem;
  color: white;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.feature-item {
  text-align: center;
  padding: 2rem;
}

.feature-number {
  font-size: 3rem;
  font-weight: 700;
  color: #a90e18;
  margin-bottom: 1rem;
  opacity: 0.3;
}

.feature-item h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: white;
}

.feature-item p {
  font-size: 1rem;
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
}

/* CTA Section */
.cta-section {
  padding: 5rem 0;
  background: linear-gradient(135deg, #a90e18 0%, #8a0b13 100%);
  color: white;
  text-align: center;
}

.cta-section h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-weight: 700;
}

.cta-section p {
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

.cta-section .btn-primary {
  background-color: white;
  color: #a90e18;
  border-color: white;
}

.cta-section .btn-primary:hover {
  background-color: #f8f9fa;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.3);
}

.cta-section .btn-secondary {
  background-color: transparent;
  color: white;
  border-color: white;
}

.cta-section .btn-secondary:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

/* Emergency Banner */
.emergency-banner {
  background: #1a1a2e;
  color: white;
  padding: 2rem 0;
}

.emergency-content {
  text-align: center;
}

.emergency-content h3 {
  font-size: 1.75rem;
  margin-bottom: 0.5rem;
  color: #a90e18;
}

.emergency-content p {
  font-size: 1.125rem;
  margin: 0.25rem 0;
  opacity: 0.9;
}

/* Responsive Design */
@media (max-width: 968px) {
  .hero-title {
    font-size: 2.25rem;
  }

  .hero-subtitle {
    font-size: 1.25rem;
  }

  .content-grid,
  .process-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .benefits-grid,
  .features-grid {
    grid-template-columns: 1fr;
  }

  .content-text h2,
  .benefits-section h2,
  .process-section h2,
  .why-choose-section h2,
  .cta-section h2 {
    font-size: 2rem;
  }
}

@media (max-width: 768px) {
  .hero-section {
    height: 400px;
  }

  .hero-title {
    font-size: 1.75rem;
  }

  .hero-subtitle {
    font-size: 1.125rem;
  }

  .content-section,
  .benefits-section,
  .process-section,
  .why-choose-section,
  .cta-section {
    padding: 3rem 0;
  }

  .btn {
    padding: 0.75rem 1.5rem;
  }

  .btn-lg {
    padding: 0.875rem 2rem;
    font-size: 1rem;
  }
}
</style>
