import { apiClient } from './client'
import type { Equipment } from '../types/equipment'

type ApiEquipment = {
  id: string; slug: string; title: string; category: string; brand: string; model: string; year: number
  condition: string; status: string; stock_number: string | null; serial_number: string | null; price: number
  engine_hours: number | null; power_hp: number | null; location: string; short_description: string
  description?: string; images: string[]; images_total: number; features: string[]; specs: Record<string, string>; featured: boolean
}
type ListResponse = { items: ApiEquipment[]; total: number; page: number; page_size: number }
type ApiFilters = { categories: string[]; brands: string[]; years: number[]; conditions: string[]; statuses: string[]; price_min: number | null; price_max: number | null }
const origin = (() => { try { return new URL(apiClient.defaults.baseURL ?? '', window.location.origin).origin } catch { return window.location.origin } })()
const mapEquipment = (item: ApiEquipment): Equipment => ({
  id: item.id, slug: item.slug, year: item.year, make: item.brand, model: item.model, trim: item.condition,
  price: item.price, hours: item.engine_hours ?? 0, bodyType: item.category, condition: item.condition,
  engine: item.power_hp ? `${item.power_hp} hp` : '', vin: item.serial_number ?? '', stockNumber: item.stock_number ?? '',
  status: item.status, shortDescription: item.short_description, description: item.description ?? item.short_description,
  features: item.features, specs: item.specs ?? {}, images: (item.images.length ? item.images : []).map((path) => path.startsWith('/media/') ? `${origin}${path}` : path),
  imagesTotal: item.images_total, featured: item.featured,
})
export type EquipmentListParams = { page?: number; pageSize?: number; make?: string; model?: string; q?: string; yearFrom?: number; bodyType?: string; condition?: string; priceMin?: number; priceMax?: number; sort?: string }
export const listEquipment = async (params: EquipmentListParams = {}) => {
  const { data } = await apiClient.get<ListResponse>('/equipment', { params: {
    page: params.page, page_size: params.pageSize, brand: params.make || undefined, category: params.bodyType || undefined,
    year: params.yearFrom || undefined, condition: params.condition || undefined, q: params.q?.trim().length && params.q.trim().length >= 2 ? params.q.trim() : undefined,
    price_min: params.priceMin, price_max: params.priceMax,
  } })
  let items = data.items.map(mapEquipment)
  if (params.model) items = items.filter((item) => item.model === params.model)
  if (params.sort === 'price_asc') items.sort((a, b) => a.price - b.price)
  if (params.sort === 'price_desc') items.sort((a, b) => b.price - a.price)
  if (params.sort === 'hours_asc') items.sort((a, b) => a.hours - b.hours)
  return { items, total: data.total, page: data.page, pageSize: data.page_size }
}
export const getEquipment = async (slug: string) => {
  const { data } = await apiClient.get<ApiEquipment>(`/equipment/${slug}`, { params: { image_limit: 9 } })
  return mapEquipment(data)
}
export const listEquipmentImages = async (slug: string, offset = 0, limit = 8) => {
  const { data } = await apiClient.get<{items:string[];total:number;offset:number;limit:number;has_more:boolean}>(`/equipment/${slug}/images`, { params: { offset, limit } })
  return { ...data, items: data.items.map((path) => path.startsWith('/media/') ? `${origin}${path}` : path), hasMore: data.has_more }
}
export const getEquipmentFilters = async (brand?: string) => {
  const [{ data }, inventory] = await Promise.all([
    apiClient.get<ApiFilters>('/equipment/filters'),
    apiClient.get<ListResponse>('/equipment', { params: { brand: brand || undefined, page_size: 50 } }),
  ])
  const equipment = inventory.data.items
  return { brands: data.brands, models: [...new Set(equipment.map((item) => item.model))], years: data.years, bodyTypes: data.categories, conditions: data.conditions, prices: [...new Set(equipment.map((item) => item.price))].sort((a, b) => a - b), priceMin: data.price_min, priceMax: data.price_max, statuses: data.statuses }
}
