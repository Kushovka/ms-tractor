from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.schemas.equipment import (
    EquipmentDetail,
    EquipmentFilters,
    EquipmentImagesResponse,
    EquipmentListResponse,
)
from app.services.equipment_service import (
    get_equipment_by_slug,
    get_equipment_filters,
    list_equipment,
)

router = APIRouter(prefix="/equipment", tags=["equipment"])
MEDIA_ROOT = Path("app/static/media").resolve()


def media_file_exists(path: str) -> bool:
    if not path.startswith("/media/"):
        return True

    relative_parts = path.removeprefix("/media/").split("/")
    file_path = (MEDIA_ROOT.joinpath(*relative_parts)).resolve()

    try:
        file_path.relative_to(MEDIA_ROOT)
    except ValueError:
        return False

    return file_path.is_file()


def existing_images(images: list[str] | None) -> list[str]:
    return [image for image in images or [] if media_file_exists(image)]


def serialize_equipment(equipment, image_limit: int | None = None) -> dict:
    all_images = existing_images(equipment.images)
    images = all_images
    if image_limit is not None:
        images = images[:image_limit]
    engine_hours_label = (
        f"{equipment.engine_hours:,} on meter" if equipment.engine_hours is not None else None
    )

    return {
        "id": equipment.id,
        "slug": equipment.slug,
        "title": equipment.title,
        "category": equipment.category,
        "brand": equipment.brand,
        "model": equipment.model,
        "year": equipment.year,
        "condition": equipment.condition,
        "status": equipment.status,
        "stock_number": equipment.stock_number,
        "serial_number": equipment.serial_number,
        "price": equipment.price,
        "engine_hours": equipment.engine_hours,
        "engine_hours_label": engine_hours_label,
        "power_hp": equipment.power_hp,
        "location": equipment.location,
        "short_description": equipment.short_description,
        "images": images,
        "images_total": len(all_images),
        "features": equipment.features or [],
        "specs": equipment.specs or {},
        "featured": equipment.featured,
        "financing_available": equipment.financing_available,
        "delivery_available": equipment.delivery_available,
    }


@router.get("", response_model=EquipmentListResponse)
def get_equipment_list(
    page: int = Query(1, ge=1),
    page_size: int = Query(12, ge=1, le=50),
    category: str | None = None,
    brand: str | None = None,
    year: int | None = None,
    condition: str | None = None,
    status: str | None = None,
    featured: bool | None = None,
    q: str | None = Query(None, min_length=2),
    price_min: int | None = Query(None, ge=0),
    price_max: int | None = Query(None, ge=0),
    db: Session = Depends(get_db),
):
    items, total = list_equipment(
        db=db,
        page=page,
        page_size=page_size,
        category=category,
        brand=brand,
        year=year,
        condition=condition,
        status=status,
        featured=featured,
        q=q,
        price_min=price_min,
        price_max=price_max,
    )
    return {
        "items": [serialize_equipment(item, image_limit=1) for item in items],
        "total": total,
        "page": page,
        "page_size": page_size,
    }


@router.get("/filters", response_model=EquipmentFilters)
def get_filters(db: Session = Depends(get_db)):
    return get_equipment_filters(db)


@router.get("/{slug}/images", response_model=EquipmentImagesResponse)
def get_equipment_images(
    slug: str,
    offset: int = Query(0, ge=0),
    limit: int = Query(12, ge=1, le=48),
    db: Session = Depends(get_db),
):
    equipment = get_equipment_by_slug(db, slug)
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")

    images = existing_images(equipment.images)
    items = images[offset : offset + limit]
    next_offset = offset + len(items)
    return {
        "items": items,
        "total": len(images),
        "offset": offset,
        "limit": limit,
        "has_more": next_offset < len(images),
    }


@router.get("/{slug}", response_model=EquipmentDetail)
def get_equipment_detail(
    slug: str,
    image_limit: int = Query(12, ge=1, le=80),
    db: Session = Depends(get_db),
):
    equipment = get_equipment_by_slug(db, slug)
    if not equipment:
        raise HTTPException(status_code=404, detail="Equipment not found")
    payload = serialize_equipment(equipment, image_limit=image_limit)
    payload["description"] = equipment.description
    payload["created_at"] = equipment.created_at
    return payload
