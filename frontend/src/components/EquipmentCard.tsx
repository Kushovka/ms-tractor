import { Link } from 'react-router'
import { FaArrowRight, FaCogs, FaPhoneAlt, FaTachometerAlt } from 'react-icons/fa'
import { business } from '../data/business'
import type { Equipment } from '../types/equipment'
import { trackContactCta } from '../utils/ctaTracking'
import { formatNumber, formatPrice } from '../utils/format'

export const EquipmentCard = ({ equipment }: { equipment: Equipment }) => {
  const title = `${equipment.year} ${equipment.make} ${equipment.model}`

  return <article className="equipment-card">
    <Link to={`/inventory/${equipment.slug}`} aria-label={`View ${title}`} className="equipment-card__image">
      <img src={equipment.images[0]} alt={title} loading="lazy" />
    </Link>
    <div className="equipment-card__body">
      <div className="equipment-card__eyebrow">
        <span>{equipment.condition || 'Equipment'}</span>
        {equipment.stockNumber ? <><i aria-hidden="true" /> <span>STK# {equipment.stockNumber}</span></> : null}
      </div>
      <Link to={`/inventory/${equipment.slug}`} className="equipment-card__title"><h3>{title}</h3></Link>
      <div className="equipment-card__specs">
        <strong className="equipment-card__price">{formatPrice(equipment.price)}</strong>
        <div className="equipment-card__spec"><FaTachometerAlt aria-hidden="true" /><span><b>{formatNumber(equipment.hours)}</b> Hours</span></div>
        <div className="equipment-card__spec"><FaCogs aria-hidden="true" /><span>{equipment.bodyType}</span></div>
      </div>
      <div className="equipment-card__actions">
        <Link to={`/inventory/${equipment.slug}`} className="equipment-card__details">View Details <FaArrowRight aria-hidden="true" /></Link>
        <a href={business.phoneHref} className="equipment-card__call" onClick={() => trackContactCta('phone_click', `Equipment Card Call ${equipment.stockNumber || equipment.slug}`)}><FaPhoneAlt aria-hidden="true" /><span>Call for Availability</span></a>
      </div>
    </div>
  </article>
}
