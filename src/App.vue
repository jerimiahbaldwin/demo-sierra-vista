<template>
  <div id="app">
    <!-- Navigation Header -->
    <header class="site-header">
      <div class="container">
        <div class="header-content">
          <div class="logo">
            <router-link to="/">
              <img src="/download/files/2019/03/sierra_vista_new.png" alt="Sierra Vista Plumbing, Inc." />
            </router-link>
          </div>
          <nav class="main-nav">
            <router-link to="/">Home</router-link>

            <div class="nav-dropdown">
              <span class="nav-dropdown-toggle">Heating Services ▾</span>
              <div class="nav-dropdown-menu">
                <router-link to="/heating-services">Heating Services</router-link>
                <router-link to="/heating-installation">Heating Installation</router-link>
                <router-link to="/heating-repair">Heating Repair</router-link>
                <router-link to="/heating-maintenance">Heating Maintenance</router-link>
              </div>
            </div>

            <div class="nav-dropdown">
              <span class="nav-dropdown-toggle">Air Conditioning ▾</span>
              <div class="nav-dropdown-menu">
                <router-link to="/air-conditioning-services">Air Conditioning Services</router-link>
                <router-link to="/air-conditioning-installation">AC Installation</router-link>
                <router-link to="/air-conditioning-repair">AC Repair</router-link>
              </div>
            </div>

            <div class="nav-dropdown">
              <span class="nav-dropdown-toggle">Other Services ▾</span>
              <div class="nav-dropdown-menu">
                <router-link to="/plumbing-services">Plumbing Services</router-link>
                <router-link to="/duct-cleaning-services">Duct Cleaning</router-link>
                <router-link to="/dryer-vent-rotobrush-cleaning-services">Dryer Vent Cleaning</router-link>
                <router-link to="/grease-pumping-services">Grease Pumping</router-link>
              </div>
            </div>

            <router-link to="/gallery">Gallery</router-link>
            <router-link to="/reviews">Reviews</router-link>
            <router-link to="/faq">FAQ</router-link>
            <router-link to="/service-area">Service Area</router-link>
            <router-link to="/contact">Contact</router-link>
          </nav>
          <div class="header-contact">
            <div class="phone-number">
              <span class="label">Call Us Today!</span>
              <a href="tel:5204172105" class="phone">(520) 417-2105</a>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Content Area -->
    <main>
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="site-footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-col">
            <h4>About Us</h4>
            <p>Sierra Vista Plumbing, Inc. provides professional plumbing and HVAC services to Sierra Vista, AZ and
              surrounding areas.</p>
          </div>
          <div class="footer-col">
            <h4>Services</h4>
            <ul>
              <li><router-link to="/plumbing-services">Plumbing Services</router-link></li>
              <li><router-link to="/heating-services">Heating Services</router-link></li>
              <li><router-link to="/air-conditioning-services">Air Conditioning</router-link></li>
              <li><router-link to="/duct-cleaning-services">Duct Cleaning</router-link></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Contact</h4>
            <p>4847 South Hwy 92<br>Sierra Vista, AZ 85650</p>
            <p><a href="tel:5204172105">(520) 417-2105</a></p>
          </div>
          <div class="footer-col">
            <h4>Follow Us</h4>
            <div class="social-links">
              <a href="http://www.facebook.com/Sierra-Vista-Plumbing-Inc-Hvac-363355883836429" target="_blank"
                class="social-icon">Facebook</a>
              <a href="https://maps.google.com/maps?daddr=4847 South Hwy 92, Sierra Vista, AZ 85650" target="_blank"
                class="social-icon">Google</a>
            </div>
          </div>
        </div>
        <div class="footer-bottom">
          <p>&copy; {{ currentYear }} Sierra Vista Plumbing, Inc. All rights reserved.</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const currentYear = computed(() => new Date().getFullYear())
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root {
  --primary-color: #a90e18;
  --secondary-color: #1a1a1a;
  --text-color: #333;
  --light-bg: #f8f9fa;
  --white: #ffffff;
  --shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: var(--text-color);
  line-height: 1.6;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Header Styles */
.site-header {
  background: var(--white);
  box-shadow: var(--shadow);
  position: sticky;
  top: 0;
  z-index: 1000;
  padding: 1rem 0;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
}

.logo img {
  height: 60px;
  width: auto;
}

.main-nav {
  display: flex;
  gap: 2rem;
  align-items: center;
}

.main-nav a,
.nav-dropdown-toggle {
  text-decoration: none;
  color: var(--text-color);
  font-weight: 500;
  transition: color 0.3s;
  cursor: pointer;
}

.main-nav a:hover,
.main-nav a.router-link-active,
.nav-dropdown:hover .nav-dropdown-toggle {
  color: var(--primary-color);
}

.nav-dropdown {
  position: relative;
}

.nav-dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  min-width: 220px;
  background: var(--white);
  box-shadow: var(--shadow);
  padding: 0.5rem 0;
  margin-top: 0.5rem;
  border-radius: 4px;
  z-index: 1000;
}

.nav-dropdown:hover .nav-dropdown-menu {
  display: block;
}

.nav-dropdown-menu a {
  display: block;
  padding: 0.75rem 1.5rem;
  color: var(--text-color);
  text-decoration: none;
  transition: background-color 0.3s, color 0.3s;
  white-space: nowrap;
}

.nav-dropdown-menu a:hover,
.nav-dropdown-menu a.router-link-active {
  background-color: var(--light-bg);
  color: var(--primary-color);
}

.header-contact {
  text-align: right;
}

.header-contact .label {
  display: block;
  font-size: 0.875rem;
  color: #666;
}

.header-contact .phone {
  display: block;
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--primary-color);
  text-decoration: none;
}

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

/* Footer */
.site-footer {
  background: var(--secondary-color);
  color: var(--white);
  padding: 3rem 0 1rem;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.footer-col h4 {
  margin-bottom: 1rem;
  color: var(--white);
}

.footer-col p {
  color: #ccc;
  margin-bottom: 0.5rem;
}

.footer-col ul {
  list-style: none;
}

.footer-col ul li {
  margin-bottom: 0.5rem;
}

.footer-col ul li a {
  color: #ccc;
  text-decoration: none;
  transition: color 0.3s;
}

.footer-col ul li a:hover {
  color: var(--white);
}

.footer-col a {
  color: #ccc;
  text-decoration: none;
}

.social-links {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.social-icon {
  color: #ccc;
  transition: color 0.3s;
}

.social-icon:hover {
  color: var(--white);
}

.footer-bottom {
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid #333;
  color: #ccc;
}

/* Responsive Design */
@media (max-width: 768px) {
  .header-content {
    flex-direction: column;
    text-align: center;
  }

  .main-nav {
    flex-direction: column;
    gap: 1rem;
  }

  .nav-dropdown-menu {
    position: static;
    margin-top: 0.25rem;
    box-shadow: none;
    background: var(--light-bg);
  }

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
