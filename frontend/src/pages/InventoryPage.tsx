import { useEffect, useRef, useState } from 'react'
import { useSearchParams } from 'react-router'
import { FaChevronDown, FaChevronLeft, FaChevronRight, FaSlidersH } from 'react-icons/fa'
import { getEquipmentFilters, listEquipment } from '../api/equipment'
import { EquipmentCard } from '../components/EquipmentCard'
import { Seo } from '../components/Seo'
import { EquipmentGridSkeleton } from '../components/Skeletons'
import type { Equipment } from '../types/equipment'

type SortKey = 'price-low' | 'price-high' | 'year' | 'hours'
const PAGE_SIZE = 12
const toNumber = (value: string) => value === '' ? undefined : Number(value)
const numberValue = (value?: number) => value?.toString() ?? ''
const queryNumber = (value: string | null) => {
  if (!value) return undefined
  const parsed = Number(value)
  return Number.isFinite(parsed) && parsed >= 0 ? parsed : undefined
}

export const InventoryPage = () => {
  const [searchParams] = useSearchParams()
  const resultsRef = useRef<HTMLDivElement | null>(null)
  const [make, setBrand] = useState(() => searchParams.get('make') ?? '')
  const [model, setModel] = useState(() => searchParams.get('model') ?? '')
  const [yearFrom, setYearFrom] = useState<number | undefined>(() => queryNumber(searchParams.get('yearFrom')))
  const [priceMin, setPriceMin] = useState<number | undefined>(() => queryNumber(searchParams.get('priceMin')))
  const [priceMax, setPriceMax] = useState<number | undefined>(() => queryNumber(searchParams.get('priceMax')))
  const [bodyType, setBodyType] = useState(() => searchParams.get('bodyType') ?? '')
  const [condition, setCondition] = useState('')
  const [search, setSearch] = useState('')
  const [sort, setSort] = useState<SortKey>('year')
  const [page, setPage] = useState(1)
  const [items, setItems] = useState<Equipment[]>([])
  const [total, setTotal] = useState(0)
  const [categoryCounts, setCategoryCounts] = useState<Record<string, number> | null>(null)
  const [loading, setLoading] = useState(true)
  const [inventoryError, setInventoryError] = useState(false)
  const [brands, setBrands] = useState<string[]>([])
  const [years, setYears] = useState<number[]>([])
  const [bodyTypes, setBodyTypes] = useState<string[]>([])
  const [conditions, setConditions] = useState<string[]>([])
  const [filtersOpen, setFiltersOpen] = useState(false)

  useEffect(() => {
    setSearch(searchParams.get('q') ?? '')
    setBodyType(searchParams.get('bodyType') ?? '')
    setPage(1)
  }, [searchParams])

  useEffect(() => {
    let cancelled = false
    getEquipmentFilters().then((filters) => {
      if (!cancelled) {
        const categoryOrder = ['Tractors', 'Skid Steers', 'Backhoes']
        setBrands(filters.brands)
        setYears(filters.years)
        setBodyTypes([...filters.bodyTypes].sort((a, b) => categoryOrder.indexOf(a) - categoryOrder.indexOf(b)))
        setConditions(filters.conditions)
      }
    }).catch(() => undefined)
    return () => { cancelled = true }
  }, [])
  useEffect(() => {
    let cancelled = false
    Promise.resolve().then(() => { if (!cancelled) setLoading(true) })
    listEquipment({ make, model, q: search, yearFrom, bodyType, condition, priceMin, priceMax, page, pageSize: PAGE_SIZE, sort: sort === 'price-low' ? 'price_asc' : sort === 'price-high' ? 'price_desc' : sort === 'hours' ? 'hours_asc' : 'year_desc' })
      .then((response) => { if (!cancelled) { setItems(response.items); setTotal(response.total); setInventoryError(false) } })
      .catch(() => { if (!cancelled) { setItems([]); setTotal(0); setInventoryError(true) } })
      .finally(() => { if (!cancelled) setLoading(false) })
    return () => { cancelled = true }
  }, [bodyType, condition, make, model, page, priceMax, priceMin, search, sort, yearFrom])

  useEffect(() => {
    let cancelled = false
    setCategoryCounts(null)
    const countFilters = { make, model, q: search, yearFrom, condition, priceMin, priceMax, page: 1, pageSize: 1 }
    Promise.all([
      listEquipment(countFilters),
      ...bodyTypes.map((type) => listEquipment({ ...countFilters, bodyType: type })),
    ]).then(([allEquipment, ...typeResponses]) => {
      if (cancelled) return
      const counts: Record<string, number> = { all: allEquipment.total }
      bodyTypes.forEach((type, index) => { counts[type] = typeResponses[index]?.total ?? 0 })
      setCategoryCounts(counts)
    }).catch(() => { if (!cancelled) setCategoryCounts(null) })
    return () => { cancelled = true }
  }, [bodyTypes, condition, make, model, priceMax, priceMin, search, yearFrom])

  const resetFilters = () => { setPage(1); setBrand(''); setModel(''); setSearch(''); setYearFrom(undefined); setPriceMin(undefined); setPriceMax(undefined); setBodyType(''); setCondition('') }
  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE))
  const pageNumbers = Array.from({ length: totalPages }, (_, index) => index + 1)
  const goToPage = (nextPage: number) => { setPage(Math.min(totalPages, Math.max(1, nextPage))); window.setTimeout(() => resultsRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' }), 0) }
  const filterChange = <T,>(setter: (value: T) => void, value: T) => { setPage(1); setter(value) }
  const filters = <aside className={`inventory-filters ${filtersOpen ? 'block' : 'hidden'} h-fit lg:block`}>
    <button type="button" className="flex min-h-11 w-full items-center justify-between gap-3 text-left lg:hidden" aria-expanded={filtersOpen} aria-controls="inventory-filters" onClick={() => setFiltersOpen((open) => !open)}>
      <span className="flex items-center gap-2"><FaSlidersH /><span className="text-[11px] font-bold uppercase tracking-[0.15em]">Refine results</span></span>
      <FaChevronDown className={`transition-transform ${filtersOpen ? 'rotate-180' : ''}`} />
    </button>
    <div className="inventory-filters__heading hidden items-center justify-between border-b pb-3 lg:flex"><h2>Refine Results</h2><button type="button" onClick={resetFilters}>Clear All</button></div>
    <div id="inventory-filters" className={`${filtersOpen ? 'block' : 'hidden'} lg:block`}>
    <fieldset className="inventory-filter-group"><legend>Category</legend>{bodyTypes.map((item) => <label key={item}><input type="radio" name="category" checked={bodyType === item} onChange={() => filterChange(setBodyType, item)} /><span>{item}</span><small>{categoryCounts?.[item] ?? '—'}</small></label>)}</fieldset>
    {conditions.length ? <fieldset className="inventory-filter-group"><legend>Condition</legend>{conditions.map((item) => <label key={item}><input type="radio" name="condition" checked={condition === item} onChange={() => filterChange(setCondition, item)} /><span>{item}</span></label>)}</fieldset> : null}
    {brands.length ? <fieldset className="inventory-filter-group"><legend>Brand</legend>{brands.map((item) => <label key={item}><input type="radio" name="brand" checked={make === item} onChange={() => { filterChange(setBrand, item); setModel('') }} /><span>{item}</span></label>)}</fieldset> : null}
    <div className="inventory-filter-group"><span className="inventory-filter-group__legend">Price</span><div className="inventory-filter-range"><label><span className="sr-only">Minimum price</span><input type="number" min="0" placeholder="Min Price" value={numberValue(priceMin)} onChange={(event) => filterChange(setPriceMin, toNumber(event.target.value))} /></label><label><span className="sr-only">Maximum price</span><input type="number" min="0" placeholder="Max Price" value={numberValue(priceMax)} onChange={(event) => filterChange(setPriceMax, toNumber(event.target.value))} /></label></div></div>
    <label className="inventory-filter-group inventory-filter-select">Year<select value={numberValue(yearFrom)} onChange={(event) => filterChange(setYearFrom, toNumber(event.target.value))}><option value="">Any year</option>{years.map((item) => <option key={item} value={item}>{item}</option>)}</select></label>
    <button className="inventory-filter-apply" onClick={() => resultsRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })} type="button">Apply Filters</button>
    <button className="inventory-filter-clear lg:hidden" onClick={resetFilters} type="button">Clear All Filters</button>
    </div>
  </aside>

  return <>
    <Seo title="Farm Equipment Inventory" description="Browse current farm equipment listings at M & S Tractor & Equipment in Shreveport, LA." />
    <section className="inventory-page px-5 pb-10 pt-5 sm:px-8 sm:pt-6 lg:px-[clamp(24px,3.9vw,58px)] lg:pt-2"><div className="mx-auto w-full max-w-[1680px]">
      <header className="inventory-intro"><h1>Current Inventory</h1><p>Browse available equipment with listing details and current prices.</p><img className="inventory-intro__art" src="/images/inventory-farm-panorama-transparent.webp" alt="" aria-hidden="true" /></header>
      <nav aria-label="Equipment categories" className="inventory-category-tabs">
        <button type="button" onClick={() => { filterChange(setBodyType, ''); setBrand(''); setModel('') }} className={!bodyType ? 'is-active' : ''}>All Equipment <span>{categoryCounts?.all ?? '—'}</span></button>
        {bodyTypes.map((type) => <button key={type} type="button" onClick={() => { filterChange(setBodyType, type); setBrand(''); setModel('') }} className={bodyType === type ? 'is-active' : ''}>{type}<span>{categoryCounts?.[type] ?? '—'}</span></button>)}
      </nav>
      <div className="inventory-workspace">
      <div className="hidden lg:block">{filters}</div>
      <div className="inventory-results">
        <div className="inventory-toolbar">
          <span className="inventory-total inventory-toolbar-total">{loading ? 'Loading…' : `${total} Equipment Listings`}</span>
          <label className="inventory-sort inventory-toolbar-sort">Sort by:<select value={sort} onChange={(event) => filterChange(setSort, event.target.value as SortKey)}><option value="year">Newest First</option><option value="price-low">Price: Low to High</option><option value="price-high">Price: High to Low</option><option value="hours">Lowest Hours</option></select></label>
          <button className="inventory-mobile-filters lg:hidden" type="button" aria-expanded={filtersOpen} aria-controls="mobile-inventory-filters" onClick={() => setFiltersOpen((open) => !open)}><span><FaSlidersH /> Filters</span><FaChevronDown className={filtersOpen ? 'rotate-180' : ''} /></button>
        </div>
        {filtersOpen ? <div id="mobile-inventory-filters" className="inventory-mobile-filter-panel lg:hidden">{filters}</div> : null}
        <div ref={resultsRef} className="mt-2 min-w-0 scroll-mt-[calc(var(--header-height)+1rem)]">
        <div className="inventory-mobile-meta mb-3 flex items-center justify-between gap-3 pt-2 sm:hidden">
          <label className="inventory-sort inventory-mobile-sort">Sort by:<select value={sort} onChange={(event) => filterChange(setSort, event.target.value as SortKey)}><option value="year">Newest First</option><option value="price-low">Price: Low to High</option><option value="price-high">Price: High to Low</option><option value="hours">Lowest Hours</option></select></label>
          <span className="text-[11px] text-[var(--color-muted)]">{loading ? 'Loading…' : `${total} equipment`}</span>
        </div>
        <div className="grid items-stretch gap-2 sm:grid-cols-2 xl:grid-cols-3">{loading ? <EquipmentGridSkeleton count={PAGE_SIZE} /> : inventoryError ? <div className="border border-[var(--color-border)] bg-[var(--color-surface)] p-7 text-center text-sm text-[var(--color-muted)]">Inventory is temporarily unavailable. Please try again later or call us for current equipment.</div> : items.length ? items.map((equipment) => <EquipmentCard key={equipment.id} equipment={equipment} />) : <div className="border border-[var(--color-border)] bg-[var(--color-surface)] p-7 text-center text-sm text-[var(--color-muted)]">No equipment match these filters right now.</div>}</div>
        {!loading && totalPages > 1 ? <div className="relative mt-7 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-center"><div className="flex items-center justify-center gap-1.5"><button aria-label="Previous page" className="grid h-8 w-8 place-items-center border border-[var(--color-border)] transition hover:bg-[var(--color-section)] disabled:opacity-35" disabled={page === 1} onClick={() => goToPage(page - 1)} type="button"><FaChevronLeft /></button>{pageNumbers.map((pageNumber) => <button key={pageNumber} aria-label={`Page ${pageNumber}`} className={`grid h-8 min-w-8 place-items-center px-2 text-[11px] ${pageNumber === page ? 'bg-[var(--color-primary)] text-white' : 'hover:bg-[var(--color-section)]'}`} onClick={() => goToPage(pageNumber)} type="button">{pageNumber}</button>)}<button aria-label="Next page" className="grid h-8 w-8 place-items-center border border-[var(--color-border)] transition hover:bg-[var(--color-section)] disabled:opacity-35" disabled={page === totalPages} onClick={() => goToPage(page + 1)} type="button"><FaChevronRight /></button></div><p className="text-center text-[10px] text-[var(--color-muted)] sm:absolute sm:right-0">Showing {((page - 1) * PAGE_SIZE) + 1}-{Math.min(page * PAGE_SIZE, total)} of {total} equipment</p></div> : null}
        </div>
      </div>
      </div>
      </div>
    </section>
  </>
}
