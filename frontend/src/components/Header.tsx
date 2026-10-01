import { AnimatePresence, motion } from 'framer-motion'
import { useEffect, useState } from 'react'
import { Link, NavLink, useNavigate } from 'react-router'
import { FaArrowRight, FaBars, FaMapMarkerAlt, FaPhoneAlt, FaSearch, FaShieldAlt, FaTimes, FaTractor, FaTruck, FaUsers, FaWarehouse } from 'react-icons/fa'
import { FiChevronRight, FiPhone, FiSearch } from 'react-icons/fi'
import { listEquipment } from '../api/equipment'
import { business } from '../data/business'
import type { Equipment } from '../types/equipment'
import { trackContactCta } from '../utils/ctaTracking'
import { formatPrice } from '../utils/format'

const desktopNavItems = [
  { label: 'Inventory', href: '/inventory' },
  { label: 'Delivery', href: '/delivery' },
  { label: 'Warranty', href: '/warranty' },
  { label: 'About', href: '/about' },
  { label: 'Our Team', href: '/team' },
  { label: 'Contact', href: '/contact' },
]

const mobileNavItems = [
  { label: 'Inventory', href: '/inventory', Icon: FaTractor },
  { label: 'Delivery', href: '/delivery', Icon: FaTruck },
  { label: 'Warranty', href: '/warranty', Icon: FaShieldAlt },
  { label: 'About', href: '/about', Icon: FaWarehouse },
  { label: 'Our Team', href: '/team', Icon: FaUsers },
  { label: 'Contact', href: '/contact', Icon: FaPhoneAlt },
]

const HeaderSearch = () => {
  const navigate = useNavigate()
  const [query, setQuery] = useState('')
  const [matches, setMatches] = useState<Equipment[]>([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    const term = query.trim()
    if (term.length < 2) {
      setMatches([])
      setLoading(false)
      return
    }
    let cancelled = false
    setLoading(true)
    listEquipment({ q: term, pageSize: 3 })
      .then((response) => { if (!cancelled) setMatches(response.items) })
      .catch(() => { if (!cancelled) setMatches([]) })
      .finally(() => { if (!cancelled) setLoading(false) })
    return () => { cancelled = true }
  }, [query])

  const viewSearch = () => {
    const term = query.trim()
    if (term) navigate(`/inventory?q=${encodeURIComponent(term)}`)
  }

  return <div className="header-search relative w-full">
    <div className="header-search-control flex h-12 items-center overflow-hidden rounded-[10px] bg-[#ebe8e0] px-3.5 transition-colors focus-within:bg-[#e8e5dc]">
      <label className="relative flex h-full min-w-0 flex-1 items-center gap-3">
        <span className="sr-only">Search equipment</span>
        <FaSearch aria-hidden="true" className="shrink-0 text-[14px] text-[var(--color-primary)]" />
        <input className="h-10 min-w-0 w-full bg-transparent py-0 pr-1 text-[15px] text-[var(--color-text)] outline-none placeholder:text-[#77746e]" type="search" inputMode="search" value={query} onChange={(event) => setQuery(event.target.value)} onKeyDown={(event) => { if (event.key === 'Enter') { event.preventDefault(); viewSearch() } if (event.key === 'Escape') setQuery('') }} placeholder="Search equipment" />
        {query ? <button type="button" aria-label="Clear equipment search" onClick={() => setQuery('')} className="grid h-8 w-8 shrink-0 place-items-center text-base text-[var(--color-muted)] transition hover:text-[var(--color-primary)]"><FaTimes aria-hidden="true" /></button> : null}
      </label>
      <button type="button" onClick={viewSearch} aria-label="Search inventory" className="header-search-submit grid h-9 w-9 shrink-0 place-items-center text-[var(--color-primary)] transition hover:text-[var(--color-secondary)]"><FiSearch aria-hidden="true" className="h-[18px] w-[18px]" /></button>
    </div>
    {query.trim().length >= 2 ? <div className="absolute right-0 top-[calc(100%+0.6rem)] z-50 max-h-[min(480px,calc(100dvh-8rem))] w-[min(620px,calc(100vw-2.5rem))] overflow-y-auto border border-[var(--color-border)] bg-[var(--color-surface)] text-[var(--color-text)] shadow-[0_22px_54px_rgba(23,26,24,0.2)]">
      <div className="flex items-center justify-between border-b border-[var(--color-border)] px-4 py-3.5 sm:px-5"><span className="text-[11px] font-bold uppercase tracking-[0.12em] text-[var(--color-muted)]">{loading ? 'Searching' : `${matches.length} matching listings`}</span><span className="h-2 w-2 bg-[var(--color-accent)]" aria-hidden="true" /></div>
      {loading ? <p className="px-5 py-6 text-sm text-[var(--color-muted)]">Looking through current inventory…</p> : matches.length ? <><div className="divide-y divide-[var(--color-border)]">{matches.map((item) => <Link key={item.id} to={`/inventory/${item.slug}`} onClick={() => setQuery('')} className="group grid min-h-[84px] grid-cols-[76px_minmax(0,1fr)_auto] items-center gap-3 px-3 py-3 transition-colors hover:bg-[var(--color-hover)] sm:grid-cols-[88px_minmax(0,1fr)_auto] sm:gap-4 sm:px-5"><img src={item.images[0]} alt="" className="h-[60px] w-[76px] shrink-0 object-cover sm:h-[66px] sm:w-[88px]" /><span className="min-w-0"><strong className="block truncate text-[14px] font-bold leading-tight sm:text-[16px]">{item.year} {item.make} {item.model}</strong><span className="mt-1 block truncate text-[11px] text-[var(--color-muted)] sm:text-[13px]">{item.trim || 'Available now'}</span></span><span className="flex items-center gap-2 pl-1 text-right"><span className="whitespace-nowrap text-[12px] font-bold tabular-nums text-[var(--color-primary)] sm:text-[14px]">{formatPrice(item.price)}</span><FaArrowRight aria-hidden="true" className="hidden text-[11px] text-[var(--color-muted)] transition group-hover:translate-x-0.5 sm:block" /></span></Link>)}</div><button type="button" onClick={viewSearch} className="flex h-12 w-full items-center justify-between border-t border-[var(--color-border)] px-4 text-[11px] font-bold uppercase tracking-[0.1em] text-[var(--color-primary)] transition hover:bg-[var(--color-hover)] sm:px-5"><span>Browse all matching equipment</span><FaArrowRight aria-hidden="true" /></button></> : <p className="px-5 py-6 text-sm text-[var(--color-muted)]">No equipment matches “{query.trim()}”.</p>}
    </div> : null}
  </div>
}

export const Header = () => {
  const [open, setOpen] = useState(false)
  const displayPhone = business.phone

  return (
    <motion.header
      className={`sticky inset-x-0 top-0 z-50 border-b border-[var(--color-border)] bg-[var(--color-surface)] ${open ? 'mobile-header-menu-open' : ''}`}
      initial={{ opacity: 0, y: -8 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.24, ease: 'easeOut' }}
    >
      <div className="mobile-header-layout relative mx-auto grid min-h-[88px] grid-cols-[auto_1fr] items-center gap-5 px-5 sm:min-h-[72px] sm:px-8 min-[1400px]:min-h-[116px] min-[1400px]:grid-cols-[170px_minmax(0,1fr)_300px] min-[1400px]:gap-7 min-[1400px]:px-[clamp(28px,3.2vw,76px)]">
        <Link to="/" className="mobile-header-logo flex min-w-0 items-center" onClick={() => setOpen(false)}>
          <img src="/images/ms-tractor-logo.webp" alt="M & S Tractor & Equipment" className="block h-auto w-[120px] shrink-0 sm:w-[166px] min-[1400px]:w-[170px]" />
        </Link>

        <nav aria-label="Main navigation" className="hidden min-w-0 items-center justify-center gap-[clamp(9px,.85vw,15px)] min-[1400px]:absolute min-[1400px]:left-1/2 min-[1400px]:flex min-[1400px]:-translate-x-1/2">
          {desktopNavItems.map((item) => (
            <NavLink key={item.label} to={item.href} className={({ isActive }) => `inline-flex items-center gap-1 whitespace-nowrap font-[var(--font-label)] text-[15px] font-bold uppercase tracking-[.01em] transition-colors ${isActive ? 'text-[var(--color-secondary)]' : 'text-[var(--color-text)] hover:text-[var(--color-secondary)]'}`}>
              {item.label}
            </NavLink>
          ))}
        </nav>

        <div className="hidden min-w-0 min-[1400px]:col-start-3 min-[1400px]:block"><HeaderSearch /></div>

        <div className="mobile-header-controls flex h-full items-center justify-self-end gap-2 min-[1400px]:hidden">
          <a href={business.phoneHref} onClick={() => trackContactCta('phone_click', 'Mobile Header Call')} className="mobile-header-call inline-flex h-10 items-center justify-center gap-1.5 rounded-md bg-[var(--color-primary)] px-2 text-[11px] font-bold uppercase tracking-[.06em] text-white" aria-label={`Call ${business.phone}`}><FaPhoneAlt aria-hidden="true" /><span>CALL</span></a>
          <button aria-label={open ? 'Close menu' : 'Open menu'} className="grid h-10 w-10 place-items-center rounded-md border border-[var(--color-primary)] text-[var(--color-primary)]" onClick={() => setOpen((value) => !value)} type="button">
            {open ? <FaTimes /> : <FaBars />}
          </button>
        </div>
      </div>

      <div className="hidden border-t border-[var(--color-border)] px-5 py-2.5 min-[761px]:block min-[1400px]:hidden sm:px-8"><HeaderSearch /></div>

      <AnimatePresence>
        {open ? (
          <motion.div className="mobile-menu-overlay fixed inset-0 z-[100] flex items-center justify-center bg-[rgba(23,58,43,.88)] p-2.5 min-[1400px]:hidden sm:p-4" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: 0.2 }} onClick={(event) => { if (event.target === event.currentTarget) setOpen(false) }}>
            <motion.section role="dialog" aria-modal="true" aria-label="Main navigation" className="mobile-menu-panel flex h-[calc(100dvh-20px)] max-h-[900px] w-full max-w-[560px] flex-col overflow-y-auto border border-[var(--color-border)] bg-[var(--color-surface)] px-5 pb-5 pt-4 text-[var(--color-text)] shadow-[0_24px_80px_rgba(23,26,24,.35)] sm:h-[calc(100dvh-32px)] sm:px-7 sm:pb-7" initial={{ y: 12, scale: 0.99 }} animate={{ y: 0, scale: 1 }} exit={{ y: 8, scale: 0.99 }} transition={{ duration: 0.22, ease: [0.22, 1, 0.36, 1] }} onClick={(event) => event.stopPropagation()}>
              <div className="mobile-menu-header flex shrink-0 items-center justify-between border-b border-[var(--color-border)] pb-3">
                <Link to="/" onClick={() => setOpen(false)}><img src="/images/ms-tractor-logo.webp" alt="M & S Tractor & Equipment" className="block h-auto w-[158px] sm:w-[180px]" /></Link>
                <button aria-label="Close menu" className="mobile-menu-close grid h-10 w-10 place-items-center text-2xl text-[var(--color-primary)]" onClick={() => setOpen(false)} type="button"><FaTimes /></button>
              </div>

              <div className="mobile-menu-departments" aria-label="Sales, parts, service, and support">Sales <i>•</i> Parts <i>•</i> Service <i>•</i> Support</div>

              <nav aria-label="Equipment categories" className="mobile-menu-nav mt-3 shrink-0">
                {mobileNavItems.map(({ label, href, Icon }) => <NavLink key={label} to={href} onClick={() => setOpen(false)} className="mobile-menu-item group flex min-h-[54px] items-center gap-3 border-b border-[var(--color-border)] text-[15px] font-bold uppercase tracking-[.02em] transition-colors hover:text-[var(--color-secondary)] sm:min-h-[61px] sm:text-[16px]"><Icon aria-hidden="true" className="mobile-menu-item-icon h-[19px] w-[19px] shrink-0 text-[var(--color-secondary)]" /><span className="flex-1">{label}</span><FiChevronRight aria-hidden="true" className="mobile-menu-chevron h-4 w-4 shrink-0 text-[var(--color-muted)] transition-transform group-hover:translate-x-1" /></NavLink>)}
              </nav>

              <Link to="/inventory" className="mobile-menu-search mt-4 inline-flex min-h-[52px] shrink-0 items-center justify-center gap-3 bg-[var(--color-primary)] px-4 text-[14px] font-bold uppercase tracking-[.06em] text-white transition-colors hover:bg-[var(--color-secondary)]" onClick={() => setOpen(false)}><FiSearch aria-hidden="true" className="h-5 w-5" />Search Inventory<FaArrowRight aria-hidden="true" /></Link>

              <div className="mobile-menu-contacts mt-4 grid shrink-0 grid-cols-2 gap-3">
                <a href={business.phoneHref} className="mobile-menu-contact flex min-h-[66px] items-center gap-3 border border-[var(--color-border)] px-3 text-[var(--color-text)]" onClick={() => { setOpen(false); trackContactCta('phone_click', 'Mobile Menu Contact') }}><FiPhone className="mobile-menu-contact-icon h-5 w-5 shrink-0 text-[var(--color-primary)]" /><span className="min-w-0"><strong className="mobile-menu-contact-title block text-[12px] uppercase">Call Us</strong><span className="mobile-menu-contact-detail mt-1 block truncate text-[11px] text-[var(--color-muted)]">{displayPhone}</span></span></a>
                <a href={business.mapsUrl} target="_blank" rel="noreferrer" className="mobile-menu-contact flex min-h-[66px] items-center gap-3 border border-[var(--color-border)] px-3 text-[var(--color-text)]" onClick={() => { setOpen(false); trackContactCta('directions_click', 'Mobile Menu Directions') }}><FaMapMarkerAlt className="mobile-menu-contact-icon shrink-0 text-[20px] text-[var(--color-primary)]" /><span className="min-w-0"><strong className="mobile-menu-contact-title block text-[12px] uppercase">Directions</strong><span className="mobile-menu-contact-detail mt-1 block truncate text-[11px] text-[var(--color-muted)]">{business.cityState}</span></span></a>
              </div>
            </motion.section>
          </motion.div>
        ) : null}
      </AnimatePresence>
    </motion.header>
  )
}
