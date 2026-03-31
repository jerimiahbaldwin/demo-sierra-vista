<template>
  <div class="dryer-page">
    <section class="hero">
      <div class="hero-overlay"></div>
      <div class="container hero-content">
        <p class="eyebrow">Dryer Vent and Rotobrush Service</p>
        <h1>Get Rid of Lint Clogging Your Dryer Vent</h1>
        <p>
          Bring us in for dryer vent cleaning services in Sierra Vista, AZ and reduce fire risk
          caused by lint and debris buildup.
        </p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="/contact">Contact Us</a>
          <a class="btn btn-secondary" href="tel:520-417-2105">Call (520) 417-2105</a>
        </div>
      </div>
    </section>

    <section class="content-section">
      <div class="container content-grid">
        <article class="content-card">
          <h2>Protect Your Home With a Professional Cleaning</h2>
          <p>
            A lint-filled dryer vent is a serious fire hazard. If you cannot remember the last
            time your dryer vent was cleaned, you are due for dryer vent cleaning service.
            Sierra Vista Plumbing, Inc. removes dust, debris, and lint buildup using professional
            Rotobrush equipment.
          </p>
          <p>
            Contact us now to schedule your service and keep your system operating safely.
          </p>
        </article>

        <div class="image-wrap">
          <img
            src="/download/files/shutterstock/2024/04/shutterstock_1982877248_1712001067_e1e5c4d705eda0b4d4396cfe983bbf5c44.jpg"
            alt="Dryer vent cleaning service technician"
          />
        </div>
      </div>
    </section>

    <section class="benefits-section">
      <div class="container">
        <h2>Producing Top-Notch Results for Every Job</h2>
        <p class="intro">
          We have the equipment needed to clean heavily impacted vents and restore airflow.
        </p>

        <div class="benefits-grid">
          <article class="benefit-card">
            <h3>Rotobrush Power</h3>
            <p>The powerful motorized system agitates and vacuums vent buildup thoroughly.</p>
          </article>
          <article class="benefit-card">
            <h3>Thorough Cleaning</h3>
            <p>We target dust, lint, and debris all the way through the vent path.</p>
          </article>
          <article class="benefit-card">
            <h3>Safer Operation</h3>
            <p>A clean vent helps reduce overheating conditions and lowers fire risk.</p>
          </article>
          <article class="benefit-card">
            <h3>Local Experts</h3>
            <p>Family-owned local team serving Sierra Vista and surrounding communities.</p>
          </article>
        </div>

        <div class="cta-wrap">
          <a class="btn btn-primary" href="/contact">Request Dryer Vent Cleaning</a>
        </div>
      </div>
    </section>

    <section class="service-areas">
      <div class="container">
        <h2>Service Areas</h2>
        <div class="chips">
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
  title: 'Dryer Vent Cleaning Services | Sierra Vista, AZ | Sierra Vista Plumbing, Inc.',
  description: 'A lint-filled dryer vent is a serious fire hazard. If you can\'t remember the last time your dryer vent was cleaned, you\'re due for dryer vent cleaning services.',
  image: '/download/files/shutterstock/2024/04/shutterstock_1982877248_1712001067_e1e5c4d705eda0b4d4396cfe983bbf5c44.jpg',
  url: '/dryer-vent-rotobrush-cleaning-services'
})
</script>

<style scoped>
.dryer-page {
  background: linear-gradient(180deg, #fffdf8 0%, #f6f9fc 100%);
  color: #1f2937;
}

.container {
  width: min(1120px, 92vw);
  margin: 0 auto;
}

.hero {
  position: relative;
  padding: 5rem 0 4rem;
  color: #ffffff;
  background:
    linear-gradient(135deg, rgba(127, 29, 29, 0.9), rgba(17, 24, 39, 0.78)),
    url('/download/files/shutterstock/2024/04/shutterstock_1982877248_1712001067_e1e5c4d705eda0b4d4396cfe983bbf5c44.jpg') center/cover;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.15), rgba(0, 0, 0, 0.3));
}

.hero-content {
  position: relative;
  z-index: 1;
  max-width: 760px;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.78rem;
  color: #fde68a;
  margin: 0 0 0.8rem;
  font-weight: 700;
}

h1 {
  margin: 0;
  font-size: clamp(2rem, 5vw, 3.2rem);
  line-height: 1.12;
}

.hero p {
  margin: 1rem 0 0;
  font-size: 1.08rem;
  line-height: 1.7;
  color: #e5e7eb;
}

.hero-actions {
  margin-top: 1.5rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  font-weight: 700;
  border-radius: 999px;
  padding: 0.75rem 1.15rem;
  border: 2px solid transparent;
  transition: transform 0.2s ease;
}

.btn:hover {
  transform: translateY(-1px);
}

.btn-primary {
  background: #b91c1c;
  color: #fff;
}

.btn-secondary {
  color: #fff;
  border-color: rgba(255, 255, 255, 0.65);
  background: rgba(255, 255, 255, 0.08);
}

.content-section,
.benefits-section,
.service-areas {
  padding: 3.2rem 0;
}

.content-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 1.25rem;
  align-items: stretch;
}

.content-card {
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 1.25rem;
  box-shadow: 0 12px 26px rgba(15, 23, 42, 0.07);
}

.content-card h2 {
  margin-top: 0;
  color: #7f1d1d;
}

.content-card p {
  margin: 0.8rem 0 0;
  line-height: 1.75;
}

.image-wrap {
  border-radius: 16px;
  overflow: hidden;
  min-height: 320px;
  box-shadow: 0 12px 28px rgba(15, 23, 42, 0.16);
}

.image-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.benefits-section h2,
.service-areas h2 {
  margin: 0;
  text-align: center;
  color: #7f1d1d;
}

.intro {
  margin: 0.7rem auto 1.4rem;
  text-align: center;
  max-width: 65ch;
  color: #4b5563;
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.benefit-card {
  background: #ffffff;
  border-radius: 14px;
  border: 1px solid #e5e7eb;
  padding: 1rem;
}

.benefit-card h3 {
  margin: 0;
  color: #111827;
}

.benefit-card p {
  margin: 0.6rem 0 0;
  color: #4b5563;
  line-height: 1.6;
}

.cta-wrap {
  margin-top: 1.35rem;
  text-align: center;
}

.chips {
  margin-top: 1rem;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.7rem;
}

.chips span {
  border: 1px solid #d1d5db;
  background: #ffffff;
  border-radius: 999px;
  padding: 0.45rem 0.8rem;
  font-weight: 600;
}

@media (max-width: 900px) {
  .content-grid {
    grid-template-columns: 1fr;
  }

  .benefits-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 640px) {
  .hero {
    padding: 4rem 0 3.2rem;
  }
}
</style>
