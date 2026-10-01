"""merge inventory migration heads

Revision ID: 20260923_0009
Revises: 20260804_0008, 20260923_0006
Create Date: 2026-09-23
"""

revision = "20260923_0009"
down_revision = ("20260804_0008", "20260923_0006")
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Join migration branches; schema and inventory data are unchanged here."""


def downgrade() -> None:
    """Alembic restores the two branch heads when this merge is downgraded."""
