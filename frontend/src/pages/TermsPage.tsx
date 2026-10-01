import { SectionHeading } from '../components/SectionHeading'
import { Seo } from '../components/Seo'
import { business } from '../data/business'

const terms = [
  ['Website information', "Inventory, pricing, mileage, equipment, photos, availability, and vehicle details are provided for convenience and may change without notice. Confirm all details directly with M & S Tractor & Equipment before relying on them."],
  ['Vehicle availability', 'A vehicle is not held, reserved, or sold until the required dealership paperwork, payment, and approval steps are completed. Online inquiries do not create a purchase agreement.'],
  ['Pricing and fees', 'Listed prices may not include tax, title, registration, dealer documentation, lender fees, optional products, shipping, or other government and third-party charges unless specifically stated.'],
  ['Warranty and returns', 'Warranty, return, deductible, coverage, and exclusion details are controlled by the signed buyer documents and any warranty contract provided at purchase.'],
  ['Website use', 'Do not misuse the website, submit false information, interfere with service operation, or attempt unauthorized access to any systems.'],
]

export const TermsPage = () => (
  <>
    <Seo title="Terms" description="Review M & S Tractor & Equipment website terms for inventory, pricing, warranty, and website use." />
    <section className="section soft-band">
      <SectionHeading eyebrow="Terms" title="Website Terms" text="Important conditions for using the site and reviewing dealership information." />
      <div className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
        <div className="surface-card rounded-md p-6">
          <p className="eyebrow">Last updated: June 24, 2026</p>
          <div className="mt-6 grid gap-6">
            {terms.map(([title, text]) => (
              <div key={title} className="border-t border-[var(--color-border)] pt-5 first:border-t-0 first:pt-0">
                <h2 className="text-xl font-normal text-[var(--color-text)]">{title}</h2>
                <p className="mt-2 text-base font-normal leading-8 text-[var(--color-muted)]">{text}</p>
              </div>
            ))}
          </div>
          <div className="mt-8 rounded-md bg-[var(--color-section)] p-4 text-sm font-normal leading-7 text-[var(--color-muted)]">
            For current vehicle details or terms, contact {business.name} at{' '}
            <a className="font-normal text-[var(--color-link)]" href={business.phoneHref || business.contactHref}>{business.phone}</a>.
          </div>
        </div>
      </div>
    </section>
  </>
)
