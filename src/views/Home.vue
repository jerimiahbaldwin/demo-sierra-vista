<template>
  <div>
    <!-- Hero Section -->
    <section class="hero" id="home">
      <div class="hero-slide active" :style="{ backgroundImage: `url(/download/files/2019/03/1551447792973_bigstock_close_up_view_on_hvac_units_h_229402624.jpg)` }">
        <div class="hero-overlay"></div>
        <div class="container">
          <div class="hero-content">
            <h1 class="hero-title">Professional HVAC & Plumbing Services</h1>
            <p class="hero-subtitle">Schedule heating and cooling services in Sierra Vista, AZ</p>
            <router-link to="/contact" class="btn btn-primary">Get A Quote</router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="stats-section">
      <div class="container">
        <div class="stats-grid">
          <div class="stat-item">
            <div class="stat-number">30+</div>
            <div class="stat-label">Years in Business</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">5000+</div>
            <div class="stat-label">Projects Completed</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">10K+</div>
            <div class="stat-label">Satisfied Customers</div>
          </div>
          <div class="stat-item">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Emergency Service</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section class="services-section" id="services">
      <div class="container">
        <div class="section-header">
          <h2>Our Services</h2>
          <p>Comprehensive HVAC and plumbing solutions for your home and business</p>
        </div>
        <div class="services-grid">
          <div class="service-card" v-for="service in services" :key="service.title">
            <div class="service-icon">
              <img :src="service.icon" :alt="service.title" />
            </div>
            <h3>{{ service.title }}</h3>
            <p>{{ service.description }}</p>
            <router-link :to="service.link" class="service-link">Learn More →</router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- About Section -->
    <section class="about-section" id="about">
      <div class="container">
        <div class="about-grid">
          <div class="about-image">
            <img src="/download/files/2019/02/1551296033801_10860843_374375896067761_499326307120328047_o.jpg" alt="Sierra Vista Plumbing Team" />
          </div>
          <div class="about-content">
            <h2>Experience, Quality and Service You Can Trust</h2>
            <p>When you need a reliable plumber or HVAC service provider, look no further than Sierra Vista Plumbing. With over 30 years of experience in the plumbing and HVAC industries, we strive to provide superior residential and commercial services to the residents of Sierra Vista, AZ.</p>
            <p>We provide quality heating, cooling and plumbing services for homes, office buildings and other commercial spaces. Whether your heat is not working properly or your drains are clogged, you can make us your on-call plumber and HVAC service provider.</p>
            <ul class="feature-list">
              <li>✓ 30+ Years of Experience</li>
              <li>✓ Licensed & Insured</li>
              <li>✓ 24/7 Emergency Service</li>
              <li>✓ Family Owned & Operated</li>
              <li>✓ Upfront Pricing</li>
              <li>✓ 100% Satisfaction Guaranteed</li>
            </ul>
            <router-link to="/contact" class="btn btn-primary">Contact Us Today</router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section" :style="{ backgroundImage: `url(/download/files/2019/02/1551296179350_bigstock_124843106.jpg)` }">
      <div class="cta-overlay"></div>
      <div class="container">
        <div class="cta-content">
          <h2>Need Emergency Service?</h2>
          <p>We're available 24/7 for your plumbing and HVAC emergencies</p>
          <a href="tel:5204172105" class="btn btn-white">Call Now: (520) 417-2105</a>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="contact-section" id="contact">
      <div class="container">
        <div class="section-header">
          <h2>Get In Touch</h2>
          <p>Contact us today for a free estimate</p>
        </div>
        <div class="contact-grid">
          <div class="contact-info">
            <div class="contact-item">
              <div class="contact-icon">📍</div>
              <div class="contact-details">
                <h4>Address</h4>
                <p>4847 South Hwy 92<br>Sierra Vista, AZ 85650</p>
              </div>
            </div>
            <div class="contact-item">
              <div class="contact-icon">📞</div>
              <div class="contact-details">
                <h4>Phone</h4>
                <p><a href="tel:5204172105">(520) 417-2105</a></p>
                <p><a href="tel:5205592534">(520) 559-2534</a></p>
              </div>
            </div>
            <div class="contact-item">
              <div class="contact-icon">⏰</div>
              <div class="contact-details">
                <h4>Hours</h4>
                <p>Mon - Fri: 8:00 AM - 5:00 PM</p>
                <p>24/7 Emergency Service Available</p>
              </div>
            </div>
          </div>
          <div class="contact-form">
            <form @submit.prevent="handleSubmit">
              <div class="form-group">
                <input type="text" placeholder="Your Name" v-model="form.name" required />
              </div>
              <div class="form-group">
                <input type="email" placeholder="Your Email" v-model="form.email" required />
              </div>
              <div class="form-group">
                <input type="tel" placeholder="Your Phone" v-model="form.phone" required />
              </div>
              <div class="form-group">
                <textarea placeholder="Message" v-model="form.message" rows="5" required></textarea>
              </div>
              <button type="submit" class="btn btn-primary btn-block">Send Message</button>
            </form>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useSeo, getOrganizationSchema } from '../composables/useSeo'

useSeo({
  title: 'Plumber | Sierra Vista, AZ | Sierra Vista Plumbing, Inc.',
  description: 'Sierra Vista Plumbing, Inc. is a plumber in Sierra Vista, AZ. Our services include HVAC services, plumbing services and so much more! Give us a call today! (520) 417-2105',
  image: '/download/files/2019/03/1551447792973_bigstock_close_up_view_on_hvac_units_h_229402624.jpg',
  url: '/',
  schema: getOrganizationSchema()
})

const form = ref({
  name: '',
  email: '',
  phone: '',
  message: ''
})

const services = [
  {
    title: 'Plumbing Services',
    icon: '/download/files/2019/02/plumbing.png',
    description: 'Expert plumbing repairs, installations, and maintenance for residential and commercial properties.',
    link: '/plumbing-services'
  },
  {
    title: 'Heating Services',
    icon: '/download/files/2019/02/thermometer_4_.png',
    description: 'Complete heating system installation, repair, and maintenance to keep you warm all winter.',
    link: '/heating-services'
  },
  {
    title: 'Air Conditioning',
    icon: '/download/files/2019/02/air_conditioner_1_.png',
    description: 'Professional AC installation, repair, and maintenance for optimal cooling performance.',
    link: '/air-conditioning-services'
  },
  {
    title: 'Duct Cleaning',
    icon: '/download/files/2019/02/air_conditioner_1_.png',
    description: 'Thorough duct cleaning services to improve air quality and system efficiency.',
    link: '/duct-cleaning-services'
  },
  {
    title: 'Water Heaters',
    icon: '/download/files/2019/02/thermometer_4_.png',
    description: 'Water heater repair, replacement, and installation services for reliable hot water.',
    link: '/heating-services'
  },
  {
    title: 'Emergency Service',
    icon: '/download/files/2019/02/plumbing.png',
    description: '24/7 emergency plumbing and HVAC services when you need us most.',
    link: '/contact'
  }
]

const handleSubmit = () => {
  alert('Thank you for your message! We will contact you shortly.')
  form.value = { name: '', email: '', phone: '', message: '' }
}
</script>

<style scoped>
/* Hero Section */
.hero {
  position: relative;
  height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  color: var(--white);
}

.hero-title {
  font-size: 3.5rem;
  font-weight: bold;
  margin-bottom: 1rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
}

/* Stats Section */
.stats-section {
  background: var(--primary-color);
  color: var(--white);
  padding: 3rem 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  text-align: center;
}

.stat-number {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 1rem;
  opacity: 0.9;
}

/* Services Section */
.services-section {
  padding: 5rem 0;
  background: var(--light-bg);
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
}

.section-header h2 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  color: var(--secondary-color);
}

.section-header p {
  font-size: 1.125rem;
  color: #666;
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.service-card {
  background: var(--white);
  padding: 2rem;
  border-radius: 8px;
  box-shadow: var(--shadow);
  text-align: center;
  transition: transform 0.3s;
}

.service-card:hover {
  transform: translateY(-5px);
}

.service-icon {
  margin-bottom: 1.5rem;
}

.service-icon img {
  width: 80px;
  height: 80px;
  object-fit: contain;
}

.service-card h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: var(--secondary-color);
}

.service-card p {
  color: #666;
  margin-bottom: 1rem;
}

.service-link {
  color: var(--primary-color);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.service-link:hover {
  color: #8a0c14;
}

/* About Section */
.about-section {
  padding: 5rem 0;
}

.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.about-image img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: var(--shadow);
}

.about-content h2 {
  font-size: 2.5rem;
  margin-bottom: 1.5rem;
  color: var(--secondary-color);
}

.about-content p {
  margin-bottom: 1rem;
  color: #666;
}

.feature-list {
  list-style: none;
  margin: 2rem 0;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 0.75rem;
}

.feature-list li {
  color: var(--text-color);
  font-weight: 500;
}

/* CTA Section */
.cta-section {
  position: relative;
  padding: 5rem 0;
  background-size: cover;
  background-position: center;
  text-align: center;
}

.cta-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(169, 14, 24, 0.9);
}

.cta-content {
  position: relative;
  z-index: 2;
  color: var(--white);
}

.cta-content h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.cta-content p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
}

/* Contact Section */
.contact-section {
  padding: 5rem 0;
  background: var(--light-bg);
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
}

.contact-item {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.contact-icon {
  font-size: 2rem;
  color: var(--primary-color);
}

.contact-details h4 {
  margin-bottom: 0.5rem;
  color: var(--secondary-color);
}

.contact-details p {
  color: #666;
}

.contact-details a {
  color: var(--primary-color);
  text-decoration: none;
}

.contact-form {
  background: var(--white);
  padding: 2rem;
  border-radius: 8px;
  box-shadow: var(--shadow);
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-family: inherit;
  font-size: 1rem;
}

.form-group input:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--primary-color);
}

/* Buttons */
.btn {
  display: inline-block;
  padding: 1rem 2rem;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  font-weight: 600;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-primary {
  background: var(--primary-color);
  color: var(--white);
}

.btn-primary:hover {
  background: #8a0c14;
}

.btn-white {
  background: var(--white);
  color: var(--primary-color);
}

.btn-white:hover {
  background: var(--light-bg);
}

.btn-block {
  width: 100%;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }

  .hero-subtitle {
    font-size: 1rem;
  }

  .about-grid,
  .contact-grid {
    grid-template-columns: 1fr;
  }

  .feature-list {
    grid-template-columns: 1fr;
  }
}
</style>
