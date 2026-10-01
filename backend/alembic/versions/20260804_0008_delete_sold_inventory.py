"""delete sold inventory vehicles

Revision ID: 20260804_0008
Revises: 20260804_0007
Create Date: 2026-08-04
"""

from alembic import op
import sqlalchemy as sa


revision = "20260804_0008"
down_revision = "20260804_0007"
branch_labels = None
depends_on = None


SOLD_VEHICLE_IDS = (
    "2024-ford-f-150-raptor-r",
    "2025-ford-f-150-raptor",
    "2026-ram-1500-rho-crew-cab-4x4",
)


def upgrade() -> None:
    connection = op.get_bind()
    vehicle_ids = sa.bindparam("vehicle_ids", expanding=True)

    connection.execute(
        sa.text("UPDATE leads SET vehicle_id = NULL WHERE vehicle_id IN :vehicle_ids").bindparams(vehicle_ids),
        {"vehicle_ids": SOLD_VEHICLE_IDS},
    )
    connection.execute(
        sa.text("DELETE FROM vehicles WHERE id IN :vehicle_ids").bindparams(vehicle_ids),
        {"vehicle_ids": SOLD_VEHICLE_IDS},
    )


def downgrade() -> None:
    pass
