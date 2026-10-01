import { FaCookieBite } from 'react-icons/fa6'
import { Link } from 'react-router'
import { useState } from 'react'

const storageKey = 'ms-tractor-equipment-cookie-consent'

export const CookieBanner = () => {
  const [visible, setVisible] = useState(() => !window.localStorage.getItem(storageKey))

  const choose = (value: 'accepted' | 'declined') => {
    window.localStorage.setItem(storageKey, value)
    setVisible(false)
  }

  if (!visible) return null

  return (
    <aside className="cookie-consent" aria-label="Cookie preferences">
      <div className="cookie-consent__mark" aria-hidden="true">
        <FaCookieBite />
      </div>
      <div className="cookie-consent__copy">
        <h2>Your privacy, your choice</h2>
        <p>
          We use cookies and similar tools to improve the site, understand traffic, and support lead tracking.{' '}
          <Link to="/privacy-policy">Read our Privacy Policy</Link>.
        </p>
      </div>
      <div className="cookie-consent__actions">
        <button type="button" className="cookie-consent__decline" onClick={() => choose('declined')}>
          Decline
        </button>
        <button type="button" className="cookie-consent__accept" onClick={() => choose('accepted')}>
          Accept
        </button>
      </div>
    </aside>
  )
}
