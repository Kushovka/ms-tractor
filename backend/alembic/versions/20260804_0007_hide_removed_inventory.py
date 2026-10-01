"""hide removed inventory vehicles

Revision ID: 20260804_0007
Revises: 20260803_0006
Create Date: 2026-08-04
"""

from alembic import op
import sqlalchemy as sa


revision = "20260804_0007"
down_revision = "20260803_0006"
branch_labels = None
depends_on = None


REMOVED_VEHICLE_IDS = (
    "2024-ford-f-150-raptor-r",
    "2025-ford-f-150-raptor",
    "2026-ram-1500-rho-crew-cab-4x4",
)


def upgrade() -> None:
    connection = op.get_bind()
    connection.execute(
        sa.text(
            "UPDATE vehicles "
            "SET status = :status, featured = false "
            "WHERE id IN :vehicle_ids"
        ).bindparams(sa.bindparam("vehicle_ids", expanding=True)),
        {"status": "Hidden", "vehicle_ids": REMOVED_VEHICLE_IDS},
    )


def downgrade() -> None:
    connection = op.get_bind()
    connection.execute(
        sa.text(
            "UPDATE vehicles "
            "SET status = :status "
            "WHERE id IN :vehicle_ids"
        ).bindparams(sa.bindparam("vehicle_ids", expanding=True)),
        {"status": "Available", "vehicle_ids": REMOVED_VEHICLE_IDS},
    )
