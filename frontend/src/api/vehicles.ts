import { apiClient } from './client'
import type { Vehicle, VehicleDetails } from '../types/vehicle'

type ApiEquipment = {
  id: string; slug: string; title: string; category: string; brand: string; model: string
  year: number; condition: string; status: string; stock_number: string | null; serial_number: string | null
  price: number; engine_hours: number | null; engine_hours_label: string | null; power_hp: number | null
  location: string; short_description: string; description?: string; images: string[]; images_total: number
  features: string[]; specs: Record<string, unknown>; featured: boolean
}
type ListResponse = { items: ApiEquipment[]; total: number; page: number; page_size: number }
type ImagesResponse = { items: string[]; total: number; offset: number; limit: number; has_more: boolean }
export type VehicleListParams = { page?: number; pageSize?: number; make?: string; model?: string; q?: string; yearFrom?: number; yearTo?: number; bodyType?: string; transmission?: string; drivetrain?: string; color?: string; featured?: boolean; priceMin?: number; priceMax?: number; mileageMin?: number; mileageMax?: number; sort?: 'year_desc' | 'price_asc' | 'price_desc' | 'mileage_asc' }
export type VehicleFilters = { makes: string[]; models: string[]; years: number[]; bodyTypes: string[]; transmissions: string[]; drivetrains: string[]; colors: string[]; statuses: string[]; prices: number[]; priceMin: number | null; priceMax: number | null; mileageMin: number | null; mileageMax: number | null }
type ApiFilters = { categories: string[]; brands: string[]; years: number[]; conditions: string[]; statuses: string[]; price_min: number | null; price_max: number | null }

const apiOrigin = (() => { try { return new URL(apiClient.defaults.baseURL ?? '', window.location.origin).origin } catch { return window.location.origin } })()
const resolveImageUrl = (image: string) => image.startsWith('/media/') ? `${apiOrigin}${image}` : image
const details: VehicleDetails = { info: [], sections: [] }
const normalizeSpecs = (specs: Record<string, unknown>) => Object.fromEntries(Object.entries(specs).map(([key, value]) => [key, Array.isArray(value) ? value.join(', ') : String(value ?? '')]))
const toVehicle = (item: ApiEquipment): Vehicle => {
  const images = (item.images.length ? item.images : ['/images/vehicle-photo-coming-soon.webp']).map(resolveImageUrl)
  return {
    id: item.id, slug: item.slug, year: item.year, make: item.brand, model: item.model, trim: item.condition,
    price: item.price, mileage: item.engine_hours ?? 0, bodyType: item.category, transmission: '', drivetrain: item.condition,
    engine: item.power_hp ? `${item.power_hp} hp` : '', exteriorColor: '', interiorColor: '', vin: item.serial_number ?? '',
    stockNumber: item.stock_number ?? '', status: item.status, shortDescription: item.short_description,
    description: item.description ?? item.short_description, features: item.features, specs: normalizeSpecs(item.specs), images,
    imagesTotal: item.images_total || images.length, details, featured: item.featured,
    category: item.category, condition: item.condition, engineHours: item.engine_hours, powerHp: item.power_hp,
    location: item.location,
  }
}
const toParams = (params: VehicleListParams) => ({
  page: params.page, page_size: params.pageSize, brand: params.make || undefined, category: params.bodyType || undefined,
  year: params.yearFrom || undefined, condition: params.drivetrain || undefined, featured: params.featured,
  q: params.q?.trim().length && params.q.trim().length >= 2 ? params.q.trim() : undefined,
  price_min: params.priceMin, price_max: params.priceMax,
})

export const listVehicles = async (params: VehicleListParams = {}) => {
  const { data } = await apiClient.get<ListResponse>('/equipment', { params: toParams(params) })
  let items = data.items.map(toVehicle)
  if (params.model) items = items.filter((item) => item.model === params.model)
  if (params.sort === 'price_asc') items.sort((a, b) => a.price - b.price)
  if (params.sort === 'price_desc') items.sort((a, b) => b.price - a.price)
  if (params.sort === 'mileage_asc') items.sort((a, b) => a.mileage - b.mileage)
  return { items, total: data.total, page: data.page, pageSize: data.page_size }
}
export const getVehicle = async (slug: string) => {
  const { data } = await apiClient.get<ApiEquipment>(`/equipment/${slug}`, { params: { image_limit: 9 } })
  return toVehicle(data)
}
export const listVehicleImages = async (slug: string, offset = 0, limit = 8) => {
  const { data } = await apiClient.get<ImagesResponse>(`/equipment/${slug}/images`, { params: { offset, limit } })
  return { items: data.items.map(resolveImageUrl), total: data.total, offset: data.offset, limit: data.limit, hasMore: data.has_more }
}
export const getVehicleFilters = async (_make?: string): Promise<VehicleFilters> => {
  const { data } = await apiClient.get<ApiFilters>('/equipment/filters')
  return { makes: data.brands, models: [], years: data.years, bodyTypes: data.categories, transmissions: [], drivetrains: data.conditions, colors: [], statuses: data.statuses, prices: [], priceMin: data.price_min, priceMax: data.price_max, mileageMin: null, mileageMax: null }
}
