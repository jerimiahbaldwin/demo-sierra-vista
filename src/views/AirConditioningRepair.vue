<template>
  <!-- ⚠️ PAGE CLAIMED - Do not modify - Currently being developed -->
  <div class="air-conditioning-repair-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <div class="container">
          <h1 class="hero-title">Let us Know When You Need an Air Conditioning Repair</h1>
          <p class="hero-subtitle">Fix Your AC in Sierra Vista, AZ</p>
          <div class="hero-buttons">
            <a href="/contact" class="btn btn-primary">Schedule Service</a>
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
            <h2>Expert Air Conditioning Repair Services</h2>
            <p>If there's a problem with your air conditioning, don't put off air conditioning repair. Call Sierra Vista Plumbing, Inc. for the HVAC services you need. We'll determine what's wrong with your air conditioner so you can resolve the issue and relax in comfort.</p>
            <p><strong>Contact us now to request an air conditioning repair in Sierra Vista, AZ.</strong></p>
          </div>
          <div class="content-image">
            <img src="/download/wp-content/uploads/b2b/stock/v2/bigstock/Industrial-Air-Conditioning-Re-4776307.jpg"
              alt="Air conditioning repair technician working on AC unit" />
          </div>
        </div>
      </div>
    </section>

    <!-- Warning Signs Section -->
    <section class="warning-signs-section">
      <div class="container">
        <h2>Signs You Need AC Repair</h2>
        <p class="section-intro">Reach out to us if you're experiencing any of these common air conditioning problems:</p>

        <div class="warning-signs-grid">
          <div class="warning-card">
            <div class="warning-icon">💨</div>
            <h3>Poor Air Flow</h3>
            <p>Weak or insufficient air circulation throughout your home</p>
          </div>
          <div class="warning-card">
            <div class="warning-icon">❄️</div>
            <h3>Lack of Cool Air</h3>
            <p>Your AC is running but not producing cold air</p>
          </div>
          <div class="warning-card">
            <div class="warning-icon">🌡️</div>
            <h3>Thermostat Problems</h3>
            <p>Temperature control issues or inconsistent readings</p>
          </div>
          <div class="warning-card">
            <div class="warning-icon">💧</div>
            <h3>Moisture Seepage</h3>
            <p>Water leaking or unusual condensation around your unit</p>
          </div>
          <div class="warning-card">
            <div class="warning-icon">🔊</div>
            <h3>Strange Noises</h3>
            <p>Unusual sounds like grinding, squealing, or rattling</p>
          </div>
          <div class="warning-card">
            <div class="warning-icon">👃</div>
            <h3>Weird Smells</h3>
            <p>Musty or burning odors coming from your AC system</p>
          </div>
        </div>
      </div>
    </section>

    <!-- AC Maintenance Section -->
    <section class="maintenance-section">
      <div class="container">
        <div class="maintenance-content">
          <h2>We'll Cover All Your AC Maintenance Needs</h2>
          <p>Don't let HVAC problems sneak up on you. Approach them head-on with our exemplary AC maintenance service. We'll keep your air conditioning working all year long to make sure it never gets too hot in your home. We'll conduct a full system performance test and a leak test to make sure we cover all of our bases.</p>
          <div class="maintenance-highlight">
            <p><strong>Regular AC maintenance helps prevent costly repairs and extends the life of your system.</strong></p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="container">
        <h2>Need Air Conditioning Repair?</h2>
        <p>Call 520-417-2105 today for AC maintenance in Sierra Vista, AZ</p>
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
  title: 'Air Conditioning Repairs | Sierra Vista, AZ | Sierra Vista Plumbing, Inc.',
  description: 'If there\'s a problem with your air conditioning, don\'t put off air conditioning repair. Call Sierra Vista Plumbing, Inc. for the HVAC services you need in Sierra Vista, AZ.',
  image: '/download/wp-content/uploads/b2b/stock/v2/bigstock/Industrial-Air-Conditioning-Re-4776307.jpg',
  url: '/air-conditioning-repair'
})
</script>

<style scoped>
.air-conditioning-repair-page {
  width: 100%;
}

/* Hero Section */
.hero-section {
  position: relative;
  height: 500px;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  background-image: url('/download/wp-content/uploads/b2b/stock/v2/bigstock/Industrial-Air-Conditioning-Re-4776307.jpg');
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

/* Warning Signs Section */
.warning-signs-section {
  padding: 5rem 0;
  background: #f8f9fa;
}

.warning-signs-section h2 {
  font-size: 2.5rem;
  color: #1a1a2e;
  text-align: center;
  margin-bottom: 1rem;
}

.section-intro {
  text-align: center;
  font-size: 1.125rem;
  color: #666;
  max-width: 800px;
  margin: 0 auto 3rem;
}

.warning-signs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.warning-card {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.warning-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

.warning-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.warning-card h3 {
  font-size: 1.25rem;
  color: #a90e18;
  margin-bottom: 0.5rem;
}

.warning-card p {
  color: #666;
  line-height: 1.6;
}

/* Maintenance Section */
.maintenance-section {
  padding: 5rem 0;
  background: white;
}

.maintenance-content {
  max-width: 900px;
  margin: 0 auto;
  text-align: center;
}

.maintenance-content h2 {
  font-size: 2.5rem;
  color: #a90e18;
  margin-bottom: 1.5rem;
}

.maintenance-content p {
  font-size: 1.125rem;
  line-height: 1.8;
  color: #333;
  margin-bottom: 2rem;
}

.maintenance-highlight {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  border-left: 4px solid #a90e18;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
}

.maintenance-highlight p {
  margin: 0;
  font-size: 1.125rem;
  color: #333;
}

/* CTA Section */
.cta-section {
  padding: 5rem 0;
  background: linear-gradient(135deg, #a90e18 0%, #8a0b14 100%);
  color: white;
  text-align: center;
}

.cta-section h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.cta-section p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Emergency Banner */
.emergency-banner {
  padding: 3rem 0;
  background: #1a1a2e;
  color: white;
  text-align: center;
}

.emergency-content h3 {
  font-size: 1.8rem;
  margin-bottom: 0.5rem;
  color: #ffc107;
}

.emergency-content p {
  font-size: 1.125rem;
  margin: 0.25rem 0;
}

/* Buttons */
.btn {
  display: inline-block;
  padding: 0.875rem 2rem;
  font-size: 1rem;
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
  background: transparent;
  color: white;
  border: 2px solid white;
}

.btn-secondary:hover {
  background: white;
  color: #a90e18;
}

.btn-lg {
  padding: 1.125rem 2.5rem;
  font-size: 1.125rem;
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

  .content-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .content-text h2,
  .warning-signs-section h2,
  .maintenance-content h2,
  .cta-section h2 {
    font-size: 1.875rem;
  }

  .warning-signs-grid {
    grid-template-columns: 1fr;
  }

  .hero-buttons,
  .cta-buttons {
    flex-direction: column;
    align-items: center;
  }

  .btn {
    width: 100%;
    max-width: 300px;
  }
}
</style>
