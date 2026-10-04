import { FaArrowRight, FaBan, FaPaintBrush, FaTint, FaWrench } from 'react-icons/fa'
import { HeroScrollCue } from '../components/HeroScrollCue'
import { LeadForm } from '../components/LeadForm'
import { Seo } from '../components/Seo'
import { business } from '../data/business'

const exclusions = [
  { icon: FaWrench, title: 'Wear & Maintenance', text: 'Normal wear items and routine maintenance are not covered.' },
  { icon: FaTint, title: 'Consumable Components', text: 'Consumable components are excluded from coverage.' },
  { icon: FaPaintBrush, title: 'Cosmetic & Accessories', text: 'Cosmetic items and add-on accessories are not covered.' },
  { icon: FaBan, title: 'Misuse or Modifications', text: 'Damage from misuse, abuse, or unauthorized modifications is excluded.' },
]

export const WarrantyPage = () => (
  <>
    <Seo title="Warranty information" description={`Review limited warranty information and contact ${business.name} for coverage details on a specific tractor or piece of equipment.`} />
    <main className="warranty-page">
      <section className="warranty-hero" aria-labelledby="warranty-title">
        <div className="warranty-hero-copy">
          <h1 id="warranty-title">90-Day / 300-Hour<br />Limited Warranty</h1>
          <p className="warranty-hero-lead">In addition to our return policy, qualifying tractors and equipment include a limited warranty for major mechanical components. Coverage begins at delivery and ends after 90 calendar days or 300 operating hours, whichever comes first.</p>
          <div className="warranty-hero-actions">
            <a className="delivery-button delivery-button--primary warranty-ask-button" href="/contact">Ask About Coverage <FaArrowRight aria-hidden="true" /></a>
            <a className="delivery-button delivery-button--phone warranty-call-button" href={business.phoneHref}>Call {business.phone} <FaArrowRight aria-hidden="true" /></a>
          </div>
        </div>
        <HeroScrollCue target="warranty-reference-section" label="Scroll to warranty details" />
      </section>

      <section id="warranty-reference-section" className="warranty-reference-section" aria-label="Warranty limitations and coverage options">
        <div className="warranty-reference-inner">
          <div className="warranty-reference-exclusions">
            <div className="warranty-reference-heading">
              <h2>Important Limitations &amp; Exclusions</h2>
            </div>
            <div className="warranty-reference-exclusion-grid">
              {exclusions.map(({ icon: Icon, title, text }) => (
                <article className="warranty-reference-exclusion" key={title}>
                  <Icon aria-hidden="true" />
                  <div><h3>{title}</h3><p>{text}</p></div>
                </article>
              ))}
            </div>
          </div>

          <div className="warranty-reference-coverage">
            <article className="warranty-reference-coverage-card">
              <img src="/images/warranty-factory-coverage.webp" alt="Green utility tractor with front loader on a Louisiana farm" loading="lazy" />
              <div className="warranty-reference-coverage-copy">
                <span aria-hidden="true" />
                <h2>Factory Warranty Coverage</h2>
                <p>Some new tractors and equipment may include manufacturer warranty coverage. Terms and duration vary by make, model, and in-service date. Our team can help confirm remaining coverage on eligible equipment.</p>
              </div>
            </article>
            <article className="warranty-reference-coverage-card">
              <img src="/images/warranty-extended-options.webp" alt="Service technician inspecting a green utility tractor in a workshop" loading="lazy" />
              <div className="warranty-reference-coverage-copy">
                <span aria-hidden="true" />
                <h2>Extended Warranty Options</h2>
                <p>Additional protection plans may be available for qualifying equipment. Ask our team about current options, coverage levels, and terms for the tractor or implement you’re considering.</p>
              </div>
            </article>
          </div>
        </div>
      </section>

      <section className="warranty-inquiry" aria-labelledby="warranty-inquiry-title">
        <div className="warranty-inquiry-media">
          <img src="/images/warranty-inquiry-dealership.webp" alt="A dealership technician inspecting a green tractor outside the service workshop" loading="lazy" />
        </div>
        <div className="warranty-inquiry-content">
          <div className="warranty-inquiry-intro">
            <span aria-hidden="true" />
            <h2 id="warranty-inquiry-title">Warranty Inquiry</h2>
            <p>Have questions about warranty coverage? Reach out and our team will be happy to help.</p>
          </div>
          <LeadForm
            title="Ask About Coverage"
            className="warranty-inquiry-form"
            markRequiredNameFields
            phonePlaceholder="Phone*"
            messagePlaceholder="Tell us about your equipment or question"
          />
        </div>
      </section>
    </main>
  </>
)
