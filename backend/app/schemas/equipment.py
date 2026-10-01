from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class EquipmentBase(BaseModel):
    slug: str
    title: str
    category: str
    brand: str
    model: str
    year: int
    condition: str
    status: str = "Available"
    stock_number: str | None = None
    serial_number: str | None = None
    price: int
    engine_hours: int | None = None
    engine_hours_label: str | None = None
    power_hp: int | None = None
    location: str
    short_description: str
    images: list[str] = Field(default_factory=list)
    images_total: int = 0
    features: list[str] = Field(default_factory=list)
    specs: dict = Field(default_factory=dict)
    featured: bool = False
    financing_available: bool = True
    delivery_available: bool = True


class EquipmentListItem(EquipmentBase):
    id: str

    model_config = ConfigDict(from_attributes=True)


class EquipmentDetail(EquipmentBase):
    id: str
    description: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class EquipmentListResponse(BaseModel):
    items: list[EquipmentListItem]
    total: int
    page: int
    page_size: int


class EquipmentImagesResponse(BaseModel):
    items: list[str]
    total: int
    offset: int
    limit: int
    has_more: bool


class EquipmentFilters(BaseModel):
    categories: list[str]
    brands: list[str]
    years: list[int]
    conditions: list[str]
    statuses: list[str]
    price_min: int | None = None
    price_max: int | None = None
