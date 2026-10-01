from sqlalchemy import Select, func, or_, select
from sqlalchemy.orm import Session

from app.models.equipment import Equipment


def build_equipment_query(
    category: str | None = None,
    brand: str | None = None,
    year: int | None = None,
    condition: str | None = None,
    status: str | None = None,
    featured: bool | None = None,
    q: str | None = None,
    price_min: int | None = None,
    price_max: int | None = None,
) -> Select[tuple[Equipment]]:
    query = select(Equipment)

    if category:
        query = query.where(Equipment.category == category)
    if brand:
        query = query.where(Equipment.brand == brand)
    if year:
        query = query.where(Equipment.year == year)
    if condition:
        query = query.where(Equipment.condition == condition)
    if status:
        query = query.where(Equipment.status == status)
    if featured is not None:
        query = query.where(Equipment.featured == featured)
    if q:
        term = f"%{q.strip()}%"
        query = query.where(
            or_(
                Equipment.title.ilike(term),
                Equipment.brand.ilike(term),
                Equipment.model.ilike(term),
                Equipment.stock_number.ilike(term),
            )
        )
    if price_min is not None:
        query = query.where(Equipment.price >= price_min)
    if price_max is not None:
        query = query.where(Equipment.price <= price_max)

    return query.order_by(Equipment.year.desc(), Equipment.price.desc())


def list_equipment(
    db: Session,
    page: int = 1,
    page_size: int = 12,
    category: str | None = None,
    brand: str | None = None,
    year: int | None = None,
    condition: str | None = None,
    status: str | None = None,
    featured: bool | None = None,
    q: str | None = None,
    price_min: int | None = None,
    price_max: int | None = None,
) -> tuple[list[Equipment], int]:
    page = max(page, 1)
    page_size = min(max(page_size, 1), 50)
    query = build_equipment_query(
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
    total = db.scalar(select(func.count()).select_from(query.subquery())) or 0
    items = db.scalars(query.offset((page - 1) * page_size).limit(page_size)).all()
    return list(items), total


def get_equipment_by_slug(db: Session, slug: str) -> Equipment | None:
    return db.scalar(select(Equipment).where(Equipment.slug == slug))


def get_equipment_filters(db: Session) -> dict:
    categories = db.scalars(select(Equipment.category).distinct().order_by(Equipment.category)).all()
    brands = db.scalars(select(Equipment.brand).distinct().order_by(Equipment.brand)).all()
    years = db.scalars(select(Equipment.year).distinct().order_by(Equipment.year.desc())).all()
    conditions = db.scalars(select(Equipment.condition).distinct().order_by(Equipment.condition)).all()
    statuses = db.scalars(select(Equipment.status).distinct().order_by(Equipment.status)).all()
    price_min = db.scalar(select(func.min(Equipment.price)))
    price_max = db.scalar(select(func.max(Equipment.price)))

    return {
        "categories": list(categories),
        "brands": list(brands),
        "years": list(years),
        "conditions": list(conditions),
        "statuses": list(statuses),
        "price_min": price_min,
        "price_max": price_max,
    }
