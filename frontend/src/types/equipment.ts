export type Equipment = {
  id: string
  slug: string
  year: number
  make: string
  model: string
  trim: string
  price: number
  hours: number
  bodyType: string
  condition: string
  engine: string
  vin: string
  stockNumber: string
  status: string
  shortDescription: string
  description: string
  features: string[]
  specs: Record<string, string>
  images: string[]
  imagesTotal: number
  featured: boolean
}
