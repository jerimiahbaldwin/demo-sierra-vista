<template>
  <!-- ⚠️ PAGE CLAIMED - Do not modify - Currently being developed -->
  <div class="heating-maintenance-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <div class="container">
          <h1 class="hero-title">Keep Your Heating System in Tip-Top Shape</h1>
          <p class="hero-subtitle">Arrange for heating maintenance services in Sierra Vista, AZ</p>
          <div class="hero-buttons">
            <a href="/contact" class="btn btn-primary">Schedule Maintenance</a>
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
            <h2>Regular Maintenance Keeps Your Heater Running</h2>
            <p>From tire rotations to oil changes, many people perform regular maintenance on their cars to keep them on the road. The same logic applies to heaters. Regular heating maintenance can keep your heat pump or furnace working year after year.</p>
            <p>Sierra Vista Plumbing, Inc. can provide heating maintenance services at a time that's convenient for you. Our heating contractor will go to your home or office in Sierra Vista, AZ and give your heating system a thorough tuneup.</p>
            <p><strong>Arrange for a heating maintenance plan today to keep your heater as efficient as possible.</strong></p>
          </div>
          <div class="content-image">
            <img src="/download/files/2019/10/bigstock-Close-Up-Of-Air-Conditioning-R-302758960.jpg"
              alt="Heating maintenance technician inspecting system" />
          </div>
        </div>
      </div>
    </section>

    <!-- Maintenance Services Section -->
    <section class="services-section">
      <div class="container">
        <h2>What Goes Into Heating Maintenance?</h2>
        <p class="section-intro">When you get heating maintenance services from Sierra Vista Plumbing, our HVAC contractor will give your heater a thorough examination. We'll look for problems and clean your system so it is more efficient and lasts longer.</p>

        <div class="services-grid">
          <div class="service-card">
            <div class="service-icon">🔥</div>
            <h3>Burner Inspection</h3>
            <p>Inspecting and cleaning the burners for optimal performance</p>
          </div>
          <div class="service-card">
            <div class="service-icon">♨️</div>
            <h3>Heat Exchangers</h3>
            <p>Inspecting the heat exchangers for safety and efficiency</p>
          </div>
          <div class="service-card">
            <div class="service-icon">🔧</div>
            <h3>Filter Check</h3>
            <p>Checking and replacing filters for better air quality</p>
          </div>
          <div class="service-card">
            <div class="service-icon">⚙️</div>
            <h3>Lubrication</h3>
            <p>Lubricating any moving parts to reduce wear</p>
          </div>
          <div class="service-card">
            <div class="service-icon">📊</div>
            <h3>Gas Pressure</h3>
            <p>Checking gas pressure for proper operation</p>
          </div>
          <div class="service-card">
            <div class="service-icon">🌀</div>
            <h3>Blower Inspection</h3>
            <p>Inspecting the blower for optimal air flow</p>
          </div>
          <div class="service-card">
            <div class="service-icon">💧</div>
            <h3>Condensate Check</h3>
            <p>Inspecting condensate drains and lines</p>
          </div>
          <div class="service-card">
            <div class="service-icon">✅</div>
            <h3>System Testing</h3>
            <p>Complete system testing and performance verification</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Benefits Section -->
    <section class="benefits-section">
      <div class="container">
        <h2>Benefits of Regular Heating Maintenance</h2>
        <div class="benefits-grid">
          <div class="benefit-card">
            <div class="benefit-number">1</div>
            <h3>Avoid Breakdowns</h3>
            <p>By catching problems early, you can avoid having your heater break down on a cold day.</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-number">2</div>
            <h3>Save Money</h3>
            <p>You'll save money when you don't have to schedule an emergency HVAC repair.</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-number">3</div>
            <h3>Improve Efficiency</h3>
            <p>A well-maintained system runs more efficiently, lowering your energy bills.</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-number">4</div>
            <h3>Extend Lifespan</h3>
            <p>Regular maintenance helps your heating system last longer and perform better.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="container">
        <h2>Ready to Schedule Your Maintenance?</h2>
        <p>Learn more about our maintenance plans today by calling 520-417-2105</p>
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
  title: 'Heating Maintenance | Sierra Vista, AZ | Sierra Vista Plumbing, Inc.',
  description: 'Regular heating maintenance can keep your heat pump or furnace working year after year. Sierra Vista Plumbing, Inc. can provide heating maintenance services.',
  image: '/download/files/2019/10/bigstock-Close-Up-Of-Air-Conditioning-R-302758960.jpg',
  url: '/heating-maintenance'
})
</script>

<style scoped>
.heating-maintenance-page {
  width: 100%;
}

/* Hero Section */
.hero-section {
  position: relative;
  height: 500px;
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  background-image: url('/download/files/2019/10/bigstock-Close-Up-Of-Air-Conditioning-R-302758960.jpg');
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

/* Services Section */
.services-section {
  padding: 5rem 0;
  background: #f8f9fa;
}

.services-section h2 {
  font-size: 2.5rem;
  color: #1a1a2e;
  margin-bottom: 1rem;
  text-align: center;
}

.section-intro {
  font-size: 1.125rem;
  color: #555;
  text-align: center;
  max-width: 800px;
  margin: 0 auto 3rem;
  line-height: 1.8;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.service-card {
  background: white;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.service-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
}

.service-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.service-card h3 {
  font-size: 1.25rem;
  color: #1a1a2e;
  margin-bottom: 0.75rem;
}

.service-card p {
  color: #666;
  line-height: 1.6;
}

/* Benefits Section */
.benefits-section {
  padding: 5rem 0;
  background: white;
}

.benefits-section h2 {
  font-size: 2.5rem;
  color: #a90e18;
  margin-bottom: 3rem;
  text-align: center;
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.benefit-card {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  text-align: center;
  position: relative;
  border-top: 4px solid #a90e18;
}

.benefit-number {
  position: absolute;
  top: -20px;
  left: 50%;
  transform: translateX(-50%);
  width: 45px;
  height: 45px;
  background: #a90e18;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
  box-shadow: 0 4px 6px rgba(169, 14, 24, 0.3);
}

.benefit-card h3 {
  font-size: 1.5rem;
  color: #1a1a2e;
  margin-bottom: 1rem;
  margin-top: 1rem;
}

.benefit-card p {
  color: #555;
  line-height: 1.6;
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
  opacity: 0.9;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Emergency Banner */
.emergency-banner {
  background: #1a1a2e;
  color: white;
  padding: 2rem 0;
  text-align: center;
}

.emergency-content h3 {
  font-size: 1.75rem;
  margin-bottom: 0.5rem;
}

.emergency-content p {
  margin: 0.25rem 0;
  font-size: 1.125rem;
  opacity: 0.9;
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
  background: #a90e18;
  color: white;
}

.btn-primary:hover {
  background: #8a0b14;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
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
  padding: 1rem 2.5rem;
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
    font-size: 1.25rem;
  }

  .content-grid {
    grid-template-columns: 1fr;
  }

  .content-text h2,
  .services-section h2,
  .benefits-section h2,
  .cta-section h2 {
    font-size: 2rem;
  }

  .services-grid,
  .benefits-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .hero-section {
    height: 400px;
  }

  .hero-title {
    font-size: 1.75rem;
  }

  .hero-subtitle {
    font-size: 1.125rem;
  }

  .hero-buttons {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }
}
</style>
