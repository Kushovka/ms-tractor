import { useEffect, useRef, useState } from 'react'
import { Link } from 'react-router'
import { FaArrowLeft, FaArrowRight, FaClock, FaEnvelope, FaMapMarkerAlt, FaPhoneAlt, FaWrench, FaCog } from 'react-icons/fa'
import { listEquipment } from '../api/equipment'
import { EquipmentCard } from '../components/EquipmentCard'
import { Seo } from '../components/Seo'
import { business } from '../data/business'
import type { Equipment } from '../types/equipment'
import { trackContactCta } from '../utils/ctaTracking'
import { localBusinessSchema } from '../utils/schema'

export const HomePage = () => {
  const [equipment, setEquipment] = useState<Equipment[]>([])
  const [inventoryLoaded, setInventoryLoaded] = useState(false)
  const desktopInventoryTrackRef = useRef<HTMLDivElement>(null)
  const mobileInventoryTrackRef = useRef<HTMLDivElement>(null)

  const scrollInventory = (direction: -1 | 1) => {
    const track = window.matchMedia('(min-width: 901px)').matches
      ? desktopInventoryTrackRef.current
      : mobileInventoryTrackRef.current
    const firstCard = track?.firstElementChild
    if (!track || !firstCard) return
    const gap = Number.parseFloat(window.getComputedStyle(track).columnGap) || 0
    track.scrollBy({ left: direction * (firstCard.getBoundingClientRect().width + gap), behavior: 'smooth' })
  }

  useEffect(() => {
    let cancelled = false
    listEquipment({ page: 1, pageSize: 50, sort: 'year_desc' })
      .then((response) => { if (!cancelled) setEquipment(response.items) })
      .catch(() => { if (!cancelled) setEquipment([]) })
      .finally(() => { if (!cancelled) setInventoryLoaded(true) })
    return () => { cancelled = true }
  }, [])

  const desktopTractors = equipment.filter((item) => item.bodyType.toLowerCase().includes('tractor')).slice(0, 6)
  const mobileEquipment = equipment.slice(0, 4)

  return <>
    <Seo
      title="M & S Tractor & Equipment | Shreveport, LA"
      description="Shop tractors, implements, mowers, trailers, and agricultural equipment at M & S Tractor & Equipment in Shreveport, Louisiana."
      schema={localBusinessSchema}
    />

    <div className="dealer-home">
      <section className="dealer-hero" aria-label="M & S Tractor & Equipment dealership">
        <img
          src="/images/ms-tractor-home-hero.webp"
          alt="M & S Tractor & Equipment facility and equipment yard in Shreveport, Louisiana"
          fetchPriority="high"
          decoding="async"
        />
        <div className="dealer-hero__content">
          <p className="store-summary__location">Shreveport, Louisiana</p>
          <h1 id="store-summary-title">M<span className="store-summary__brand-space">&nbsp;</span>&amp;<span className="store-summary__brand-space">&nbsp;</span>S Tractor &amp; Equipment</h1>
          <p className="store-summary__description">New &amp; used tractors, implements, mowers, trailers and equipment. Parts · Service · Local support</p>
        </div>
      </section>

      <section id="current-inventory-carousel" className="equipment-inventory" aria-labelledby="equipment-inventory-title">
        <div className="equipment-inventory__heading">
          <h2 id="equipment-inventory-title">Current Inventory</h2>
          {equipment.length ? <div className="equipment-inventory__controls" aria-label="Inventory carousel controls">
            <button type="button" onClick={() => scrollInventory(-1)} aria-label="Previous inventory items" aria-controls="current-inventory-carousel"><FaArrowLeft aria-hidden="true" /></button>
            <button type="button" onClick={() => scrollInventory(1)} aria-label="Next inventory items" aria-controls="current-inventory-carousel"><FaArrowRight aria-hidden="true" /></button>
          </div> : null}
        </div>
        {equipment.length ? <>
          <div className="equipment-inventory__carousel equipment-inventory__carousel--desktop" ref={desktopInventoryTrackRef} aria-label="Six current tractors">
            {desktopTractors.map((item) => <EquipmentCard equipment={item} key={item.id} />)}
            <Link to="/inventory" className="equipment-inventory__view-all">
              <span>Browse all equipment</span>
              <strong>View All Inventory</strong>
              <FaArrowRight aria-hidden="true" />
            </Link>
          </div>
          <div className="equipment-inventory__carousel equipment-inventory__carousel--mobile" ref={mobileInventoryTrackRef} aria-label="Current equipment inventory">
            {mobileEquipment.map((item) => <EquipmentCard equipment={item} key={item.id} />)}
            <Link to="/inventory" className="equipment-inventory__view-all">
              <span>Browse all equipment</span>
              <strong>View All Inventory</strong>
              <FaArrowRight aria-hidden="true" />
            </Link>
          </div>
        </> : <div className="equipment-inventory__empty">
          <p>{inventoryLoaded ? 'Inventory is temporarily unavailable.' : 'Loading current inventory…'}</p>
          <a href={business.phoneHref} onClick={() => trackContactCta('phone_click', 'Home Inventory Availability')}>{business.phone} <FaArrowRight aria-hidden="true" /></a>
        </div>}
      </section>
      <section className="parts-service" aria-labelledby="parts-service-title">
        <div className="parts-service__inner">
          <div className="parts-service__photo">
            <img src="/images/ms-tractor-service.webp" alt="Technician servicing a tractor inside an agricultural equipment workshop" loading="lazy" />
          </div>
          <div className="parts-service__content">
            <div className="parts-service__eyebrow"><span>Parts &amp; Service</span><i /></div>
            <h2 id="parts-service-title">Parts, Service &amp; Support<br className="hidden xl:block" /> for Working Equipment</h2>
            <p className="parts-service__intro">Get the parts you need and service that keeps your equipment working. Parts for tractors, implements, mowers and equipment. Routine service, repairs and support for the equipment you use.</p>
            <div className="parts-service__departments">
              <article>
                <FaCog aria-hidden="true" />
                <div><h3>Parts Department</h3><p>Stocking quality parts for tractors, implements, mowers and equipment. We can help you find the right part and get you back to work.</p></div>
              </article>
              <article>
                <FaWrench aria-hidden="true" />
                <div><h3>Service Department</h3><p>Routine service, repairs and support from experienced technicians. We service what we sell and many other makes and models.</p></div>
              </article>
            </div>
            <div className="parts-service__contact">
              <a href={business.phoneHref} onClick={() => trackContactCta('phone_click', 'Parts Service Call')}>
                <FaPhoneAlt aria-hidden="true" /><span><strong>Call Us</strong><b>{business.phone}</b><small>Talk with our parts and service team.</small></span>
              </a>
              <Link to="/contact#contact-form" onClick={() => trackContactCta('contact_form_click', 'Parts Service Contact')}>
                <FaEnvelope aria-hidden="true" /><span><strong>Contact Us <FaArrowRight aria-hidden="true" /></strong><small>Send us a message about parts or service.</small></span>
              </Link>
              <a href={business.mapsUrl} target="_blank" rel="noreferrer" onClick={() => trackContactCta('directions_click', 'Parts Service Directions')}>
                <FaMapMarkerAlt aria-hidden="true" /><span><strong>Get Directions <FaArrowRight aria-hidden="true" /></strong><small>{business.address}<br />{business.cityState} {business.postalCode}</small></span>
              </a>
            </div>
          </div>
        </div>
      </section>
      <section className="tractor-guide" aria-labelledby="tractor-guide-title">
        <div className="tractor-guide__inner">
          <div className="tractor-guide__photo">
            <img src="/images/tractor-buying-guide.webp" alt="Green tractors with front loaders displayed at an equipment dealership" loading="lazy" />
          </div>
          <div className="tractor-guide__main">
            <div className="tractor-guide__eyebrow"><span>Tractor Buying Guide</span><i /></div>
            <h2 id="tractor-guide-title">Find the Right<br className="tractor-guide__desktop-break" /> Tractor for the Job</h2>
            <p className="tractor-guide__intro"><strong>Every property and job is different.</strong> We’ll help you find a tractor that fits your needs, whether you’re working on a small acreage, maintaining your property or handling daily work on the farm.</p>
            <div className="tractor-guide__actions">
              <Link to="/inventory?q=tractor" onClick={() => trackContactCta('inventory_click', 'Tractor Buying Guide Browse')} className="tractor-guide__button tractor-guide__button--primary">Browse Current Tractors <FaArrowRight aria-hidden="true" /></Link>
              <a href={business.phoneHref} onClick={() => trackContactCta('phone_click', 'Tractor Buying Guide Call')} className="tractor-guide__button">Call Our Team <FaArrowRight aria-hidden="true" /></a>
            </div>
          </div>
          <ol className="tractor-guide__steps">
            <li><span className="tractor-guide__number">01</span><div><h3>Property Size</h3><p>Small acreage, larger property or farm use.</p></div></li>
            <li><span className="tractor-guide__number">02</span><div><h3>Horsepower</h3><p>Match the tractor to the work you actually need to do.</p></div></li>
            <li><span className="tractor-guide__number">03</span><div><h3>Loader &amp; Attachments</h3><p>Consider lifting, mowing, grading and material handling.</p></div></li>
            <li><span className="tractor-guide__number">04</span><div><h3>Cab or Open Station</h3><p>Choose the setup that fits your work and comfort needs.</p></div></li>
          </ol>
        </div>
      </section>
      <section className="home-location" aria-labelledby="home-location-title">
        <div className="home-location__inner">
          <div className="home-location__details">
            <div className="home-location__eyebrow"><span>Location</span><i /></div>
            <h2 id="home-location-title">Visit M &amp; S</h2>
            <p className="home-location__intro">Stop by our location in Shreveport, Louisiana. We’re here to help with equipment, parts, service and any questions you may have.</p>

            <div className="home-location__fact">
              <FaMapMarkerAlt aria-hidden="true" className="home-location__icon home-location__icon--pin" />
              <div><h3>Address</h3><p>{business.address}<br />{business.cityState} {business.postalCode}</p><a href={business.mapsUrl} target="_blank" rel="noreferrer" onClick={() => trackContactCta('directions_click', 'Home Location Directions')}>Get directions <FaArrowRight aria-hidden="true" /></a></div>
            </div>
            <div className="home-location__fact">
              <FaClock aria-hidden="true" className="home-location__icon" />
              <div><h3>Hours</h3><p>Mon - Fri: 8:00 AM - 5:00 PM<br />Sat: 8:00 AM - 12:00 PM<br />Sun: Closed</p></div>
            </div>
            <a href={business.phoneHref} className="home-location__fact home-location__fact--call" onClick={() => trackContactCta('phone_click', 'Home Location Call')}>
              <FaPhoneAlt aria-hidden="true" className="home-location__icon" />
              <div><h3>Call Us</h3><strong>{business.phone}</strong><p>Talk with our team about<br />equipment, parts, and service.</p></div>
            </a>
          </div>

          <div className="home-location__media">
            <img className="home-location__photo" src={business.heroImage} alt="M & S Tractor & Equipment dealership and tractor yard in Shreveport, Louisiana" loading="lazy" />
            <iframe title="Map to M & S Tractor & Equipment at 3221 Forge Road in Shreveport" className="home-location__map" loading="lazy" referrerPolicy="no-referrer-when-downgrade" src={business.mapEmbedUrl} />
          </div>
        </div>
      </section>
    </div>
  </>
}
