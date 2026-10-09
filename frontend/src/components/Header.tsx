import { AnimatePresence, motion } from 'framer-motion'
import { useState } from 'react'
import { Link, NavLink, useNavigate } from 'react-router'
import { FaArrowRight, FaBars, FaMapMarkerAlt, FaPhoneAlt, FaSearch, FaShieldAlt, FaTimes, FaTractor, FaTruck, FaUsers, FaWarehouse } from 'react-icons/fa'
import { FiChevronRight, FiPhone, FiSearch } from 'react-icons/fi'
import { MdFrontLoader } from 'react-icons/md'
import { TbBackhoe, TbGridDots, TbTractor } from 'react-icons/tb'
import { business } from '../data/business'
import { trackContactCta } from '../utils/ctaTracking'

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

const inventoryCategories = [
  { label: 'All Equipment', href: '/inventory', Icon: TbGridDots },
  { label: 'Tractors', href: '/inventory?bodyType=Tractors', Icon: TbTractor },
  { label: 'Skid Steers', href: '/inventory?bodyType=Skid%20Steers', Icon: MdFrontLoader },
  { label: 'Backhoes', href: '/inventory?bodyType=Backhoes', Icon: TbBackhoe },
]

const HeaderSearch = () => {
  const navigate = useNavigate()
  const [query, setQuery] = useState('')

  const submitSearch = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault()
    const term = query.trim()
    navigate(term ? `/inventory?q=${encodeURIComponent(term)}` : '/inventory')
  }

  return (
    <form role="search" onSubmit={submitSearch} className="header-search-form flex h-12 min-w-0 items-center overflow-hidden rounded-md border border-[var(--color-border)] bg-[var(--color-surface)] focus-within:border-[var(--color-primary)]">
      <label className="flex min-w-0 flex-1 items-center gap-3 px-3.5">
        <span className="sr-only">Search equipment</span>
        <FaSearch aria-hidden="true" className="h-4 w-4 shrink-0 text-[var(--color-muted)]" />
        <input type="search" inputMode="search" value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Search equipment (e.g. tractor, skid steer...)" className="h-full min-w-0 flex-1 bg-transparent text-[14px] text-[var(--color-text)] outline-none placeholder:text-[var(--color-muted)]" />
      </label>
    </form>
  )
}

export const Header = () => {
  const [open, setOpen] = useState(false)
  const [inventoryMenuOpen, setInventoryMenuOpen] = useState(false)
  const displayPhone = business.phone

  return (
    <motion.header
      className={`sticky inset-x-0 top-0 z-50 border-b border-[var(--color-border)] bg-[var(--color-surface)] ${open ? 'mobile-header-menu-open' : ''}`}
      initial={{ opacity: 0, y: -8 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.24, ease: 'easeOut' }}
    >
      <div className="mobile-header-layout relative mx-auto grid min-h-[88px] grid-cols-[auto_1fr] items-center gap-5 px-5 sm:min-h-[72px] sm:px-8 min-[1400px]:min-h-[100px] min-[1400px]:grid-cols-[250px_minmax(0,1fr)_250px] min-[1400px]:gap-7 min-[1400px]:px-[clamp(28px,3.2vw,76px)]">
        <Link to="/" className="mobile-header-logo flex min-w-0 items-center" onClick={() => setOpen(false)}>
          <img src="/images/ms-tractor-logo.webp" alt="M & S Tractor & Equipment" className="block h-auto w-[120px] shrink-0 sm:w-[166px] min-[1400px]:w-[220px]" />
        </Link>

        <div className="header-search-desktop absolute left-1/2 top-1/2 hidden w-[min(48vw,960px)] -translate-x-1/2 -translate-y-1/2 min-[1400px]:block"><HeaderSearch /></div>

        <div className="hidden min-w-0 min-[1400px]:col-start-3 min-[1400px]:flex min-[1400px]:items-center min-[1400px]:justify-end">
          <a href={business.phoneHref} onClick={() => trackContactCta('phone_click', 'Desktop Header Call')} className="desktop-header-call inline-flex shrink-0 items-center gap-2 text-[var(--color-text)] transition-colors hover:text-[var(--color-accent)]" aria-label={`Call Now ${business.phone}`}>
            <FiPhone aria-hidden="true" className="h-[26px] w-[26px] shrink-0 -rotate-[8deg] text-[var(--color-accent)]" />
            <span className="whitespace-nowrap text-[18px] font-semibold tracking-[-.02em]">{business.phone}</span>
          </a>
        </div>

        <div className="mobile-header-controls flex h-full items-center justify-self-end gap-2 min-[1400px]:hidden">
          <a href={business.phoneHref} onClick={() => trackContactCta('phone_click', 'Mobile Header Call')} className="mobile-header-call inline-flex h-10 items-center justify-center gap-1.5 rounded-md bg-[var(--color-primary)] px-2 text-[11px] font-bold uppercase tracking-[.06em] text-white" aria-label={`Call ${business.phone}`}><FaPhoneAlt aria-hidden="true" /><span>CALL</span></a>
          <button aria-label={open ? 'Close menu' : 'Open menu'} className="grid h-10 w-10 place-items-center rounded-md border border-[var(--color-primary)] text-[var(--color-primary)]" onClick={() => setOpen((value) => !value)} type="button">
            {open ? <FaTimes /> : <FaBars />}
          </button>
        </div>
      </div>

      <div className="hidden border-t border-[var(--color-border)] min-[1400px]:block">
        <div className="mx-auto flex min-h-[62px] items-center justify-center px-[clamp(28px,3.2vw,76px)]">
          <nav aria-label="Main navigation" className="flex min-w-0 items-center justify-center gap-[clamp(30px,3.4vw,54px)]">
            {desktopNavItems.map((item) => item.label === 'Inventory' ? (
              <div key={item.label} className="group relative flex min-h-[40px] items-center" onMouseEnter={() => setInventoryMenuOpen(true)} onMouseLeave={() => setInventoryMenuOpen(false)}>
                <NavLink to="/inventory" className={({ isActive }) => `inline-flex min-h-[40px] items-center whitespace-nowrap font-[var(--font-label)] text-[18px] font-black uppercase tracking-[.02em] transition-colors ${isActive ? 'text-[var(--color-secondary)]' : 'text-[var(--color-text)] hover:text-[var(--color-secondary)]'}`}>
                  Inventory
                </NavLink>
                <button type="button" aria-label="Show inventory categories" aria-expanded={inventoryMenuOpen} onClick={() => setInventoryMenuOpen((value) => !value)} onFocus={() => setInventoryMenuOpen(true)} className="ml-2 grid h-8 w-7 place-items-center text-[var(--color-muted)] hover:text-[var(--color-secondary)]"><FiChevronRight className={`h-4 w-4 rotate-90 transition-transform ${inventoryMenuOpen ? '-rotate-90' : ''}`} /></button>
                <div className={`absolute left-0 top-full z-[60] min-w-[260px] border border-[var(--color-border)] bg-[var(--color-surface)] p-2 shadow-[0_14px_32px_rgba(20,30,25,.18)] transition duration-150 ${inventoryMenuOpen ? 'visible translate-y-0 opacity-100' : 'invisible -translate-y-1 opacity-0'}`}>
                  {inventoryCategories.map(({ label, href, Icon }) => <Link key={label} to={href} onClick={() => setInventoryMenuOpen(false)} className="flex min-h-12 items-center gap-3 px-3 text-[15px] font-semibold text-[var(--color-text)] transition-colors hover:bg-[var(--color-background)] hover:text-[var(--color-secondary)]"><Icon aria-hidden="true" className="h-[18px] w-[18px] shrink-0 text-[var(--color-secondary)]" /><span>{label}</span><FiChevronRight aria-hidden="true" className="ml-auto h-4 w-4 text-[var(--color-muted)]" /></Link>)}
                </div>
              </div>
            ) : (
              <NavLink key={item.label} to={item.href} className={({ isActive }) => `inline-flex min-h-[40px] items-center whitespace-nowrap font-[var(--font-label)] text-[18px] font-black uppercase tracking-[.02em] transition-colors ${isActive ? 'text-[var(--color-secondary)]' : 'text-[var(--color-text)] hover:text-[var(--color-secondary)]'}`}>
                {item.label}
              </NavLink>
            ))}
          </nav>
        </div>
      </div>

      <div className="hidden border-t border-[var(--color-border)] px-5 py-2.5 min-[761px]:block min-[1400px]:hidden sm:px-8">
        <div className="mx-auto w-full max-w-[760px]"><HeaderSearch /></div>
      </div>

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
