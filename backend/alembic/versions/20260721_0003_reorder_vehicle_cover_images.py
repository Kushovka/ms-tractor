"""Reorder vehicle cover images.

Revision ID: 20260721_0003
Revises: 20260721_0002
Create Date: 2026-07-21
"""

from alembic import op
import sqlalchemy as sa


revision = "20260721_0003"
down_revision = "20260721_0002"
branch_labels = None
depends_on = None


IMAGE_COUNTS = {
    "2015-dodge-challenger-srt-hellcat": 98,
    "2017-porsche-macan-gts": 264,
    "2020-range-rover-sport-svr": 111,
    "2021-ford-f-350-super-duty-platinum-4x4": 122,
    "2022-ford-f-150-lightning-lariat": 114,
    "2022-porsche-911-carrera-s-coupe": 116,
    "2025-bmw-m2": 215,
    "2025-bmw-m3-competition-xdrive": 100,
    "2025-ford-f-150-raptor": 55,
}

COVER_IMAGES = {
    "2015-dodge-challenger-srt-hellcat": "01.jpg",
    "2017-porsche-macan-gts": "01.jpg",
    "2020-range-rover-sport-svr": "01.jpg",
    "2021-ford-f-350-super-duty-platinum-4x4": "02.jpg",
    "2022-ford-f-150-lightning-lariat": "02.jpg",
    "2022-porsche-911-carrera-s-coupe": "05.jpg",
    "2025-bmw-m2": "01.jpg",
    "2025-bmw-m3-competition-xdrive": "01.jpg",
    "2025-ford-f-150-raptor": "01.jpg",
}


def vehicle_images(slug: str, cover_filename: str) -> list[str]:
    images = [f"/media/vehicles/{slug}/{index:02d}.jpg" for index in range(1, IMAGE_COUNTS[slug] + 1)]
    cover = f"/media/vehicles/{slug}/{cover_filename}"
    return [cover, *[image for image in images if image != cover]]


def vehicles_table() -> sa.Table:
    return sa.table(
        "vehicles",
        sa.column("id", sa.String),
        sa.column("images", sa.JSON),
    )


def upgrade() -> None:
    table = vehicles_table()
    connection = op.get_bind()

    for slug, cover_filename in COVER_IMAGES.items():
        connection.execute(
            table.update()
            .where(table.c.id == slug)
            .values(images=vehicle_images(slug, cover_filename))
        )


def downgrade() -> None:
    table = vehicles_table()
    connection = op.get_bind()

    for slug, count in IMAGE_COUNTS.items():
        connection.execute(
            table.update()
            .where(table.c.id == slug)
            .values(images=[f"/media/vehicles/{slug}/{index:02d}.jpg" for index in range(1, count + 1)])
        )
