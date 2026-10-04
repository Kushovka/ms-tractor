import { FaArrowRight, FaClock, FaEnvelope, FaMapMarkerAlt, FaPhoneAlt } from 'react-icons/fa'
import { LeadForm } from '../components/LeadForm'
import { HeroScrollCue } from '../components/HeroScrollCue'
import { Seo } from '../components/Seo'
import { business } from '../data/business'
import { trackContactCta } from '../utils/ctaTracking'

const phoneHref = business.phoneHref || business.contactHref
const faqs = [
  { question: 'Do you offer equipment delivery?', answer: 'Yes. Contact our team with the equipment and destination details for a delivery quote.' },
  { question: 'What areas do you serve?', answer: 'We are based in Shreveport, Louisiana. Call us to discuss delivery and service availability for your area.' },
  { question: 'Can I schedule a service appointment online?', answer: 'Send us a message with your equipment and service needs, or call us to schedule an appointment.' },
]

export const ContactPage = () => (
  <main className="contact-page">
    <Seo title="Contact" description="Call, visit, or send a message to M & S Tractor & Equipment in Shreveport, LA." />

    <section id="contact-form" className="contact-hero" aria-labelledby="contact-hero-title">
      <div className="contact-container contact-hero-layout">
        <div className="contact-hero-content">
          <h1 id="contact-hero-title">We’re here<br />to help</h1>
          <p>Have a question about equipment, parts, service, or delivery?<br className="contact-wide-break" /> Our team is ready to help. Reach out, give us a call, or stop by<br className="contact-wide-break" /> our dealership in Shreveport, Louisiana.</p>
        </div>
        <div className="contact-message contact-hero-form">
          <h2>Contact Form</h2>
          <LeadForm title="Send Message" variant="contact" markRequiredNameFields phonePlaceholder="Phone number*" messagePlaceholder="Tell us a little more..." inquiryOptions={['Equipment questions', 'Parts & service', 'Delivery', 'Schedule a visit', 'Other']} />
        </div>
      </div>
      <HeroScrollCue target="contact-details" label="Scroll to contact information" />
    </section>

    <section id="contact-details" className="contact-main" aria-label="Contact information">
      <div className="contact-container contact-main-grid">
        <div className="contact-information">
          <h2>Contact Information</h2>
          <p className="contact-intro">You can reach us by phone, email, or visit our dealership in person. We’re happy to answer your questions and help you find the right equipment for your needs.</p>
          <div className="contact-facts">
            <div className="contact-fact"><span className="contact-fact-icon"><FaPhoneAlt aria-hidden="true" /></span><div><h3>Call us</h3><a className="contact-fact-value" href={phoneHref} onClick={() => trackContactCta('phone_click', 'Contact Page Call')}>{business.phone}</a><p>Talk with our team about equipment, parts, and service.</p></div></div>
            <div className="contact-fact"><span className="contact-fact-icon"><FaMapMarkerAlt aria-hidden="true" /></span><div><h3>Visit our dealership</h3><p>{business.address}<br />{business.cityState} {business.postalCode}</p><a className="contact-inline-link" href={business.mapsUrl} target="_blank" rel="noreferrer" onClick={() => trackContactCta('directions_click', 'Contact Page Address')}>Get directions <FaArrowRight aria-hidden="true" /></a></div></div>
            <div className="contact-fact"><span className="contact-fact-icon"><FaClock aria-hidden="true" /></span><div><h3>Hours</h3><p>Mon - Fri: 8:00 AM - 5:00 PM<br />Sat: 8:00 AM - 12:00 PM<br />Sun: Closed</p></div></div>
            <div className="contact-fact"><span className="contact-fact-icon"><FaEnvelope aria-hidden="true" /></span><div><h3>Email us</h3><a className="contact-fact-value" href="mailto:sales@ms-tractor.com">sales@ms-tractor.com</a><p>We’ll get back to you as soon as possible.</p></div></div>
          </div>
        </div>

      </div>
    </section>

    <section className="contact-location" aria-labelledby="location-heading">
      <div className="contact-container">
        <div className="contact-map-panel">
          <div className="contact-location-card">
            <p className="contact-eyebrow"><i /> Our location</p>
            <h2 id="location-heading">Find us in<br />Shreveport, LA</h2>
            <p><FaMapMarkerAlt aria-hidden="true" /> <span>{business.address}<br />{business.cityState} {business.postalCode}</span></p>
            <a href={business.mapsUrl} target="_blank" rel="noreferrer" onClick={() => trackContactCta('directions_click', 'Contact Page Map Directions')}>Get directions <FaArrowRight aria-hidden="true" /></a>
          </div>
          <iframe title="Satellite map showing M & S Tractor & Equipment" className="contact-map" loading="lazy" referrerPolicy="no-referrer-when-downgrade" src={business.mapEmbedUrl} />
        </div>

        <div className="contact-lower-grid">
          <img className="contact-dealership-photo" src="/images/contact-service-photo.webp" alt="A dealership technician discussing a green tractor with its owner" loading="lazy" />
          <div className="contact-faq">
            <h2>Frequently Asked Questions</h2>
            <div className="contact-faq-list">{faqs.map(({ question, answer }) => <details key={question}><summary>{question}<span aria-hidden="true" /></summary><p>{answer}</p></details>)}</div>
          </div>
        </div>
      </div>
    </section>
  </main>
)
