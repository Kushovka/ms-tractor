import {
  FaArrowRight,
  FaCalendarAlt,
  FaCheckCircle,
  FaClock,
  FaDollarSign,
  FaFileAlt,
  FaTachometerAlt,
  FaShieldAlt,
  FaTruck,
} from 'react-icons/fa'
import { Link } from 'react-router'
import { Seo } from '../components/Seo'
import { business } from '../data/business'

const returnHighlights = [
  { icon: FaCalendarAlt, title: '72-Hour Return Period', text: 'The return period begins when the delivery paperwork is signed and the vehicle is received.' },
  { icon: FaTachometerAlt, title: '250-Mile Additional Miles', text: 'You may drive up to 250 additional miles during the 72-hour period to properly evaluate the vehicle.' },
  { icon: FaFileAlt, title: 'Written Warranty Included', text: 'Qualifying vehicles include written warranty documentation provided at the time of sale.' },
  { icon: FaTruck, title: 'Seller-Paid Return Transport', text: 'For qualifying returns, we arrange and pay for return transportation under the written policy.' },
]

const steps = [
  ['Notify Us', 'Contact us within 72 hours of delivery and before exceeding 250 additional miles to let us know you would like to return the vehicle.'],
  ['Vehicle Inspection', 'Once the vehicle is returned, we inspect it to confirm it meets the return policy conditions.'],
  ['Return Transport', 'We arrange and pay for return transportation for qualifying returns.'],
  ['Refund Processing', 'After inspection is complete and the vehicle meets the policy conditions, we process your refund according to the terms of sale.'],
]

const conditions = [
  'No new damage beyond normal wear and tear',
  'No modifications or unauthorized changes',
  'Not driven more than 250 additional miles',
  'No abuse, neglect, or misuse',
  'All original equipment and included items returned',
  'Vehicle meets the conditions in the written return policy',
]

const keyPoints = [
  [FaClock, '72-hour return period from delivery'],
  [FaTachometerAlt, '250-mile additional driving limit'],
  [FaTruck, 'Seller-arranged and paid return transport for qualifying returns'],
  [FaFileAlt, 'Written warranty included for qualifying vehicles'],
  [FaShieldAlt, 'Clean title documentation provided'],
  [FaDollarSign, 'Upfront pricing with no hidden fees'],
] as const

export const GuaranteePage = () => (
  <div className="guarantee-page">
    <Seo title="72-Hour / 250-Mile Money-Back Guarantee" description={`Review the return policy, process, and conditions for qualifying vehicles at ${business.name}. Written purchase and return documents control eligibility.`} />

    <section className="guarantee-hero" aria-labelledby="guarantee-title">
      <div className="guarantee-hero-copy">
        <h1 id="guarantee-title">72-Hour / 250-Mile<br />Money Back Guarantee</h1>
        <p>We want you to be completely satisfied with your purchase. That’s why qualifying vehicles include a 72-hour / 250-mile return policy and written warranty. We stand behind our vehicles and believe in honest deals, clear pricing, and no hidden fees.</p>
        <div className="guarantee-actions">
          <a className="guarantee-button guarantee-button--red" href="#return-conditions">View Return Policy Details <FaArrowRight aria-hidden="true" /></a>
          <Link className="guarantee-button guarantee-button--light" to="/inventory">Shop Our Inventory <FaArrowRight aria-hidden="true" /></Link>
        </div>
      </div>
    </section>

    <section className="guarantee-section guarantee-how" aria-labelledby="guarantee-how-title">
      <h2 id="guarantee-how-title">72 Hours and 250 Miles to Make Sure It Is Right for You</h2>
      <p className="guarantee-section-intro">Take time to drive, inspect, and make sure the vehicle meets your needs. If it’s not the right fit, qualifying vehicles may be returned within 72 hours or 250 additional miles, whichever limit is reached first, under our written return policy.</p>
      <div className="guarantee-highlight-grid">
        {returnHighlights.map(({ icon: Icon, title, text }) => <article className="guarantee-highlight" key={title}><Icon aria-hidden="true" /><div><h3>{title}</h3><p>{text}</p></div></article>)}
      </div>
    </section>

    <section className="guarantee-promise" aria-labelledby="guarantee-promise-title">
      <img src="/images/warranty-truck.webp" alt="A vehicle at M & S Tractor & Equipment, with the dealership in the background" />
      <div className="guarantee-promise-copy">
        <h2 id="guarantee-promise-title">Upfront Pricing. No Hidden Fees.</h2>
        <p>We believe car buying should be simple and transparent. Our vehicles are priced clearly and include all available information about the vehicle’s history, condition, and documentation.</p>
        <div className="guarantee-docs">
          <article><FaFileAlt aria-hidden="true" /><div><h3>Vehicle Documentation</h3><p>We provide available documentation, including vehicle history reports and warranty information, so you can make an informed decision.</p></div></article>
          <article><FaShieldAlt aria-hidden="true" /><div><h3>Clean Title Documentation</h3><p>Qualifying vehicles are sold with clean title documentation. We provide the necessary title documents and handle the paperwork transparently.</p></div></article>
        </div>
      </div>
    </section>

    <section className="guarantee-section guarantee-process" aria-labelledby="guarantee-process-title">
      <h2 id="guarantee-process-title">Clear Steps From Notice to Inspection</h2>
      <p className="guarantee-section-intro">Our return process is straightforward and designed to be fair for both you and our dealership.</p>
      <div className="guarantee-steps">
        {steps.map(([title, text], index) => <article key={title}><span>{index + 1}</span><div><h3>{title}</h3><p>{text}</p></div></article>)}
      </div>
    </section>

    <section className="guarantee-commitment">
      <div className="guarantee-commitment-inner">
        <div><h2>A Better Car Buying Experience<br />for Our Customers</h2><p>We’re a locally owned dealership in Shreveport, LA. Our goal is simple: honest vehicles, clear information, and a fair buying experience. If you have questions about our money-back guarantee, our team is here to help.</p></div>
        <div className="guarantee-commitment-actions"><Link className="guarantee-button guarantee-button--red" to="/inventory">Shop Our Inventory <FaArrowRight aria-hidden="true" /></Link><Link className="guarantee-button guarantee-button--outline" to="/contact"><FaFileAlt aria-hidden="true" /> Ask a Question <FaArrowRight aria-hidden="true" /></Link></div>
      </div>
    </section>

    <section className="guarantee-terms" id="return-conditions" aria-label="Return conditions and key points">
      <article className="guarantee-conditions">
        <h2>Protecting the Vehicle During Evaluation</h2>
        <p>To be eligible for a return, the vehicle must be in substantially the same condition as when it was delivered, subject to the following:</p>
        <ul>{conditions.map((condition) => <li key={condition}><FaCheckCircle aria-hidden="true" />{condition}</li>)}</ul>
      </article>
      <article className="guarantee-keypoints">
        <h2>Simple Terms. Clear Expectations.</h2>
        <p>Our 72-hour / 250-mile money-back guarantee is designed to give you confidence and peace of mind when you buy from M &amp; S Tractor &amp; Equipment.</p>
        <ul>{keyPoints.map(([Icon, text]) => <li key={text}><Icon aria-hidden="true" />{text}</li>)}</ul>
        <p className="guarantee-terms-note">Eligibility, inspection requirements, exclusions, refund timing, and other conditions are governed by the signed purchase documents and written return policy.</p>
      </article>
    </section>

  </div>
)
