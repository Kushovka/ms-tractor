import { FaArrowRight, FaHandshake, FaMapMarkerAlt, FaUsers, FaCog } from 'react-icons/fa'
import { Link } from 'react-router'
import { HeroScrollCue } from '../components/HeroScrollCue'
import { Seo } from '../components/Seo'
import { business } from '../data/business'

const values = [
  { icon: FaHandshake, title: 'Family owned & operated', text: 'A local team that values honest work and long-term relationships.' },
  { icon: FaUsers, title: 'Experienced team', text: 'We know equipment and we’re here to help you find the right solution.' },
  { icon: FaCog, title: 'Parts & service support', text: 'Keep your equipment running with quality parts and experienced technicians.' },
  { icon: FaMapMarkerAlt, title: 'Serving the region', text: 'Proudly serving Louisiana, East Texas, and surrounding communities.' },
]

export const AboutPage = () => (
  <div className="about-page">
    <Seo title="About M & S Tractor & Equipment" description="Meet M & S Tractor & Equipment, serving farmers, landowners, and contractors in Shreveport, Louisiana." />
    <section className="about-hero">
      <div className="about-hero-copy">
        <h1>A local company<br />that works for you</h1>
        <p>M&amp;S Tractor &amp; Equipment is a family-owned business based in Shreveport, Louisiana. We’re here to help farmers, landowners, and contractors get the equipment, parts, and service they need to keep moving.</p>
        <div className="about-actions"><Link className="about-button about-button--red" to="/inventory">Our inventory <FaArrowRight /></Link></div>
      </div>
      <HeroScrollCue target="about-story" label="Scroll to our story" />
    </section>
    <section id="about-story" className="about-story">
      <div className="about-story-copy"><h2>Rooted in<br />North Louisiana</h2>
        <p>M&amp;S Tractor &amp; Equipment was founded with a simple goal - to provide reliable equipment, honest service, and real support to the people who work the land. What started as a local business has grown into a trusted dealer serving customers across Louisiana, East Texas, and beyond.</p>
        <p>We understand the challenges that come with farming, land management, and construction, because we live and work in the same communities as our customers. That’s why we focus on building long-term relationships and being a partner you can count on.</p>
      </div>
      <img src="/images/about-north-louisiana.webp" alt="Orange utility tractor beside a rural field in North Louisiana at sunset" />
    </section>
    <section className="about-values" aria-label="What you can expect"><div className="about-values-grid">
      {values.map(({ icon: Icon, title, text }) => <article key={title}><Icon aria-hidden="true" /><div><h2>{title}</h2><p>{text}</p></div></article>)}
    </div></section>
    <section className="about-why">
      <div className="about-mission-media"><img className="about-mission-image" src="/images/about-mission-workshop.webp" alt="M&S mechanic servicing a green utility tractor inside the workshop" /></div>
      <div className="about-why-copy"><h2>Keeping you<br />in the field</h2>
        <p>Our mission is to deliver the equipment, parts, and support that help our customers get the job done. We stand behind what we sell and work hard to make sure you have a positive experience every time you work with us.</p>
        <Link className="about-button about-button--red" to="/contact">Contact our team <FaArrowRight /></Link>
      </div>
    </section>
    <section className="about-location">
      <div className="about-location-copy"><h2>Visit our dealership</h2>
        <p>Stop by our location in Shreveport, Louisiana to see our current inventory, get parts, or talk with our team. We’re here to help.</p>
        <a className="about-button" href={business.mapsUrl} target="_blank" rel="noreferrer">Get directions <FaArrowRight /></a>
      </div>
      <div className="about-gallery">
        <img src="/images/about-dealership-front.webp" alt="Orange compact tractors outside a green equipment service building" loading="lazy" />
        <img src="/images/about-equipment-detail.webp" alt="Compact tractors and farm implements on the dealership lot" loading="lazy" />
        <img src="/images/about-service-workshop.webp" alt="Mechanic servicing a tractor inside an equipment workshop" loading="lazy" />
      </div>
    </section>
  </div>
)
