<template>
  <div>
    <!-- Hero Section -->
    <section class="hero-inner">
      <div class="hero-slide" :style="{ backgroundImage: `url(/download/wp-content/uploads/b2b/stock/v2/bigstock/bath-wrench-plumling-7068036.jpg)` }">
        <div class="hero-overlay"></div>
        <div class="container">
          <div class="hero-content">
            <h1 class="hero-title">Frequently Asked Questions</h1>
            <p class="hero-subtitle">Find answers to common plumbing, heating, and AC questions</p>
            <a href="tel:5204172105" class="btn btn-primary">Call (520) 417-2105</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Main Content Section -->
    <section class="content-section">
      <div class="container">
        <div class="content-grid">
          <div class="main-content">
            <div class="content-block">
              <p class="intro-text">
                Have questions about our plumbing, heating, or air conditioning services? We've compiled answers 
                to the most frequently asked questions from our customers in Sierra Vista, AZ. If you don't find 
                the answer you're looking for, please don't hesitate to contact us directly.
              </p>
            </div>

            <!-- FAQ Items -->
            <div class="faq-list">
              <div class="faq-item">
                <div class="faq-question">
                  <div class="faq-icon">?</div>
                  <h3>How can I check if I have a leak?</h3>
                </div>
                <div class="faq-answer">
                  <p>
                    The easiest way is to look at your water meter. If the meter is moving you have water moving. 
                    Time the meter for 3 minutes in order to catch smaller leaks. If you're unsure, give us a call!
                  </p>
                </div>
              </div>

              <div class="faq-item">
                <div class="faq-question">
                  <div class="faq-icon">?</div>
                  <h3>How do you schedule your clients?</h3>
                </div>
                <div class="faq-answer">
                  <p>
                    Clients get scheduled in the order that they call. We have a few time brackets so normal service 
                    calls do not have to wait behind bigger all day jobs.
                  </p>
                </div>
              </div>

              <div class="faq-item">
                <div class="faq-question">
                  <div class="faq-icon">?</div>
                  <h3>What is your typical process for working with a customer?</h3>
                </div>
                <div class="faq-answer">
                  <p>
                    Our process is streamlined. Customers make contact with our office at 520-417-2105. Zach is 
                    normally the first point of contact. Zach will take their information and schedule an appointment. 
                    All of our techs are radio dispatched so if something needs quick attention, we can expedite it.
                  </p>
                </div>
              </div>

              <div class="faq-item">
                <div class="faq-question">
                  <div class="faq-icon">?</div>
                  <h3>How long do jobs usually take?</h3>
                </div>
                <div class="faq-answer">
                  <p>
                    Normal jobs take an hour or two. More complex repairs or installations may take longer, and 
                    we'll provide you with an estimated timeframe when we schedule your appointment.
                  </p>
                </div>
              </div>

              <div class="faq-item">
                <div class="faq-question">
                  <div class="faq-icon">?</div>
                  <h3>Should I repair or replace leaky faucets?</h3>
                </div>
                <div class="faq-answer">
                  <p>
                    Typically a repair is recommended. It's entirely up to the customer once we diagnose the issue. 
                    Our experienced technicians will provide you with options and help you make the best decision 
                    for your situation and budget.
                  </p>
                </div>
              </div>

              <div class="faq-item">
                <div class="faq-question">
                  <div class="faq-icon">?</div>
                  <h3>Why does my hot water not work as well in the winter?</h3>
                </div>
                <div class="faq-answer">
                  <p>
                    Typically it is because the incoming cold water is colder this time of year. Your water heater 
                    has to work harder to heat the water to the desired temperature. If you're experiencing 
                    significant issues, we can inspect your water heater to ensure it's functioning properly.
                  </p>
                </div>
              </div>
            </div>

            <div class="content-block call-to-action-box">
              <h2>Still Have Questions?</h2>
              <p>
                Our friendly team is here to help! Whether you need emergency service or want to schedule a 
                routine maintenance appointment, we're just a phone call away.
              </p>
              <div class="action-buttons">
                <a href="tel:5204172105" class="btn btn-primary">Call (520) 417-2105</a>
                <router-link to="/contact" class="btn btn-secondary-outline">Contact Us Online</router-link>
              </div>
            </div>
          </div>

          <aside class="sidebar">
            <div class="sidebar-card">
              <h3>Need Immediate Help?</h3>
              <p>Our experts are standing by to assist you with any plumbing, heating, or AC needs.</p>
              <a href="tel:5204172105" class="btn btn-block">(520) 417-2105</a>
              <a href="tel:5205592534" class="btn btn-block btn-secondary">(520) 559-2534</a>
            </div>

            <div class="sidebar-card">
              <h3>Our Services</h3>
              <ul class="service-links">
                <li><router-link to="/plumbing-services">Plumbing Services</router-link></li>
                <li><router-link to="/heating-services">Heating Services</router-link></li>
                <li><router-link to="/air-conditioning-services">AC Services</router-link></li>
                <li><router-link to="/duct-cleaning-services">Duct Cleaning</router-link></li>
                <li><router-link to="/dryer-vent-rotobrush-cleaning-services">Dryer Vent Cleaning</router-link></li>
              </ul>
            </div>

            <div class="sidebar-card highlight">
              <h3>24/7 Emergency Service</h3>
              <p>Plumbing emergencies don't wait for business hours. We're here when you need us most.</p>
            </div>

            <div class="sidebar-card info-card">
              <h3>Service Area</h3>
              <p>We proudly serve:</p>
              <ul class="service-areas">
                <li>Sierra Vista, AZ</li>
                <li>Bisbee, AZ</li>
                <li>Benson, AZ</li>
                <li>Huachuca City, AZ</li>
                <li>Whetstone, AZ</li>
              </ul>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section" :style="{ backgroundImage: `url(/download/files/2019/02/1551296179350_bigstock_124843106.jpg)` }">
      <div class="cta-overlay"></div>
      <div class="container">
        <div class="cta-content">
          <h2>Ready to Experience Quality Service?</h2>
          <p>Family owned and operated with over 30 years of experience</p>
          <router-link to="/contact" class="btn btn-white">Schedule Service Today</router-link>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="features-section">
      <div class="container">
        <h2>Why Choose Sierra Vista Plumbing?</h2>
        <div class="features-grid">
          <div class="feature-item">
            <div class="feature-icon">✓</div>
            <h3>30+ Years Experience</h3>
            <p>Trusted expertise serving Sierra Vista since our founding</p>
          </div>
          <div class="feature-item">
            <div class="feature-icon">✓</div>
            <h3>Licensed & Insured</h3>
            <p>Fully certified and insured for your protection</p>
          </div>
          <div class="feature-item">
            <div class="feature-icon">✓</div>
            <h3>Upfront Pricing</h3>
            <p>Clear, honest quotes with no hidden fees</p>
          </div>
          <div class="feature-item">
            <div class="feature-icon">✓</div>
            <h3>24/7 Emergency Service</h3>
            <p>Available when you need us most</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'FAQ | Sierra Vista Plumbing, Inc.',
  description: 'Find answers to frequently asked questions about our plumbing, heating, and air conditioning services in Sierra Vista, AZ.',
  image: '/download/wp-content/uploads/b2b/stock/v2/bigstock/bath-wrench-plumling-7068036.jpg',
  url: '/faq'
})
</script>

<style scoped>
/* Hero Section */
.hero-inner {
  position: relative;
  height: 500px;
  overflow: hidden;
}

.hero-slide {
  height: 100%;
  background-size: cover;
  background-position: center;
  position: relative;
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
  color: white;
  padding-top: 150px;
  text-align: center;
}

.hero-title {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 1rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.hero-subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
}

/* Content Section */
.content-section {
  padding: 4rem 0;
  background: #f8f9fa;
}

.content-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 3rem;
}

.main-content {
  background: white;
  padding: 2.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.content-block {
  margin-bottom: 2.5rem;
}

.content-block:last-child {
  margin-bottom: 0;
}

.content-block h2 {
  font-size: 2rem;
  color: #dc3545;
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 3px solid #dc3545;
}

.intro-text {
  font-size: 1.15rem;
  line-height: 1.8;
  margin-bottom: 1rem;
  color: #555;
}

/* FAQ Items */
.faq-list {
  margin: 2rem 0;
}

.faq-item {
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 1.5rem;
  overflow: hidden;
  border-left: 4px solid #dc3545;
  transition: all 0.3s;
}

.faq-item:hover {
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.2);
  transform: translateX(5px);
}

.faq-question {
  display: flex;
  align-items: center;
  padding: 1.5rem;
  background: #ffffff;
}

.faq-icon {
  width: 50px;
  height: 50px;
  background: #dc3545;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
  font-weight: bold;
  margin-right: 1.5rem;
  flex-shrink: 0;
}

.faq-question h3 {
  font-size: 1.3rem;
  color: #333;
  margin: 0;
  line-height: 1.4;
}

.faq-answer {
  padding: 0 1.5rem 1.5rem 1.5rem;
  background: #ffffff;
}

.faq-answer p {
  color: #666;
  line-height: 1.8;
  margin: 0;
  padding-left: 65px;
}

/* Call to Action Box */
.call-to-action-box {
  background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
  padding: 2.5rem;
  border-radius: 8px;
  text-align: center;
  margin-top: 3rem;
}

.call-to-action-box h2 {
  border-bottom: none;
  margin-bottom: 1rem;
}

.call-to-action-box p {
  font-size: 1.1rem;
  line-height: 1.8;
  margin-bottom: 2rem;
  color: #555;
}

.action-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn-secondary-outline {
  background: transparent;
  border: 2px solid #dc3545;
  color: #dc3545;
  display: inline-block;
  padding: 0.75rem 2rem;
  text-decoration: none;
  border-radius: 4px;
  font-weight: 600;
  transition: all 0.3s;
}

.btn-secondary-outline:hover {
  background: #dc3545;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.3);
}

/* Sidebar */
.sidebar {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.sidebar-card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.sidebar-card.highlight {
  background: linear-gradient(135deg, #dc3545 0%, #c82333 100%);
  color: white;
}

.sidebar-card h3 {
  font-size: 1.3rem;
  margin-bottom: 1rem;
  color: #333;
}

.sidebar-card.highlight h3 {
  color: white;
}

.sidebar-card p {
  margin-bottom: 1rem;
  line-height: 1.6;
}

.sidebar-card.highlight p {
  margin-bottom: 0;
}

.btn-block {
  display: block;
  width: 100%;
  text-align: center;
  padding: 0.75rem;
  margin-bottom: 0.5rem;
}

.btn-secondary {
  background: #6c757d;
}

.btn-secondary:hover {
  background: #5a6268;
}

.service-links {
  list-style: none;
  padding: 0;
  margin: 0;
}

.service-links li {
  border-bottom: 1px solid #e9ecef;
  padding: 0.75rem 0;
}

.service-links li:last-child {
  border-bottom: none;
}

.service-links a {
  color: #dc3545;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.3s;
}

.service-links a:hover {
  color: #c82333;
}

.info-card ul.service-areas {
  list-style: none;
  padding: 0;
  margin: 0.5rem 0 0 0;
}

.info-card ul.service-areas li {
  padding: 0.4rem 0;
  color: #555;
  font-size: 0.95rem;
}

/* CTA Section */
.cta-section {
  position: relative;
  padding: 5rem 0;
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

.cta-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(220, 53, 69, 0.85);
}

.cta-content {
  position: relative;
  z-index: 2;
  text-align: center;
  color: white;
}

.cta-content h2 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  font-weight: bold;
}

.cta-content p {
  font-size: 1.3rem;
  margin-bottom: 2rem;
}

.btn-white {
  background: white;
  color: #dc3545;
  font-weight: bold;
}

.btn-white:hover {
  background: #f8f9fa;
  color: #c82333;
}

/* Features Section */
.features-section {
  padding: 4rem 0;
  background: white;
}

.features-section h2 {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 3rem;
  color: #333;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2rem;
}

.feature-item {
  text-align: center;
  padding: 2rem 1rem;
}

.feature-icon {
  width: 70px;
  height: 70px;
  margin: 0 auto 1rem;
  background: #dc3545;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  font-weight: bold;
}

.feature-item h3 {
  font-size: 1.3rem;
  margin-bottom: 0.5rem;
  color: #333;
}

.feature-item p {
  color: #666;
  line-height: 1.6;
}

/* Common Styles */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

.btn {
  display: inline-block;
  padding: 0.75rem 2rem;
  background: #dc3545;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-weight: 600;
  transition: all 0.3s;
  border: none;
  cursor: pointer;
}

.btn:hover {
  background: #c82333;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.3);
}

.btn-primary {
  background: #dc3545;
}

.btn-primary:hover {
  background: #c82333;
}

/* Responsive Design */
@media (max-width: 992px) {
  .content-grid {
    grid-template-columns: 1fr;
  }

  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .hero-title {
    font-size: 2rem;
  }

  .hero-subtitle {
    font-size: 1.2rem;
  }
}

@media (max-width: 768px) {
  .hero-inner {
    height: 400px;
  }

  .hero-content {
    padding-top: 100px;
  }

  .hero-title {
    font-size: 1.8rem;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }

  .main-content {
    padding: 1.5rem;
  }

  .faq-question {
    flex-direction: column;
    text-align: center;
  }

  .faq-icon {
    margin-right: 0;
    margin-bottom: 1rem;
  }

  .faq-answer p {
    padding-left: 0;
  }

  .action-buttons {
    flex-direction: column;
  }

  .action-buttons .btn,
  .action-buttons .btn-secondary-outline {
    width: 100%;
  }

  .cta-content h2 {
    font-size: 2rem;
  }

  .cta-content p {
    font-size: 1.1rem;
  }
}
</style>
