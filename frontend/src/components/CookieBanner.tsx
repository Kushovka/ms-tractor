import { useState } from 'react'
import { Link } from 'react-router'

const storageKey = 'ms-tractor-equipment-cookie-consent'

export const CookieBanner = () => {
  const [visible, setVisible] = useState(() => !window.localStorage.getItem(storageKey))

  const choose = (value: 'accepted' | 'declined') => {
    window.localStorage.setItem(storageKey, value)
    setVisible(false)
  }

  if (!visible) return null

  return (
    <div className="fixed inset-x-4 bottom-20 z-[60] ml-auto max-w-md rounded-md border border-[var(--color-border)] bg-[var(--color-background)] p-4 shadow-2xl shadow-sm lg:bottom-6 lg:right-6 lg:left-auto">
      <div className="flex flex-col gap-4">
        <p className="text-sm font-normal leading-6 text-[var(--color-muted)]">
          We use cookies and similar tools to improve the site, understand traffic, and support lead tracking. Read our{' '}
          <Link to="/privacy-policy" className="font-normal text-[var(--color-link)] hover:text-[var(--color-link-hover)]">Privacy Policy</Link>.
        </p>
        <div className="grid grid-cols-2 gap-2">
          <button
            type="button"
            className="rounded-md border border-[var(--color-border)] px-4 py-2 text-sm font-normal text-[var(--color-link)] transition hover:bg-[var(--color-hover)]"
            onClick={() => choose('declined')}
          >
            Decline
          </button>
          <button
            type="button"
            className="rounded-md bg-[var(--color-primary)] px-4 py-2 text-sm font-normal text-white transition hover:bg-[var(--color-primary-dark)]"
            onClick={() => choose('accepted')}
          >
            Accept
          </button>
        </div>
      </div>
    </div>
  )
}
