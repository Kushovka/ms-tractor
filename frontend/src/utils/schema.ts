import { business } from '../data/business'

export const localBusinessSchema = {
  '@context': 'https://schema.org',
  '@type': 'Store',
  name: business.name,
  address: {
    '@type': 'PostalAddress',
    streetAddress: business.address,
    addressLocality: 'Shreveport',
    addressRegion: 'LA',
    postalCode: business.postalCode,
    addressCountry: 'US',
  },
  url: business.website || business.mapsUrl,
  geo: {
    '@type': 'GeoCoordinates',
    latitude: business.latitude,
    longitude: business.longitude,
  },
  openingHours: 'Mo-Fr 08:00-17:00, Sa 08:00-12:00',
}
