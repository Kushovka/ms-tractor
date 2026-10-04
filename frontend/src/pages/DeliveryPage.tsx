import { FaArrowRight, FaCalendarAlt, FaClock, FaPhoneAlt, FaShieldAlt, FaTruck } from 'react-icons/fa'
import { Link } from 'react-router'
import { HeroScrollCue } from '../components/HeroScrollCue'
import { Seo } from '../components/Seo'
import { business } from '../data/business'
import { trackContactCta } from '../utils/ctaTracking'

export const DeliveryPage = () => (
  <main className="delivery-page">
    <Seo title="Nationwide Equipment Delivery" description="M & S Tractor & Equipment delivers agricultural equipment from Shreveport, Louisiana across the United States." />
    <section className="delivery-hero" aria-labelledby="delivery-title">
      <div className="delivery-hero-copy">
        <h1 id="delivery-title">Nationwide<br />Delivery</h1>
        <p className="delivery-hero-description">We deliver the equipment you need safely, reliably, and on time. From our lot to your farm, job site or business anywhere in the U.S.</p>
        <div className="delivery-actions">
          <Link className="delivery-button delivery-button--primary" to="/contact">
            Request a Delivery Quote <FaArrowRight aria-hidden="true" />
          </Link>
          <a className="delivery-button delivery-button--phone" href={business.phoneHref} onClick={() => trackContactCta('phone_click', 'Delivery Hero Call')}>
            Call {business.phone} <FaArrowRight aria-hidden="true" />
          </a>
        </div>
      </div>
      <HeroScrollCue target="delivery-services" label="Scroll to delivery services" />
    </section>
    <section id="delivery-services" className="delivery-services" aria-labelledby="delivery-services-title">
      <div className="delivery-services-top">
        <div className="delivery-services-copy">
          <h2 id="delivery-services-title">Built Around<br />Your Operation</h2>
          <p className="delivery-services-description">Whether you're a farmer, contractor, or business owner, we make it easy to get your equipment delivered anywhere in the United States. We work with trusted, experienced carriers to ensure your equipment arrives safely and on time.</p>
        </div>
        <img
          className="delivery-services-image"
          src="/images/delivery-services-tractor.webp"
          alt="Green farm tractors secured on a flatbed trailer for delivery"
          loading="lazy"
          decoding="async"
        />
      </div>
      <div className="delivery-services-benefits">
        <article>
          <FaTruck aria-hidden="true" />
          <div><h3>Nationwide Coverage</h3><p>Delivery to all 50 states with reliable carriers.</p></div>
        </article>
        <article>
          <FaShieldAlt aria-hidden="true" />
          <div><h3>Safe &amp; Insured Transport</h3><p>Your equipment is handled by professionals, experienced carriers.</p></div>
        </article>
        <article>
          <FaClock aria-hidden="true" />
          <div><h3>Competitive Rates</h3><p>We work with multiple carriers to get the best freight rates.</p></div>
        </article>
        <article>
          <FaCalendarAlt aria-hidden="true" />
          <div><h3>Flexible Scheduling</h3><p>We’ll coordinate pickup and delivery at a time that works for you.</p></div>
        </article>
      </div>
    </section>
    <section className="delivery-quote-banner" aria-labelledby="delivery-quote-title">
      <div className="delivery-quote-panel">
        <h2 id="delivery-quote-title">Get a Delivery Quote</h2>
        <p className="delivery-quote-description">Call us or fill out a short form and we’ll get you a freight quote as soon as possible.</p>
        <div className="delivery-quote-actions">
          <Link className="delivery-quote-button delivery-quote-button--primary" to="/contact">
            Request a Quote <FaArrowRight aria-hidden="true" />
          </Link>
          <a className="delivery-quote-button delivery-quote-button--phone" href={business.phoneHref} onClick={() => trackContactCta('phone_click', 'Delivery Quote Banner Call')}>
            <FaPhoneAlt aria-hidden="true" /> {business.phone}
          </a>
        </div>
      </div>
    </section>
    <section className="delivery-process" aria-labelledby="delivery-process-title">
      <div className="delivery-process-inner">
        <h2 id="delivery-process-title">A Simple Process</h2>
        <ol className="delivery-process-steps">
          <li>
            <span className="delivery-process-number" aria-hidden="true">01</span>
            <div><h3>Request a Quote</h3><p>Get in touch with the equipment you're interested in and your delivery location.</p></div>
          </li>
          <li>
            <span className="delivery-process-number" aria-hidden="true">02</span>
            <div><h3>Get a Freight Rate</h3><p>We’ll get you a competitive shipping quote from our trusted carriers.</p></div>
          </li>
          <li>
            <span className="delivery-process-number" aria-hidden="true">03</span>
            <div><h3>Schedule Delivery</h3><p>Once you approve the quote, we’ll arrange pickup and delivery at a time that works for you.</p></div>
          </li>
          <li>
            <span className="delivery-process-number" aria-hidden="true">04</span>
            <div><h3>Receive Your Equipment</h3><p>Your equipment is delivered safely to your location, ready to get to work.</p></div>
          </li>
        </ol>
      </div>
    </section>
    <section className="delivery-types" aria-label="Delivery equipment categories">
      <div className="delivery-types-inner">
        <div className="delivery-types-grid">
          <article className="delivery-type-card">
            <img src="/images/delivery-type-tractor.webp" alt="Green farm tractor secured on a flatbed trailer at an equipment dealership" loading="lazy" decoding="async" />
            <div><h2>Tractors</h2><p>Compact, utility and ag tractors delivered to your location.</p></div>
          </article>
          <article className="delivery-type-card">
            <img src="/images/delivery-type-skid-steer.webp" alt="Compact tracked skid steer secured on a trailer for delivery" loading="lazy" decoding="async" />
            <div><h2>Skid Steers</h2><p>Skid steers and compact track loaders, safely transported.</p></div>
          </article>
          <article className="delivery-type-card">
            <img src="/images/delivery-type-implements.webp" alt="Green agricultural planter secured on a flatbed trailer" loading="lazy" decoding="async" />
            <div><h2>Implements</h2><p>Tillers, discs, mowers and other implements delivered nationwide.</p></div>
          </article>
        </div>
      </div>
    </section>
  </main>
)
