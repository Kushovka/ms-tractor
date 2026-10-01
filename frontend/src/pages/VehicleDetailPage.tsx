import { useEffect, useMemo, useState } from 'react'
import { motion } from 'framer-motion'
import { Link, useParams } from 'react-router'
import { FaArrowLeft, FaArrowRight, FaCarSide, FaCheck, FaChevronLeft, FaChevronRight, FaEnvelope, FaMapMarkerAlt, FaPhoneAlt, FaTag, FaTachometerAlt } from 'react-icons/fa'
import { getVehicle, listVehicles } from '../api/vehicles'
import { Button } from '../components/Button'
import { EquipmentCard } from '../components/EquipmentCard'
import { LeadForm } from '../components/LeadForm'
import { Seo } from '../components/Seo'
import { VehicleDetailSkeleton } from '../components/Skeletons'
import { VehicleGallery } from '../components/VehicleGallery'
import { business } from '../data/business'
import type { Equipment } from '../types/equipment'
import type { Vehicle } from '../types/vehicle'
import { trackContactCta } from '../utils/ctaTracking'
import { formatNumber, formatPrice } from '../utils/format'
import { trackViewContent } from '../utils/metaPixel'

const phoneHref = business.phoneHref || business.contactHref
const hasListingValue = (value: string | number) => String(value).trim() !== '' && !/^not listed$/i.test(String(value).trim())
const toEquipmentCardData = (vehicle: Vehicle): Equipment => ({
  id: vehicle.id, slug: vehicle.slug, year: vehicle.year, make: vehicle.make, model: vehicle.model, trim: vehicle.trim,
  price: vehicle.price, hours: vehicle.engineHours ?? vehicle.mileage, bodyType: vehicle.category ?? vehicle.bodyType,
  condition: vehicle.condition ?? vehicle.trim, engine: vehicle.engine, vin: vehicle.vin, stockNumber: vehicle.stockNumber,
  status: vehicle.status ?? '', shortDescription: vehicle.shortDescription ?? vehicle.description, description: vehicle.description,
  features: vehicle.features, specs: vehicle.specs ?? {}, images: vehicle.images, imagesTotal: vehicle.imagesTotal ?? vehicle.images.length,
  featured: vehicle.featured ?? false,
})

const Feature = ({ feature }: { feature: string }) => <li className="flex items-start gap-2.5 text-[13px] leading-5 text-[var(--color-text)]"><span className="mt-0.5 grid h-4 w-4 shrink-0 place-items-center rounded-full bg-[var(--color-primary)] text-[9px] text-white"><FaCheck /></span>{feature}</li>

const RelatedVehiclesCarousel = ({ vehicles }: { vehicles: Vehicle[] }) => {
  const [start, setStart] = useState(0)
  const [direction, setDirection] = useState<1 | -1>(1)
  const [visibleCount, setVisibleCount] = useState(() => window.innerWidth >= 1024 ? 3 : window.innerWidth >= 640 ? 2 : 1)
  useEffect(() => { const resize = () => setVisibleCount(window.innerWidth >= 1024 ? 3 : window.innerWidth >= 640 ? 2 : 1); window.addEventListener('resize', resize); return () => window.removeEventListener('resize', resize) }, [])
  if (!vehicles.length) return null
  const visible = Array.from({ length: Math.min(visibleCount, vehicles.length) }, (_, index) => vehicles[(start + index) % vehicles.length])
  const move = (step: 1 | -1) => { setDirection(step); setStart((current) => (current + step + vehicles.length) % vehicles.length) }
  return <section aria-labelledby="related-vehicles-title" className="border-t border-[var(--color-divider)] bg-[var(--color-background)] px-5 py-8 sm:px-7 lg:px-9 lg:py-10"><div className="mx-auto max-w-[1440px]"><div className="mb-5 flex items-end justify-between gap-4"><div><h2 id="related-vehicles-title" className="text-[30px] font-bold leading-none text-[var(--color-primary)] sm:text-[36px]">More equipment</h2><p className="mt-1 text-sm text-[var(--color-muted)]">Explore other equipment in our inventory.</p></div><Link to="/inventory" className="group inline-flex shrink-0 items-center gap-3 border-b-2 border-[var(--color-accent)] pb-1 text-[15px] font-semibold text-[var(--color-primary)] transition hover:text-[var(--color-button-hover)] sm:text-[17px]">View all inventory <FaArrowRight className="transition-transform group-hover:translate-x-1" /></Link></div><div className="relative"><div className="grid items-stretch gap-2 sm:grid-cols-2 xl:grid-cols-3">{visible.map((vehicle, index) => <motion.div key={`${vehicle.id}-${start}-${index}`} initial={{ opacity: 0, x: direction * 18 }} animate={{ opacity: 1, x: 0 }} transition={{ duration: 0.22, ease: [0.16, 1, 0.3, 1] }}><EquipmentCard equipment={toEquipmentCardData(vehicle)} /></motion.div>)}</div>{vehicles.length > 1 ? <><button type="button" aria-label="Previous recommended equipment" onClick={() => move(-1)} className="absolute left-0 top-1/2 z-10 grid h-10 w-10 -translate-x-1/2 -translate-y-1/2 place-items-center border border-[var(--color-primary)] bg-[var(--color-background)] text-base text-[var(--color-primary)] transition hover:bg-[var(--color-primary)] hover:text-white"><FaChevronLeft /></button><button type="button" aria-label="Next recommended equipment" onClick={() => move(1)} className="absolute right-0 top-1/2 z-10 grid h-10 w-10 translate-x-1/2 -translate-y-1/2 place-items-center border border-[var(--color-primary)] bg-[var(--color-background)] text-base text-[var(--color-primary)] transition hover:bg-[var(--color-primary)] hover:text-white"><FaChevronRight /></button></> : null}</div></div></section>
}

export const VehicleDetailPage = () => {
  const { slug } = useParams()
  const [vehicle, setVehicle] = useState<Vehicle | null>(null)
  const [recommendations, setRecommendations] = useState<Vehicle[]>([])
  const [nextVehicleSlug, setNextVehicleSlug] = useState<string | null>(null)
  const [loaded, setLoaded] = useState(false)
  const [loadError, setLoadError] = useState(false)
  const [detailView, setDetailView] = useState<'overview' | 'photos'>(() => window.location.hash === '#photos' ? 'photos' : 'overview')

  const showPhotos = () => {
    setDetailView('photos')
    window.history.replaceState(null, '', '#photos')
    window.setTimeout(() => document.getElementById('photos')?.scrollIntoView({ behavior: 'smooth', block: 'start' }), 0)
  }

  useEffect(() => {
    let cancelled = false
    setLoaded(false)
    getVehicle(slug ?? '').then((item) => {
      if (!cancelled) { setVehicle(item); setLoadError(false); trackViewContent(item.id, `${item.year} ${item.make} ${item.model} ${item.trim}`, item.price) }
    }).catch(() => { if (!cancelled) { setVehicle(null); setLoadError(true) } }).finally(() => { if (!cancelled) setLoaded(true) })
    return () => { cancelled = true }
  }, [slug])

  useEffect(() => {
    if (!vehicle || vehicle.slug !== slug) return
    let cancelled = false
    listVehicles({ pageSize: 50, sort: 'year_desc' }).then(({ items }) => {
      const currentIndex = items.findIndex((item) => item.slug === vehicle.slug)
      setNextVehicleSlug(currentIndex >= 0 ? items[currentIndex + 1]?.slug ?? null : null)
      const candidates = items.slice(0, 8).filter((item) => item.id !== vehicle.id && item.slug !== vehicle.slug)
      const score = (item: Vehicle) => (item.category?.toLowerCase() === vehicle.category?.toLowerCase() ? 3 : 0) + (item.make.toLowerCase() === vehicle.make.toLowerCase() ? 2 : 0) + (vehicle.price > 0 && Math.abs(item.price - vehicle.price) / vehicle.price < 0.3 ? 1 : 0)
      candidates.sort((a, b) => score(b) - score(a))
      if (!cancelled) setRecommendations(candidates.slice(0, 6))
    }).catch(() => { if (!cancelled) { setRecommendations([]); setNextVehicleSlug(null) } })
    return () => { cancelled = true }
  }, [slug, vehicle])

  const title = useMemo(() => vehicle ? [vehicle.year, vehicle.make, vehicle.model, vehicle.trim !== vehicle.condition ? vehicle.trim : ''].filter(Boolean).join(' ') : '', [vehicle])
  if (!vehicle && loaded && loadError) return <section className="section soft-band"><div className="mx-auto max-w-3xl px-4 text-center sm:px-6 lg:px-8"><div className="surface-card p-8"><h1 className="text-3xl text-[var(--color-text)]">Equipment details are temporarily unavailable</h1><p className="mt-3 text-[var(--color-muted)]">Please try again later or call us for current equipment information.</p><div className="mt-6 flex flex-col justify-center gap-3 sm:flex-row"><Button href="/inventory" variant="secondary">Back to Inventory</Button><Button href={phoneHref}><FaPhoneAlt /> Contact</Button></div></div></div></section>
  if (!vehicle) return <VehicleDetailSkeleton />

  const specs = [['Year', String(vehicle.year)], ['Make', vehicle.make], ['Model', vehicle.model], ['Condition', vehicle.condition ?? ''], ['Category', vehicle.category ?? vehicle.bodyType], ['Serial number', vehicle.vin], ['Engine hours', vehicle.engineHours == null ? '' : `${formatNumber(vehicle.engineHours)} hrs`], ['Power', vehicle.powerHp ? `${vehicle.powerHp} hp` : ''], ...Object.entries(vehicle.specs ?? {})].filter(([, value]) => hasListingValue(value))
  const facts = [
    { label: 'Engine Hours', value: vehicle.engineHours == null ? 'Not listed' : `${formatNumber(vehicle.engineHours)} hrs`, Icon: FaTachometerAlt },
    { label: 'Category', value: vehicle.category ?? vehicle.bodyType, Icon: FaCarSide },
    { label: 'Condition', value: vehicle.condition ?? 'Not listed', Icon: FaTag },
  ]

  return <><Seo title={title} description={`${title} available at M & S Tractor & Equipment in Shreveport, LA. Call or request information.`} noIndex schema={{ '@context': 'https://schema.org', '@type': 'Product', name: title, brand: vehicle.make, model: vehicle.model, additionalProperty: [{ '@type': 'PropertyValue', name: 'Engine hours', value: vehicle.engineHours ?? '' }], ...(vehicle.price > 0 ? { offers: { '@type': 'Offer', price: vehicle.price, priceCurrency: 'USD' } } : {}) }} />
    <main className="equipment-detail-page bg-[var(--color-background)] text-[var(--color-text)]">
      <nav aria-label="Browse equipment" className="equipment-detail-listing-nav">
        <Link to="/inventory" className="inline-flex min-h-8 items-center gap-2 text-[12px] text-[var(--color-muted)] transition hover:text-[var(--color-primary)]"><FaArrowLeft aria-hidden="true" />Previous</Link>
        <span aria-hidden="true" className="h-5 border-l border-[var(--color-border)]" />
        {nextVehicleSlug ? <Link to={`/inventory/${nextVehicleSlug}`} className="inline-flex min-h-8 items-center gap-2 text-[12px] font-semibold text-[var(--color-text)] transition hover:text-[var(--color-primary)]">Next<FaArrowRight aria-hidden="true" /></Link> : <span aria-disabled="true" className="inline-flex min-h-8 items-center gap-2 text-[12px] font-semibold text-[var(--color-disabled)]">Next<FaArrowRight aria-hidden="true" /></span>}
      </nav>
      <section className="equipment-detail-hero mx-auto grid max-w-[1440px] gap-5 px-5 pb-6 sm:px-7 lg:grid-cols-[minmax(0,1.03fr)_minmax(400px,.7fr)] lg:gap-10 lg:px-0 lg:pb-7">
        <div id="vehicle-gallery" className="relative min-w-0 lg:min-h-[520px]"><VehicleGallery images={vehicle.images} imagesTotal={vehicle.imagesTotal} slug={vehicle.slug} title={title} onShowPhotos={showPhotos} showAllPhotos={detailView === 'photos'} /></div>
        <aside className="flex min-w-0 flex-col pt-1 lg:pt-2">
          <div className="flex items-center gap-2 text-[10px] font-semibold uppercase tracking-[.08em] text-[var(--color-muted)]"><span className="h-[2px] w-4 bg-[var(--color-primary)]" />{vehicle.category ?? vehicle.bodyType}</div>
          <h1 className="equipment-detail-title mt-2 font-[var(--font-heading)] text-[36px] font-bold uppercase leading-[.94] tracking-[-.02em] text-[var(--color-primary)] sm:text-[42px] lg:text-[40px]">{title}</h1>
          <p className="equipment-detail-meta mt-2 flex flex-wrap items-center gap-x-3 gap-y-1 text-[13px] text-[var(--color-muted)]"><span>{vehicle.condition ?? 'Equipment'}</span>{vehicle.stockNumber ? <><span className="text-[var(--color-border)]">|</span><span>Stock #{vehicle.stockNumber}</span></> : null}{hasListingValue(vehicle.vin) ? <><span className="text-[var(--color-border)]">|</span><span className="max-w-full truncate" title={vehicle.vin}>Serial #{vehicle.vin}</span></> : null}</p>
          <p className="equipment-detail-price mt-2 text-[44px] font-bold leading-none tracking-[-.025em] text-[var(--color-primary)] sm:text-[46px] lg:text-[44px]">{formatPrice(vehicle.price)}</p>
          <dl className="equipment-detail-facts mt-4 grid grid-cols-3 border-y border-[var(--color-border)] py-3">{facts.map(({ label, value, Icon }, index) => <div key={label} className={`flex min-w-0 items-center gap-2.5 ${index > 0 ? 'border-l border-[var(--color-divider)] pl-3 sm:pl-5' : ''}`}><Icon className="shrink-0 text-lg text-[var(--color-primary)]" /><div className="min-w-0"><dd className="truncate text-[12px] font-bold leading-4 text-[var(--color-text)] sm:text-[14px]">{value}</dd><dt className="mt-0.5 text-[10px] text-[var(--color-muted)] sm:text-[12px]">{label}</dt></div></div>)}</dl>
          <a href={phoneHref} className="equipment-detail-call site-button mt-4 flex min-h-[50px] items-center justify-center gap-2.5 bg-[var(--color-primary)] px-4 text-[15px] font-bold text-white transition hover:bg-[var(--color-button-hover)]" onClick={() => trackContactCta('phone_click', 'Equipment Detail Call')}><FaPhoneAlt aria-hidden="true" />Call {business.phone}</a>
          <div className="mt-2 grid grid-cols-1 gap-2"><a href="#request-info" className="equipment-detail-request site-button flex min-h-[48px] items-center justify-center gap-2 border border-[var(--color-border)] bg-transparent px-2 text-center text-[13px] font-semibold text-[var(--color-text)] transition hover:bg-[var(--color-hover)]" onClick={() => trackContactCta('contact_form_click', 'Equipment Detail Request Info')}><FaEnvelope />Request More Info</a></div>
        </aside>
      </section>

      <section className="equipment-detail-shell border-t border-[var(--color-divider)] px-5 py-5 sm:px-7 lg:py-6"><div className="equipment-detail-content mx-auto max-w-[1440px]"><div className="grid gap-7 lg:grid-cols-2 lg:gap-8">
        <div className="min-w-0"><nav aria-label="Equipment details" className="mb-5 flex gap-7 overflow-x-auto border-b border-[var(--color-border)] text-[12px] font-semibold uppercase tracking-wide"><a href="#overview" onClick={() => { setDetailView('overview'); window.history.replaceState(null, '', '#overview') }} className={`shrink-0 border-b-2 px-3 pb-3 ${detailView === 'overview' ? 'border-[var(--color-primary)] text-[var(--color-primary)]' : 'border-transparent text-[var(--color-muted)] hover:text-[var(--color-primary)]'}`}>Overview</a><a href="#photos" onClick={() => { setDetailView('photos'); window.history.replaceState(null, '', '#photos') }} className={`shrink-0 border-b-2 px-3 pb-3 ${detailView === 'photos' ? 'border-[var(--color-primary)] text-[var(--color-primary)]' : 'border-transparent text-[var(--color-muted)] hover:text-[var(--color-primary)]'}`}>Photos</a></nav>
          {detailView === 'photos' ? <section id="photos" className="scroll-mt-24 border-b border-[var(--color-divider)] pb-5"><h2 className="font-[var(--font-heading)] text-[28px] font-bold text-[var(--color-primary)]">Equipment photos</h2><div id="vehicle-photos-grid" className="mt-3" /></section> : null}
          <article id="overview" className="scroll-mt-24"><h2 className="font-[var(--font-heading)] text-[28px] font-bold leading-none text-[var(--color-primary)] sm:text-[30px]">Equipment overview</h2><p className="mt-3 max-w-[78ch] whitespace-pre-line text-[14px] leading-[1.6] text-[var(--color-muted)]">{vehicle.description || vehicle.shortDescription}</p></article>
          <div className="mt-5 grid gap-6 md:grid-cols-[minmax(0,1.35fr)_minmax(190px,.85fr)] md:gap-5"><section id="specifications" className="min-w-0 scroll-mt-24 border-t border-[var(--color-divider)] pt-3"><h2 className="font-[var(--font-heading)] text-[22px] font-bold leading-none text-[var(--color-primary)]">Specifications</h2><dl className="mt-2 grid grid-cols-1 gap-x-4">{specs.map(([label, value]) => <div key={label} className="grid min-h-[32px] grid-cols-[minmax(0,.72fr)_minmax(0,1fr)] gap-2 border-b border-[var(--color-divider)] px-2 py-1.5 text-[11px] leading-4"><dt className="text-[var(--color-text)]">{label}</dt><dd className="min-w-0 break-words text-[var(--color-muted)]" title={value}>{value}</dd></div>)}</dl></section>
            <aside id="features" className="scroll-mt-24 border-t border-[var(--color-divider)] pt-3"><h2 className="font-[var(--font-heading)] text-[22px] font-bold leading-none text-[var(--color-primary)]">Key features</h2>{vehicle.features.length ? <ul className="mt-3 grid gap-y-2">{vehicle.features.map((feature) => <Feature key={feature} feature={feature} />)}</ul> : <p className="mt-3 text-sm text-[var(--color-muted)]">Contact us for equipment details.</p>}<div className="mt-5 border border-[var(--color-divider)] p-3 text-[11px] leading-5 text-[var(--color-muted)]"><span className="font-semibold text-[var(--color-primary)]">Well maintained and ready to work.</span><br />Contact us for more details or to schedule a viewing.</div></aside>
          </div>
        </div>
        <aside className={`grid gap-3 pt-[44px] lg:sticky lg:top-24 ${detailView === 'overview' ? 'lg:grid-rows-[auto_minmax(0,1fr)] lg:self-stretch' : 'lg:content-start lg:self-start'}`}><section id="location" className="grid min-h-[180px] min-w-0 overflow-hidden border border-[var(--color-border)] bg-[var(--color-surface)] sm:grid-cols-[1fr_1fr]"><div className="flex items-start gap-3 p-4"><FaMapMarkerAlt className="mt-0.5 shrink-0 text-xl text-[var(--color-primary)]" /><div className="text-[15px] leading-7"><h2 className="text-[16px] font-bold leading-6 text-[var(--color-text)]">{business.shortLocation}</h2><p className="mt-1">{business.address}<br />{business.cityState} {business.postalCode}</p><a href={business.mapsUrl} target="_blank" rel="noreferrer" className="mt-2 inline-block font-semibold text-[var(--color-primary)] underline underline-offset-2">View on Map →</a></div></div><img src={business.heroImage} alt="M & S Tractor & Equipment dealership in Shreveport, Louisiana" className="h-[150px] w-full object-cover sm:h-full" /></section>
          <section id="request-info" className={`vehicle-inquiry scroll-mt-24 grid min-w-0 gap-4 p-4 text-white sm:p-5 ${detailView === 'overview' ? 'vehicle-inquiry--fill' : ''}`}><div><h2 className="font-[var(--font-heading)] text-[28px] font-bold leading-none sm:text-[30px]">Get more information</h2><p className="mt-2 text-[12px] leading-5 text-white/85">Have a question or want to schedule a time to see this equipment? Send us a message and we’ll get back to you shortly.</p></div><LeadForm title="Send Inquiry" vehicleId={vehicle.id} vehicleName={title} vehicleValue={vehicle.price} variant="vehicle" className="vehicle-inquiry-form" messageDefaultValue={`I'm interested in the ${title}. Please contact me with more information.`} /></section></aside>
      </div></div></section>
      <RelatedVehiclesCarousel vehicles={recommendations} />
    </main>
    <div className="equipment-detail-sticky fixed inset-x-0 bottom-0 z-50 border-t border-[var(--color-border)] bg-[var(--color-background)] px-4 py-3 shadow-sm lg:hidden"><div className="mx-auto flex max-w-7xl items-center gap-3"><div className="min-w-0 flex-1"><p className="truncate text-sm text-[var(--color-text)]">{title}</p><p className="font-semibold text-[var(--color-primary)]">{formatPrice(vehicle.price)}</p></div><a href={phoneHref} className="equipment-detail-sticky__action site-button inline-flex h-12 w-12 shrink-0 items-center justify-center bg-[var(--color-primary)] text-xl text-white" aria-label="Call about this equipment" onClick={() => trackContactCta('phone_click', 'Equipment Detail Sticky Call')}><FaPhoneAlt /></a><a href="#request-info" className="equipment-detail-sticky__action site-button inline-flex h-12 w-12 shrink-0 items-center justify-center bg-[var(--color-accent)] text-xl text-[var(--color-text)]" aria-label="Request information about this equipment" onClick={() => trackContactCta('contact_form_click', 'Equipment Detail Sticky Request Info')}><FaArrowRight /></a></div></div>
  </>
}
