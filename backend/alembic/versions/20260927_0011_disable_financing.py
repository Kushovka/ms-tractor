"""Disable financing for all vehicles.

Revision ID: 20260927_0011
Revises: 20260923_0010
Create Date: 2026-09-27
"""

from alembic import op


revision = "20260927_0011"
down_revision = "20260923_0010"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("UPDATE vehicles SET financing_available = FALSE")


def downgrade() -> None:
    op.execute("UPDATE vehicles SET financing_available = TRUE")
