import { useCallback, useEffect, useState } from 'react'
import { createPortal } from 'react-dom'
import { FaCamera, FaChevronLeft, FaChevronRight, FaExpand, FaImages, FaSearchPlus, FaTimes } from 'react-icons/fa'
import { listVehicleImages } from '../api/vehicles'

type VehicleGalleryProps = {
  images: string[]
  imagesTotal?: number
  slug: string
  title: string
  onShowPhotos: () => void
  showAllPhotos: boolean
}

const loadBatchSize = 6

export const VehicleGallery = ({ images, imagesTotal, slug, title, onShowPhotos, showAllPhotos }: VehicleGalleryProps) => {
  const [active, setActive] = useState(0)
  const [loadedImages, setLoadedImages] = useState(images)
  const [totalImages, setTotalImages] = useState(imagesTotal || images.length)
  const [imageLoading, setImageLoading] = useState(false)
  const [loadingMore, setLoadingMore] = useState(false)
  const [lightbox, setLightbox] = useState(false)
  const [zoomed, setZoomed] = useState(false)
  const [photosPortalReady, setPhotosPortalReady] = useState(false)
  const [touchStartX, setTouchStartX] = useState<number | null>(null)

  const currentImage = loadedImages[active] ?? loadedImages[0]
  const previewStart = Math.max(0, Math.min(active - 2, loadedImages.length - 6))
  const previewImages = loadedImages.map((image, index) => ({ image, index })).slice(previewStart, previewStart + 6)
  const photoGridTarget = document.getElementById('vehicle-photos-grid')

  useEffect(() => {
    setPhotosPortalReady(showAllPhotos)
  }, [showAllPhotos])

  useEffect(() => {
    setActive(0)
    setLoadedImages(images)
    setTotalImages(imagesTotal || images.length)
    setImageLoading(false)
    setLoadingMore(false)
    setZoomed(false)
  }, [images, imagesTotal, slug])

  const loadMoreImages = useCallback(async () => {
    if (loadingMore || loadedImages.length >= totalImages) return [] as string[]
    setLoadingMore(true)
    try {
      const response = await listVehicleImages(slug, loadedImages.length, loadBatchSize)
      const known = new Set(loadedImages)
      const additions = response.items.filter((image) => !known.has(image))
      setLoadedImages((current) => [...current, ...additions])
      setTotalImages(response.total)
      return additions
    } finally {
      setLoadingMore(false)
    }
  }, [loadedImages, loadingMore, slug, totalImages])

  useEffect(() => {
    if (images.length >= 7 || (imagesTotal ?? images.length) <= images.length) return undefined
    let cancelled = false
    void listVehicleImages(slug, images.length, Math.min(loadBatchSize, (imagesTotal ?? images.length) - images.length)).then((response) => {
      if (cancelled) return
      setLoadedImages((current) => {
        const known = new Set(current)
        return [...current, ...response.items.filter((image) => !known.has(image))]
      })
      setTotalImages(response.total)
    }).catch(() => undefined)
    return () => { cancelled = true }
  }, [images, imagesTotal, slug])

  const goTo = useCallback(async (index: number) => {
    const nextIndex = index < 0 ? totalImages - 1 : index >= totalImages ? 0 : index
    if (nextIndex < loadedImages.length) {
      setImageLoading(loadedImages[nextIndex] !== loadedImages[active])
      setActive(nextIndex)
      setZoomed(false)
      return
    }
    if (loadingMore) return
    setLoadingMore(true)
    try {
      const response = await listVehicleImages(slug, loadedImages.length, Math.max(loadBatchSize, nextIndex - loadedImages.length + 1))
      const known = new Set(loadedImages)
      const additions = response.items.filter((image) => !known.has(image))
      setLoadedImages((current) => [...current, ...additions])
      setTotalImages(response.total)
      if (nextIndex < loadedImages.length + additions.length) {
        setImageLoading(additions[nextIndex - loadedImages.length] !== loadedImages[active])
        setActive(nextIndex)
        setZoomed(false)
      }
    } finally {
      setLoadingMore(false)
    }
  }, [active, loadedImages, loadingMore, slug, totalImages])

  const previous = useCallback(() => { void goTo(active - 1) }, [active, goTo])
  const next = useCallback(() => { void goTo(active + 1) }, [active, goTo])

  useEffect(() => {
    if (!lightbox) return undefined
    const originalOverflow = document.body.style.overflow
    document.body.style.overflow = 'hidden'
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setLightbox(false)
      if (event.key === 'ArrowLeft') previous()
      if (event.key === 'ArrowRight') next()
    }
    window.addEventListener('keydown', handleKeyDown)
    return () => {
      document.body.style.overflow = originalOverflow
      window.removeEventListener('keydown', handleKeyDown)
    }
  }, [lightbox, next, previous])

  if (!currentImage) return <div className="min-h-[330px] bg-[var(--color-primary)]" />

  return <div className="lg:absolute lg:inset-x-8 lg:inset-y-5">
    <div className="vehicle-gallery__layout grid h-[370px] grid-cols-1 grid-rows-[minmax(0,1fr)_72px_48px] gap-2 border border-[var(--color-border)] bg-[var(--color-background)] p-2 sm:h-[430px] sm:grid-cols-[minmax(0,2.15fr)_minmax(180px,1fr)] sm:grid-rows-[minmax(0,1fr)_64px] sm:gap-3 sm:p-3 lg:h-full" onTouchStart={(event) => setTouchStartX(event.touches[0]?.clientX ?? null)} onTouchEnd={(event) => { if (touchStartX === null) return; const delta = event.changedTouches[0].clientX - touchStartX; if (Math.abs(delta) > 48) { if (delta > 0) previous(); else next() }; setTouchStartX(null) }}>
      <div className="vehicle-gallery__stage group relative row-start-1 min-h-0 overflow-hidden bg-[var(--color-background)] sm:row-span-2">
        <button aria-label="Open main vehicle photo" className="block h-full w-full" onClick={() => setLightbox(true)} type="button">
          <img src={currentImage} alt={title} className={`h-full w-full object-cover transition-opacity duration-200 ${imageLoading ? 'opacity-60' : 'opacity-100'}`} onLoad={() => setImageLoading(false)} onError={() => setImageLoading(false)} />
        </button>
        {loadedImages.length > 1 ? <>
          <button aria-label="Previous image" className="vehicle-gallery__nav vehicle-gallery__nav--previous absolute left-4 top-1/2 grid h-10 w-10 -translate-y-1/2 place-items-center rounded-md bg-black/75 text-sm text-white transition hover:bg-black disabled:opacity-40" disabled={loadingMore} onClick={previous} type="button"><FaChevronLeft /></button>
          <button aria-label="Next image" className="vehicle-gallery__nav vehicle-gallery__nav--next absolute right-4 top-1/2 grid h-10 w-10 -translate-y-1/2 place-items-center rounded-md bg-black/75 text-sm text-white transition hover:bg-black disabled:opacity-40" disabled={loadingMore} onClick={next} type="button"><FaChevronRight /></button>
        </> : null}
        <span className="vehicle-gallery__counter absolute bottom-3 left-3 inline-flex items-center gap-2 rounded-md bg-black/75 px-3 py-2 text-sm font-semibold text-white sm:bottom-4 sm:left-4"><FaCamera aria-hidden="true" />{active + 1} / {totalImages}</span>
        {loadingMore ? <span className="absolute bottom-3 left-28 bg-black/75 px-3 py-2 text-xs text-white sm:bottom-4 sm:left-32">Loading photos…</span> : null}
        <button aria-label="View fullscreen gallery" className="vehicle-gallery__fullscreen absolute bottom-3 right-3 grid h-10 w-10 place-items-center rounded-md bg-black/75 text-sm text-white transition hover:bg-black sm:bottom-4 sm:right-4" type="button" onClick={() => setLightbox(true)}><FaExpand /></button>
      </div>
      <div className="vehicle-gallery__thumbs row-start-2 grid min-h-0 grid-cols-3 gap-2 sm:hidden">{previewImages.slice(0, 3).map(({ image, index }) => <button key={`${image}-${index}`} aria-label={`View photo ${index + 1}`} aria-pressed={index === active} className={`relative min-w-0 overflow-hidden bg-[var(--color-primary)] ${index === active ? 'outline outline-2 outline-offset-[-2px] outline-[var(--color-primary)]' : ''}`} type="button" onClick={() => void goTo(index)}><img src={image} alt={`${title}, photo ${index + 1}`} className="h-full w-full object-cover" loading="lazy" /></button>)}</div>
      <div className="hidden min-h-0 grid-cols-2 grid-rows-3 gap-2 sm:col-start-2 sm:row-start-1 sm:grid">{previewImages.map(({ image, index }) => <button key={`${image}-${index}`} aria-label={`View photo ${index + 1}`} aria-pressed={index === active} className={`group relative min-h-0 overflow-hidden bg-[var(--color-primary)] ${index === active ? 'outline outline-2 outline-offset-[-2px] outline-[var(--color-primary)]' : ''}`} type="button" onClick={() => void goTo(index)}><img src={image} alt={`${title}, photo ${index + 1}`} className="h-full w-full object-cover transition duration-300 group-hover:scale-[1.03]" loading="lazy" /></button>)}</div>
      <button className="vehicle-gallery__all-photos row-start-3 inline-flex min-h-0 items-center justify-center gap-2 border border-[var(--color-primary)] px-3 text-[11px] font-bold uppercase tracking-wide text-[var(--color-primary)] transition hover:bg-[var(--color-hover)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--color-primary)] sm:col-start-2 sm:row-start-2 sm:gap-3 sm:text-sm" type="button" onClick={() => { onShowPhotos(); void loadMoreImages() }}><FaImages className="shrink-0 text-lg" /><span>View all {totalImages} photos</span></button>
    </div>
    {showAllPhotos && photosPortalReady && photoGridTarget ? createPortal(<div>
      <div className="mb-3 flex items-center justify-between gap-3"><p className="text-sm font-semibold text-[var(--color-primary)]">All photos</p><span className="text-xs text-[var(--color-muted)]">{loadedImages.length} of {totalImages}</span></div>
      <div className="grid grid-cols-3 gap-2 sm:grid-cols-4 lg:grid-cols-6">{loadedImages.map((image, index) => <button key={`${image}-${index}`} aria-label={`Show image ${index + 1}`} onClick={() => { void goTo(index); setLightbox(true) }} type="button" className={`aspect-[4/3] overflow-hidden border-2 bg-[var(--color-primary)] transition ${active === index ? 'border-[var(--color-accent)]' : 'border-transparent opacity-80 hover:opacity-100'}`}><img src={image} alt={`${title} thumbnail ${index + 1}`} className="h-full w-full object-cover" loading="lazy" /></button>)}</div>
      {loadedImages.length < totalImages ? <button className="mt-4 min-h-11 w-full border border-[var(--color-border)] bg-[var(--color-surface)] px-5 text-sm font-medium text-[var(--color-primary)] transition hover:border-[var(--color-primary)] hover:bg-[var(--color-hover)] disabled:opacity-70" disabled={loadingMore} onClick={() => void loadMoreImages()} type="button">{loadingMore ? 'Loading photos…' : `Load ${Math.min(loadBatchSize, totalImages - loadedImages.length)} more photos (${loadedImages.length} of ${totalImages})`}</button> : null}
    </div>, photoGridTarget) : null}
    {lightbox ? <div className="fixed inset-0 z-[70] bg-black/95 p-4" onClick={() => setLightbox(false)}>
      <button aria-label="Close gallery" className="absolute right-5 top-5 z-10 grid h-10 w-10 place-items-center rounded-full border border-white/15 bg-white/10 text-sm text-white transition hover:bg-white/20" onClick={() => setLightbox(false)} type="button"><FaTimes /></button>
      {totalImages > 1 ? <>
        <button aria-label="Previous image" className="absolute left-5 top-1/2 z-10 grid h-11 w-11 -translate-y-1/2 place-items-center rounded-full border border-white/15 bg-white/10 text-sm text-white transition hover:bg-white/20 disabled:opacity-35" disabled={loadingMore} onClick={(event) => { event.stopPropagation(); previous() }} type="button"><FaChevronLeft /></button>
        <button aria-label="Next image" className="absolute right-5 top-1/2 z-10 grid h-11 w-11 -translate-y-1/2 place-items-center rounded-full border border-white/15 bg-white/10 text-sm text-white transition hover:bg-white/20 disabled:opacity-35" disabled={loadingMore} onClick={(event) => { event.stopPropagation(); next() }} type="button"><FaChevronRight /></button>
      </> : null}
      <button aria-label={zoomed ? 'Zoom out' : 'Zoom in'} className="absolute bottom-5 left-1/2 z-10 grid h-10 w-10 -translate-x-1/2 place-items-center rounded-full border border-white/15 bg-white/10 text-sm text-white transition hover:bg-white/20" onClick={(event) => { event.stopPropagation(); setZoomed((value) => !value) }} type="button"><FaSearchPlus className={zoomed ? 'scale-90 opacity-70' : ''} /></button>
      <div className="flex h-full items-center justify-center overflow-auto px-8 py-12 sm:px-12"><img src={currentImage} alt={title} className={`${zoomed ? 'max-h-none max-w-none scale-150' : 'max-h-[84vh] w-full max-w-6xl'} object-contain transition duration-200 ${imageLoading ? 'opacity-55' : 'opacity-100'}`} onLoad={() => setImageLoading(false)} onError={() => setImageLoading(false)} onClick={(event) => { event.stopPropagation(); setZoomed((value) => !value) }} /></div>
      <span className="absolute bottom-5 right-5 rounded-full border border-white/10 bg-white/10 px-3 py-1.5 text-xs text-white">{active + 1} / {totalImages}</span>
    </div> : null}
  </div>
}
