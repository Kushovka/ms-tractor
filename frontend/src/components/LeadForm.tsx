import { motion, useReducedMotion } from 'framer-motion'
import { useMemo, useState, type ReactNode } from 'react'
import { FaArrowRight, FaBan, FaCreditCard } from 'react-icons/fa'
import { FiChevronDown, FiFileText, FiMail, FiMessageSquare, FiPhone, FiUser } from 'react-icons/fi'
import { createLead } from '../api/leads'
import { trackingConfig } from '../config/tracking'
import { createMetaEventId, getCookieValue, splitName, trackLead } from '../utils/metaPixel'

type LeadFormProps = {
  title: string
  vehicleId?: string
  vehicleName?: string
  vehicleValue?: number
  messagePlaceholder?: string
  messageDefaultValue?: string
  className?: string
  variant?: 'contact' | 'default' | 'vehicle'
  showVehicleInterest?: boolean
  markRequiredNameFields?: boolean
  singleNameField?: boolean
  namePlaceholder?: string
  phonePlaceholder?: string
  actionAside?: ReactNode
  inquiryOptions?: string[]
}

const COUNTRY_CODE_PREFIX = '+1 '

const getPhoneDigits = (value: string) => {
  const digits = value.replace(/\D/g, '')
  const hasCountryCode = value.trim().startsWith('+1') || digits.length > 10
  const localDigits = hasCountryCode && digits.startsWith('1') ? digits.slice(1) : digits

  return localDigits.slice(0, 10)
}

const formatUsPhone = (value: string) => {
  const digits = getPhoneDigits(value)

  if (!digits) return ''
  if (digits.length <= 3) return `${COUNTRY_CODE_PREFIX}(${digits}`
  if (digits.length <= 6) return `${COUNTRY_CODE_PREFIX}(${digits.slice(0, 3)}) ${digits.slice(3)}`

  return `${COUNTRY_CODE_PREFIX}(${digits.slice(0, 3)}) ${digits.slice(3, 6)}-${digits.slice(6)}`
}

export const LeadForm = ({ title, vehicleId, vehicleName, vehicleValue, messagePlaceholder = 'Message (optional)', messageDefaultValue, className = '', variant = 'default', showVehicleInterest = false, markRequiredNameFields = false, singleNameField = false, namePlaceholder, phonePlaceholder = '(318) 631-3222', actionAside, inquiryOptions }: LeadFormProps) => {
  const prefersReducedMotion = useReducedMotion()
  const formStartedAt = useMemo(() => Date.now(), [])
  const [sent, setSent] = useState(false)
  const [error, setError] = useState('')
  const [phoneValue, setPhoneValue] = useState('')
  const [submitting, setSubmitting] = useState(false)
  const withFieldIcon = (icon: ReactNode, control: ReactNode, modifier = '') => (
    <div className={`lead-field-control${variant === 'contact' ? ' contact-field-control' : ''} ${modifier}`}>
      {icon}{control}
    </div>
  )

  return (
    <motion.form
      className={`surface-card p-5 sm:p-6 ${variant === 'contact' ? 'contact-form' : variant === 'vehicle' ? 'lg:p-7' : 'rounded-md'} ${className}`}
      action="/api/leads"
      method="post"
      initial={prefersReducedMotion ? false : { opacity: 0, clipPath: 'inset(0 0 8% 0)' }}
      whileInView={{ opacity: 1, clipPath: 'inset(0 0 0% 0)' }}
      viewport={{ once: true, amount: 0.2 }}
      transition={{ duration: prefersReducedMotion ? 0.14 : 0.4, ease: [0.16, 1, 0.3, 1] }}
      onSubmit={async (event) => {
        event.preventDefault()
        const formElement = event.currentTarget
        setError('')
        setSent(false)
        setSubmitting(true)

        const form = new FormData(formElement)
        const firstName = String(form.get('firstName') ?? '').trim()
        const lastName = String(form.get('lastName') ?? '').trim()
        const phone = getPhoneDigits(phoneValue)
        const email = String(form.get('email') ?? '').trim()
        const website = String(form.get('website') ?? '').trim()
        const message = String(form.get('message') ?? '').trim()
        const inquiryType = String(form.get('inquiryType') ?? '').trim()
        const vehicleInterest = String(form.get('vehicleInterest') ?? '').trim()
        const leadMessage = [inquiryType ? `Inquiry type: ${inquiryType}` : '', message, vehicleInterest ? `Vehicle or Stock #: ${vehicleInterest}` : ''].filter(Boolean).join('\n')
        const customerName = `${firstName} ${lastName}`.trim()
        const leadType = vehicleId ? 'quote' : 'contact'
        const metaEventId = createMetaEventId('lead')
        const fbp = getCookieValue('_fbp')
        const fbc = getCookieValue('_fbc')
        const { firstName: metaFirstName, lastName: metaLastName } = splitName(customerName)
        const contentIds = [vehicleId ?? `${trackingConfig.meta.defaultLeadContentPrefix}-${leadType}`]
        const contentType = vehicleId ? trackingConfig.meta.productContentType : trackingConfig.meta.serviceContentType
        const contentName = vehicleName ?? `${leadType} request`
        const currency = trackingConfig.meta.currency
        const eventValue = vehicleValue ?? trackingConfig.meta.defaultLeadValue

        if (phone.length !== 10) {
          setSubmitting(false)
          setError('Please enter a valid 10-digit US phone number.')
          return
        }

        try {
          await createLead({
            vehicleId,
            leadType,
            customerName,
            phone,
            email,
            message: leadMessage,
            metaEventId,
            fbp,
            fbc,
            userAgent: navigator.userAgent,
            eventSourceUrl: window.location.href,
            formStartedAt,
            website,
            contentIds,
            contentName,
            contentType,
            currency,
            value: eventValue ?? undefined,
          })
          try {
            trackLead({
              eventId: metaEventId,
              leadType,
              contentIds,
              contentName,
              contentType,
              currency,
              value: eventValue,
              advancedMatching: {
                email,
                phone,
                firstName: metaFirstName,
                lastName: metaLastName,
                externalId: email || phone,
                fbp,
                fbc,
              },
            })
          } catch {
            // Browser tracking can be blocked; the lead itself was already submitted.
          }
          setError('')
          setSent(true)
          setPhoneValue('')
          formElement.reset()
        } catch {
          setSent(false)
          setError('We could not send the request right now. Please call us or try again.')
        } finally {
          setSubmitting(false)
        }
      }}
    >
      {variant === 'default' ? <><p className="eyebrow">Quick request</p><h3 className="mt-2 text-2xl font-normal text-[var(--color-text)]">{title}</h3>{vehicleName ? <p className="mt-1 text-sm font-normal text-[var(--color-muted)]">{vehicleName}</p> : null}</> : null}
      <aside className="financing-notice" aria-label="Financing information">
        <span className="financing-notice-icon" aria-hidden="true"><FaCreditCard /><FaBan /></span>
        <div className="financing-notice-copy"><strong>No financing available.</strong><span className="financing-notice-divider" aria-hidden="true" /><span>We do not offer in-house financing.</span></div>
      </aside>
      <div className={`${variant === 'vehicle' ? '' : 'mt-5'} grid gap-2.5 sm:grid-cols-2`}>
        <div className="hidden" aria-hidden="true">
          <label>
            Website
            <input name="website" tabIndex={-1} autoComplete="off" />
          </label>
        </div>
        <label className={`contact-form-field${singleNameField ? ' sm:col-span-2' : ''}`}><span>{singleNameField ? 'Full Name' : 'First Name'} *</span>{withFieldIcon(<FiUser aria-hidden="true" />, <input required aria-label={singleNameField ? 'Full name' : 'First name'} className="input" name="firstName" placeholder={namePlaceholder ?? (singleNameField ? 'Full name*' : markRequiredNameFields ? 'First name*' : 'First name')} />)}</label>
        {singleNameField ? null : <label className="contact-form-field"><span>Last Name *</span>{withFieldIcon(<FiUser aria-hidden="true" />, <input required aria-label="Last name" className="input" name="lastName" placeholder={markRequiredNameFields ? 'Last name*' : 'Last name'} />)}</label>}
        <label className="contact-form-field"><span>Phone Number *</span>{withFieldIcon(<FiPhone aria-hidden="true" />, <input
          required
          aria-label="Phone"
          className="input"
          name="phone"
          placeholder={phonePlaceholder}
          type="tel"
          inputMode="numeric"
          autoComplete="tel"
          maxLength={17}
          pattern="\+1 \([0-9]{3}\) [0-9]{3}-[0-9]{4}"
          title="Enter a 10-digit US phone number"
          value={phoneValue}
          onChange={(event) => setPhoneValue(formatUsPhone(event.target.value))}
          onFocus={() => {
            if (!phoneValue) {
              setPhoneValue(COUNTRY_CODE_PREFIX)
            }
          }}
        />)}</label>
        <label className="contact-form-field"><span>Email Address {variant === 'contact' ? '*' : ''}</span>{withFieldIcon(<FiMail aria-hidden="true" />, <input required={variant === 'contact'} aria-label="Email" className="input" name="email" placeholder="Email" type="email" />)}</label>
        {inquiryOptions ? <label className="contact-form-field contact-form-field-wide"><span>How can we help? *</span>{withFieldIcon(<FiFileText aria-hidden="true" />, <><select required={variant === 'contact'} aria-label="What can we help you with?" className="input" name="inquiryType" defaultValue=""><option value="" disabled>Select a topic</option>{inquiryOptions.map((option) => <option key={option} value={option}>{option}</option>)}</select><FiChevronDown className="contact-field-chevron" aria-hidden="true" /></>)}</label> : null}
        {showVehicleInterest ? <label className="contact-form-field contact-form-field-wide"><span>Vehicle or Stock Number (optional)</span>{withFieldIcon(<FiFileText aria-hidden="true" />, <input aria-label="Vehicle or Stock Number (optional)" className="input" name="vehicleInterest" placeholder="Vehicle or Stock # (optional)" />)}</label> : null}
        <label className="contact-form-field contact-form-field-wide"><span>Message {variant === 'contact' ? '*' : ''}</span>{withFieldIcon(<FiMessageSquare aria-hidden="true" />, <textarea required={variant === 'contact'} aria-label="Message" className="input min-h-28" name="message" placeholder={messagePlaceholder} defaultValue={messageDefaultValue} />, 'contact-field-control--textarea')}</label>
      </div>
      <div className={`mt-5${actionAside ? ' form-actions-with-aside' : ''}`}>
        <button className="inline-flex min-h-11 w-full items-center justify-center gap-3 rounded-[3px] bg-[var(--color-primary)] px-5 py-3 text-sm font-bold text-white shadow-none transition hover:bg-[var(--color-primary-dark)] active:translate-y-px disabled:cursor-wait disabled:bg-[var(--color-disabled)] sm:w-auto" disabled={submitting} type="submit">
          {submitting ? 'Sending...' : <>{title} <FaArrowRight aria-hidden="true" /></>}
        </button>
        {actionAside}
      </div>
      {sent ? <p className="mt-4 rounded-md bg-[var(--color-hover)] px-4 py-3 text-sm font-normal text-[var(--color-link)]">Thanks. We received your request and will follow up shortly.</p> : null}
      {error ? <p className="mt-4 rounded-md bg-[var(--color-hover)] px-4 py-3 text-sm font-normal text-[var(--color-accent)]">{error}</p> : null}
    </motion.form>
  )
}
