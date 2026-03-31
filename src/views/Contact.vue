<template>
  <div class="contact-page">
    <section class="hero-section">
      <div class="container hero-content">
        <p class="eyebrow">Sierra Vista Plumbing, Inc.</p>
        <h1>Find a Plumber in Sierra Vista, AZ</h1>
        <p class="hero-subtitle">Hire an experienced professional for plumbing and HVAC services.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="tel:520-417-2105">Call (520) 417-2105</a>
          <a class="btn btn-secondary" href="#contact-methods">Contact Options</a>
        </div>
      </div>
    </section>

    <section id="contact-methods" class="contact-section">
      <div class="container">
        <div class="intro-card">
          <h2>Contact Us Now</h2>
          <p>
            Thank you for visiting Sierra Vista Plumbing, Inc. We look forward to working in your
            home or commercial space soon. Use the contact options below to request service,
            ask a question, or schedule an estimate.
          </p>
        </div>

        <div class="methods-grid">
          <article class="method-card">
            <h3>Primary Phone</h3>
            <p class="method-value"><a href="tel:520-417-2105">(520) 417-2105</a></p>
            <p>Available for plumbing and HVAC service requests.</p>
          </article>

          <article class="method-card">
            <h3>Second Office</h3>
            <p class="method-value"><a href="tel:520-559-2534">(520) 559-2534</a></p>
            <p>Alternate line for office and scheduling support.</p>
          </article>

          <article class="method-card">
            <h3>Business Address</h3>
            <p class="method-value">4847 South Hwy 92<br />Sierra Vista, AZ 85650</p>
            <p>
              <a
                href="https://maps.google.com/maps?daddr=4847+South+Hwy+92,+Sierra+Vista,+AZ+85650"
                target="_blank"
                rel="noopener noreferrer"
              >
                Get Directions
              </a>
            </p>
          </article>

          <article class="method-card">
            <h3>Business Hours</h3>
            <p class="method-value">Mon - Fri: 8:00 AM - 5:00 PM</p>
            <p>Saturday: Closed<br />Sunday: Closed</p>
          </article>
        </div>
      </div>
    </section>

    <section class="map-section">
      <div class="container">
        <h2>Visit Our Sierra Vista Office</h2>
        <div class="map-frame-wrap">
          <iframe
            title="Sierra Vista Plumbing, Inc. Location"
            src="https://www.google.com/maps?q=4847+South+Hwy+92,+Sierra+Vista,+AZ+85650&output=embed"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
          ></iframe>
        </div>
      </div>
    </section>

    <section class="cta-section">
      <div class="container cta-card">
        <h2>Need Plumbing or HVAC Help?</h2>
        <p>
          Family owned and operated with 24/7 emergency service availability. Reach out now for
          fast support.
        </p>
        <div class="cta-actions">
          <a class="btn btn-primary" href="tel:520-417-2105">Call Now</a>
          <a class="btn btn-secondary" href="mailto:service@sierravistaplumbinginc.com?subject=Service%20Estimate%20Request">Email for Estimate</a>
        </div>
      </div>
    </section>

    <section class="areas-section">
      <div class="container">
        <h2>Service Areas</h2>
        <div class="area-chips">
          <span>Sierra Vista, AZ</span>
          <span>Bisbee, AZ</span>
          <span>Benson, AZ</span>
          <span>Huachuca City, AZ</span>
          <span>Whetstone, AZ</span>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Contact A Plumber in Sierra Vista, AZ | Sierra Vista Plumbing, Inc.',
  description: 'We provide plumbing and HVAC services in Sierra Vista, AZ. We look forward to working in your home or commercial space soon. Give us a call at (520) 417-2105.',
  url: '/contact'
})
</script>

<style scoped>
.contact-page {
  background: radial-gradient(circle at 10% 10%, #fff8ed 0%, #f7f8fa 45%, #eef1f4 100%);
  color: #1f2a33;
}

.container {
  width: min(1100px, calc(100% - 2rem));
  margin: 0 auto;
}

.hero-section {
  background: linear-gradient(130deg, #8f1d14 0%, #bf4a2f 52%, #f5ad48 100%);
  color: #fff;
  padding: 5rem 0 4rem;
}

.hero-content {
  text-align: center;
  animation: rise-in 0.7s ease both;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 700;
  margin-bottom: 0.6rem;
}

.hero-content h1 {
  font-size: clamp(2rem, 4vw, 3.4rem);
  line-height: 1.15;
  margin: 0;
}

.hero-subtitle {
  margin: 1rem auto 1.8rem;
  max-width: 720px;
  font-size: 1.1rem;
}

.hero-actions,
.cta-actions {
  display: flex;
  justify-content: center;
  gap: 0.9rem;
  flex-wrap: wrap;
}

.btn {
  display: inline-block;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 700;
  padding: 0.8rem 1.2rem;
  border: 2px solid transparent;
  transition: transform 0.2s ease, background-color 0.2s ease;
}

.btn:hover {
  transform: translateY(-1px);
}

.btn-primary {
  background: #12263a;
  color: #fff;
}

.btn-primary:hover {
  background: #0b1928;
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.65);
  color: #fff;
}

.contact-section,
.map-section,
.cta-section {
  padding: 3rem 0;
}

.intro-card,
.cta-card {
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 14px 34px rgba(18, 38, 58, 0.08);
  padding: 1.6rem;
  margin-bottom: 1.5rem;
}

.intro-card h2,
.map-section h2,
.cta-card h2 {
  margin-top: 0;
  color: #8f1d14;
}

.methods-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
}

.method-card {
  background: #fff;
  border-radius: 14px;
  border: 1px solid #e6e8ec;
  padding: 1rem;
}

.method-card h3 {
  margin-top: 0;
  margin-bottom: 0.7rem;
}

.method-value {
  font-weight: 700;
  color: #12263a;
}

.method-card a {
  color: #8f1d14;
}

.map-frame-wrap {
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 14px 30px rgba(18, 38, 58, 0.13);
}

.map-frame-wrap iframe {
  width: 100%;
  min-height: 430px;
  border: 0;
}

.cta-card {
  text-align: center;
}

.areas-section {
  padding: 0 0 3.5rem;
}

.areas-section h2 {
  text-align: center;
  color: #8f1d14;
  margin-top: 0;
  margin-bottom: 1rem;
}

.area-chips {
  display: flex;
  gap: 0.7rem;
  flex-wrap: wrap;
  justify-content: center;
}

.area-chips span {
  background: #ffffff;
  border: 1px solid #d9dfe6;
  border-radius: 999px;
  padding: 0.45rem 0.85rem;
  font-weight: 600;
}

@keyframes rise-in {
  from {
    opacity: 0;
    transform: translateY(14px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 980px) {
  .methods-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 640px) {
  .hero-section {
    padding: 4rem 0 3.2rem;
  }

  .methods-grid {
    grid-template-columns: 1fr;
  }

  .map-frame-wrap iframe {
    min-height: 340px;
  }
}
</style>
