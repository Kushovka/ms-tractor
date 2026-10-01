"""update bmw m2 price

Revision ID: 20260803_0006
Revises: 20260728_0005
Create Date: 2026-08-03
"""

from alembic import op
import sqlalchemy as sa


revision = "20260803_0006"
down_revision = "20260728_0005"
branch_labels = None
depends_on = None


def upgrade() -> None:
    connection = op.get_bind()
    connection.execute(
        sa.text("UPDATE vehicles SET price = :price WHERE id = :vehicle_id"),
        {"price": 46999, "vehicle_id": "2025-bmw-m2"},
    )


def downgrade() -> None:
    connection = op.get_bind()
    connection.execute(
        sa.text("UPDATE vehicles SET price = :price WHERE id = :vehicle_id"),
        {"price": 16999, "vehicle_id": "2025-bmw-m2"},
    )
