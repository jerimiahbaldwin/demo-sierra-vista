<template>
  <div class="reviews-page">
    <section class="reviews-hero">
      <div class="hero-overlay"></div>
      <div class="container hero-content">
        <p class="eyebrow">Local Reputation</p>
        <h1>Reviews from Sierra Vista Homeowners</h1>
        <p class="hero-copy">
          Read what customers are saying about plumbing, heating, and cooling service from Sierra Vista Plumbing,
          Inc.
        </p>
        <div class="hero-actions">
          <a href="https://g.page/SierraVistaPlumbingINC?share" target="_blank" rel="noopener" class="btn btn-primary">
            Read Our Top Reviews
          </a>
          <a href="https://g.page/SierraVistaPlumbingINC?share" target="_blank" rel="noopener"
            class="btn btn-secondary">
            Leave a Review on Google
          </a>
        </div>
      </div>
    </section>

    <section class="testimonials-section">
      <div class="container">
        <div class="section-heading">
          <h2>What Customers Are Saying</h2>
          <p>
            Highlights below are sourced from the original site and linked to our Google review profile.
          </p>
        </div>

        <div class="testimonials-grid">
          <article v-for="review in reviews" :key="review.author" class="review-card">
            <p class="review-text">{{ review.text }}</p>
            <div class="review-meta">
              <a :href="googleReviewUrl" target="_blank" rel="noopener" class="review-author">{{ review.author }}</a>
              <span>Reviewed on Google</span>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="review-cta-section">
      <div class="container cta-wrap">
        <div>
          <h2>Have We Helped You Recently?</h2>
          <p>
            Your feedback helps neighbors choose a trusted local team for plumbing and HVAC work.
          </p>
        </div>
        <a href="https://g.page/SierraVistaPlumbingINC?share" target="_blank" rel="noopener" class="btn btn-primary">
          Leave a Review
        </a>
      </div>
    </section>

    <section class="emergency-banner">
      <div class="container emergency-content">
        <h3>24/7 Emergency Service Available</h3>
        <p>Family Owned and Operated | Call: (520) 417-2105 | Second Office: (520) 559-2534</p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

const googleReviewUrl = 'https://g.page/SierraVistaPlumbingINC?share'

const reviews = [
  {
    author: 'Carlos Rivera',
    text: 'The best in Sierra Vista. Easy and quick to schedule a service call. The technician was prompt, courteous, and provided an explanation and estimate. Work was completed quickly and got things flowing again at a reasonable cost.'
  },
  {
    author: 'Troy Clayton',
    text: 'Clear a kitchen sink clog in no time. Even worked after hours and got it done. David was great.'
  },
  {
    author: 'B Diddy',
    text: "I\'ve used Sierra Vista Plumbing for about 10 years for two different houses. They\'ve handled complex leaks, water heater installs, and basic plumbing jobs with top-notch workmanship. Highly recommended."
  },
  {
    author: 'Kenneth Dymski',
    text: 'Sierra Vista Plumbing installed a garbage disposal and repaired a leaking toilet. Aaron Wright was a true professional, and the parts and labor cost was very reasonable.'
  },
  {
    author: 'Ron Crandall',
    text: 'Very nice, very reasonable, fixed all my problems. I will definitely call them back for all my plumbing needs.'
  },
  {
    author: 'Donald Fritz',
    text: 'Great job with short notice.'
  },
  {
    author: 'Donna Bowser',
    text: 'I was impressed with the quality of work on a new heating and cooling system plus a hot water heater. Jared and his team were professional and successful in taking care of all my needs.'
  },
  {
    author: 'nicyboosma',
    text: 'Simply amazing. They came quickly, diagnosed the AC issue, coordinated with home warranty, and got us taken care of fast. They went above and beyond expectations.'
  },
  {
    author: 'Zachary Burres',
    text: 'I called Sierra Vista Plumbing to repair my air conditioner and service my heater for winter. They were quick, helpful, and everything is working perfectly now.'
  },
  {
    author: 'Tim Seifert',
    text: 'Excellent work.'
  }
]

useSeo({
  title: 'Reviews | Sierra Vista Plumbing, Inc.',
  description: 'Read verified customer reviews for plumbing, heating, and cooling services from Sierra Vista Plumbing, Inc.',
  image: '/images/logo/sierra-vista-logo.png',
  url: '/reviews'
})
</script>

<style scoped>
.reviews-page {
  color: #1f2937;
  background: #f8fafc;
}

.container {
  width: min(1120px, 92vw);
  margin: 0 auto;
}

.reviews-hero {
  position: relative;
  overflow: hidden;
  background:
    radial-gradient(circle at 20% 20%, rgba(250, 204, 21, 0.18), transparent 42%),
    linear-gradient(135deg, #7f1d1d 0%, #111827 88%);
  color: #fff;
  padding: 5.5rem 0 4.25rem;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(17, 24, 39, 0.2), rgba(17, 24, 39, 0.45));
}

.hero-content {
  position: relative;
  z-index: 1;
}

.eyebrow {
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-size: 0.75rem;
  font-weight: 700;
  color: #fcd34d;
  margin-bottom: 0.75rem;
}

h1 {
  margin: 0;
  font-size: clamp(2rem, 5vw, 3.1rem);
  line-height: 1.1;
  max-width: 14ch;
}

.hero-copy {
  margin-top: 1rem;
  max-width: 60ch;
  font-size: 1.05rem;
  line-height: 1.7;
  color: #e5e7eb;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.85rem;
  margin-top: 1.5rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.8rem 1.2rem;
  border-radius: 0.6rem;
  text-decoration: none;
  font-weight: 700;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.btn:hover {
  transform: translateY(-1px);
}

.btn-primary {
  background: #b91c1c;
  color: #fff;
  box-shadow: 0 10px 20px rgba(127, 29, 29, 0.28);
}

.btn-secondary {
  border: 1px solid rgba(255, 255, 255, 0.55);
  color: #fff;
  background: rgba(255, 255, 255, 0.06);
}

.testimonials-section {
  padding: 3.5rem 0;
}

.section-heading {
  margin-bottom: 1.5rem;
}

.section-heading h2 {
  margin: 0;
  color: #111827;
  font-size: clamp(1.5rem, 3vw, 2.1rem);
}

.section-heading p {
  margin: 0.65rem 0 0;
  color: #4b5563;
}

.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.review-card {
  background: #fff;
  border: 1px solid #e5e7eb;
  border-radius: 0.9rem;
  padding: 1.1rem;
  box-shadow: 0 14px 28px rgba(15, 23, 42, 0.06);
}

.review-text {
  margin: 0;
  color: #374151;
  line-height: 1.65;
}

.review-meta {
  margin-top: 0.85rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  font-size: 0.88rem;
  color: #6b7280;
}

.review-author {
  color: #991b1b;
  font-weight: 700;
  text-decoration: none;
}

.review-author:hover {
  text-decoration: underline;
}

.review-cta-section {
  padding: 0 0 4rem;
}

.emergency-banner {
  padding: 1.1rem 0 1.35rem;
  background: #111827;
  color: #f9fafb;
  text-align: center;
}

.emergency-content h3 {
  margin: 0;
  font-size: 1.05rem;
}

.emergency-content p {
  margin: 0.35rem 0 0;
  color: #d1d5db;
}

.cta-wrap {
  background: linear-gradient(135deg, #111827, #7f1d1d);
  color: #fff;
  border-radius: 1rem;
  padding: 1.4rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 1rem;
}

.cta-wrap h2 {
  margin: 0;
  font-size: clamp(1.2rem, 2.8vw, 1.7rem);
}

.cta-wrap p {
  margin: 0.5rem 0 0;
  color: #e5e7eb;
}

@media (max-width: 900px) {
  .testimonials-grid {
    grid-template-columns: 1fr;
  }

  .cta-wrap {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>
