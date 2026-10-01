import { Link } from 'react-router'
import { FaClock, FaMapMarkerAlt, FaPhoneAlt } from 'react-icons/fa'

import { business } from '../data/business'
import { trackContactCta } from '../utils/ctaTracking'

const equipmentLinks = [
  ['New Equipment', '/inventory?q=tractor'],
  ['Used Equipment', '/inventory?q=tractor'],
  ['Tractors', '/inventory?q=tractor'],
  ['Implements', '/inventory?q=implement'],
  ['Mowers', '/inventory?q=mower'],
  ['Trailers', '/inventory?q=trailer'],
]

const serviceLinks = [
  ['Parts Department', '/contact#contact-form'],
  ['Service Department', '/#parts-service-title'],
  ['Contact Us', '/contact#contact-form'],
]

const aboutLinks = [
  ['About Us', '/about'],
  ['Our Team', '/team'],
  ['Privacy Policy', '/privacy-policy'],
]

export const Footer = () => (
  <footer className="home-footer">
    <div className="home-footer-container">
      <div className="home-footer-main">
        <nav className="home-footer-column" aria-label="Equipment inventory links">
          <h2>Inventory</h2><i />
          {equipmentLinks.map(([label, href]) => <Link to={href} key={label}>{label}</Link>)}
        </nav>
        <nav className="home-footer-column" aria-label="Sales and service links">
          <h2>Sales &amp; Service</h2><i />
          {serviceLinks.map(([label, href]) => <Link to={href} key={label}>{label}</Link>)}
          <a href={business.mapsUrl} target="_blank" rel="noreferrer" onClick={() => trackContactCta('directions_click', 'Footer Directions Link')}>Directions</a>
        </nav>
        <nav className="home-footer-column" aria-label="About M & S links">
          <h2>About</h2><i />
          {aboutLinks.map(([label, href]) => <Link to={href} key={href}>{label}</Link>)}
        </nav>

        <section className="home-footer-contact" aria-labelledby="home-footer-contact-title">
          <h2 id="home-footer-contact-title">Contact Information</h2><i />
          <a href={business.phoneHref} className="home-footer-contact__row" onClick={() => trackContactCta('phone_click', 'Footer Contact Phone')}>
            <FaPhoneAlt aria-hidden="true" /><span>{business.phone.replace('+1 ', '')}</span>
          </a>
          <a href={business.mapsUrl} target="_blank" rel="noreferrer" className="home-footer-contact__row" onClick={() => trackContactCta('directions_click', 'Footer Contact Address')}>
            <FaMapMarkerAlt aria-hidden="true" /><span>{business.address}<br />{business.cityState} {business.postalCode}</span>
          </a>
          <div className="home-footer-contact__row home-footer-contact__hours">
            <FaClock aria-hidden="true" />
            <span><strong>Hours</strong><br />Mon-Fri: 8:00 AM–5:00 PM<br />Sat: 8:00 AM–12:00 PM<br />Sun: Closed</span>
          </div>
        </section>

        <section className="home-footer-intro" aria-label="M & S Tractor & Equipment">
          <Link to="/" className="home-footer-logo"><img src="/images/ms-tractor-logo.webp" alt="M & S Tractor & Equipment" /></Link>
          <p>New &amp; used tractors, implements, mowers, trailers and equipment. Parts, service and local support in Shreveport, Louisiana.</p>
        </section>
      </div>

      <div className="home-footer-bottom">
        <span>© 2026 M &amp; S Tractor &amp; Equipment. All rights reserved.</span>
        <i aria-hidden="true" />
        <div><Link to="/contact">Contact Us</Link><Link to="/privacy-policy">Privacy Policy</Link><Link to="/terms">Terms of Service</Link></div>
      </div>
    </div>
  </footer>
)
