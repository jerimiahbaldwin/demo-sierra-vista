<template>
  <!-- ⚠️ PAGE CLAIMED - Do not modify - Currently being developed -->
  <div class="heating-installation-page">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <div class="container">
          <h1 class="hero-title">Upgrade Your Outdated Heating System</h1>
          <p class="hero-subtitle">Get a new heating installation in Sierra Vista, AZ</p>
          <div class="hero-buttons">
            <a href="/contact" class="btn btn-primary">Get Free Estimate</a>
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
            <h2>Professional Heating Installation Services</h2>
            <p>Is your heater more than a decade old? They might last for years, but technology improves quickly.
              A heating replacement will be more efficient and can give you greater control over the heating in your
              home or office. Reach out to Sierra Vista Plumbing, Inc. when you're ready for a new heating installation.
            </p>
            <p>We've been providing heating replacement services In Sierra Vista, Arizona for over 10 years. We'll help
              you find a new heater that will provide the temperature control you need while lowering your utility bill.
            </p>
            <p><strong>Speak with our HVAC contractor today to learn more about your heating options.</strong></p>
          </div>
          <div class="content-image">
            <img src="/download/files/2019/10/bigstock-House-Heating-Unit-Repair-By-P-321026833.jpg"
              alt="Professional heating system installation" />
          </div>
        </div>
      </div>
    </section>

    <!-- Benefits Section -->
    <section class="benefits-section">
      <div class="container">
        <h2>Benefits of a New Heating System</h2>
        <div class="benefits-grid">
          <div class="benefit-card">
            <div class="benefit-icon">💰</div>
            <h3>Lower Energy Bills</h3>
            <p>Modern heating systems are far more energy-efficient than older models, helping you save on monthly
              utility costs</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">🌡️</div>
            <h3>Better Temperature Control</h3>
            <p>New systems provide more precise temperature control and consistent heating throughout your home</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">🔧</div>
            <h3>Fewer Repairs</h3>
            <p>A new heating system means fewer breakdowns and repair calls, saving you time and money</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">🌱</div>
            <h3>Eco-Friendly</h3>
            <p>Modern heaters are designed to be more environmentally friendly with reduced emissions</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">😌</div>
            <h3>Peace of Mind</h3>
            <p>Enjoy the comfort of knowing your heating system is reliable and backed by a warranty</p>
          </div>
          <div class="benefit-card">
            <div class="benefit-icon">📱</div>
            <h3>Smart Technology</h3>
            <p>Many new systems include smart thermostats for remote control and programmable schedules</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Installation Process Section -->
    <section class="process-section">
      <div class="container">
        <h2>Our Installation Process</h2>
        <div class="process-steps">
          <div class="process-step">
            <div class="step-number">1</div>
            <h3>Consultation & Assessment</h3>
            <p>We'll assess your current system and home heating needs to recommend the best options for your budget and
              requirements</p>
          </div>
          <div class="process-step">
            <div class="step-number">2</div>
            <h3>System Selection</h3>
            <p>We'll help you choose a heating system that suits your needs, explaining the benefits of different models
              and brands</p>
          </div>
          <div class="process-step">
            <div class="step-number">3</div>
            <h3>Professional Installation</h3>
            <p>Our experienced technicians will complete the installation quickly and efficiently, ensuring everything
              works perfectly</p>
          </div>
          <div class="process-step">
            <div class="step-number">4</div>
            <h3>Testing & Training</h3>
            <p>We'll test your new system thoroughly and show you how to operate it for optimal performance and comfort
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Support Section -->
    <section class="support-section">
      <div class="container">
        <div class="support-content">
          <h2>Not Sure What Heater to Install?</h2>
          <p>If your old heater has broken down or you're looking to improve the functionality of your system, give our
            heating contractor a call. We'll explain your options and help you find a heater that suits your needs while
            matching your budget. Once you make your choice, we'll complete the heating installation as quickly as
            possible.</p>
          <div class="support-stats">
            <div class="stat">
              <div class="stat-number">10+</div>
              <div class="stat-label">Years Experience</div>
            </div>
            <div class="stat">
              <div class="stat-number">24/7</div>
              <div class="stat-label">Emergency Service</div>
            </div>
            <div class="stat">
              <div class="stat-number">100%</div>
              <div class="stat-label">Satisfaction</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="container">
        <h2>Ready for a More Efficient Heating System?</h2>
        <p>Call us at 520-417-2105 today for HVAC repair and replacement services in the Sierra Vista, AZ area</p>
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
  title: 'Heating Installation | Sierra Vista, AZ | Sierra Vista Plumbing, Inc.',
  description: 'We\'ve been providing heating replacement services In Sierra Vista, Arizona for over 10 years. Speak with an HVAC contractor today.',
  image: '/download/files/2019/10/bigstock-House-Heating-Unit-Repair-By-P-321026833.jpg',
  url: '/heating-installation'
})
</script>

<style scoped>
/* Hero Section */
.hero-section {
  position: relative;
  height: 500px;
  background: linear-gradient(135deg, rgba(169, 14, 24, 0.9), rgba(0, 0, 0, 0.7)),
    url('/download/files/2019/10/bigstock-House-Heating-Unit-Repair-By-P-321026833.jpg') center/cover;
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
  background: rgba(0, 0, 0, 0.3);
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 800px;
  padding: 2rem;
}

.hero-title {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 1rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* Buttons */
.btn {
  padding: 0.875rem 2rem;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  display: inline-block;
}

.btn-primary {
  background-color: #a90e18;
  color: white;
}

.btn-primary:hover {
  background-color: #8a0b14;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.btn-secondary {
  background-color: white;
  color: #a90e18;
  border: 2px solid white;
}

.btn-secondary:hover {
  background-color: transparent;
  color: white;
  transform: translateY(-2px);
}

.btn-lg {
  padding: 1rem 2.5rem;
  font-size: 1.125rem;
}

/* Content Section */
.content-section {
  padding: 4rem 0;
  background-color: #f9f9f9;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.content-text h2 {
  font-size: 2rem;
  color: #333;
  margin-bottom: 1.5rem;
}

.content-text p {
  font-size: 1.125rem;
  line-height: 1.8;
  color: #666;
  margin-bottom: 1rem;
}

.content-image img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* Benefits Section */
.benefits-section {
  padding: 4rem 0;
  background-color: white;
}

.benefits-section h2 {
  text-align: center;
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 3rem;
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.benefit-card {
  padding: 2rem;
  background-color: #f9f9f9;
  border-radius: 8px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.benefit-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.benefit-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.benefit-card h3 {
  font-size: 1.5rem;
  color: #a90e18;
  margin-bottom: 1rem;
}

.benefit-card p {
  color: #666;
  line-height: 1.6;
}

/* Process Section */
.process-section {
  padding: 4rem 0;
  background-color: #f9f9f9;
}

.process-section h2 {
  text-align: center;
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 3rem;
}

.process-steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.process-step {
  text-align: center;
  padding: 2rem;
}

.step-number {
  width: 60px;
  height: 60px;
  background-color: #a90e18;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.75rem;
  font-weight: bold;
  margin: 0 auto 1.5rem;
}

.process-step h3 {
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 1rem;
}

.process-step p {
  color: #666;
  line-height: 1.6;
}

/* Support Section */
.support-section {
  padding: 4rem 0;
  background-color: white;
}

.support-content h2 {
  text-align: center;
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1.5rem;
}

.support-content p {
  text-align: center;
  font-size: 1.125rem;
  line-height: 1.8;
  color: #666;
  max-width: 900px;
  margin: 0 auto 3rem;
}

.support-stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  max-width: 800px;
  margin: 0 auto;
}

.stat {
  text-align: center;
  padding: 2rem;
  background-color: #f9f9f9;
  border-radius: 8px;
}

.stat-number {
  font-size: 3rem;
  font-weight: bold;
  color: #a90e18;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 1.125rem;
  color: #666;
}

/* CTA Section */
.cta-section {
  padding: 4rem 0;
  background-color: #f9f9f9;
  text-align: center;
}

.cta-section h2 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1rem;
}

.cta-section p {
  font-size: 1.25rem;
  color: #666;
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
  background-color: #a90e18;
  color: white;
  padding: 2.5rem 0;
  text-align: center;
}

.emergency-content h3 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.emergency-content p {
  font-size: 1.125rem;
  margin: 0.25rem 0;
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
  }

  .benefits-grid,
  .process-steps {
    grid-template-columns: 1fr;
  }

  .hero-buttons,
  .cta-buttons {
    flex-direction: column;
  }

  .btn {
    width: 100%;
  }
}
</style>
