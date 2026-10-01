import { motion, useReducedMotion } from 'framer-motion'
import { useEffect } from 'react'
import { Outlet, useLocation } from 'react-router'
import { Header } from './Header'
import { Footer } from './Footer'
import { ScrollToTop } from './ScrollToTop'
import { CookieBanner } from './CookieBanner'
import { initMetaPixel, trackPageView } from '../utils/metaPixel'

export const Layout = () => {
  const location = useLocation()
  const prefersReducedMotion = useReducedMotion()

  useEffect(() => {
    initMetaPixel()
    trackPageView()
  }, [location.pathname, location.search])

  return (
    <div className={location.pathname === '/warranty' ? 'warranty-layout' : undefined}>
      <ScrollToTop />
      <Header />
      <motion.main
        key={location.pathname}
        initial={prefersReducedMotion ? false : { opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: prefersReducedMotion ? 0.1 : 0.2, ease: 'easeOut' }}
      >
        <Outlet />
      </motion.main>
      <Footer />
      <CookieBanner />
    </div>
  )
}
