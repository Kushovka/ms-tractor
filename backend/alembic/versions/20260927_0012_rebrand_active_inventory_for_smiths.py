"""Replace legacy dealer metadata in the active Smith's inventory.

Revision ID: 20260927_0012
Revises: 20260927_0011
Create Date: 2026-09-27
"""

from alembic import op


revision = "20260927_0012"
down_revision = "20260927_0011"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        "UPDATE vehicles "
        "SET location = 'Commodore, PA', stock_number = NULL"
    )


def downgrade() -> None:
    """Do not restore metadata from the previous dealer site."""
