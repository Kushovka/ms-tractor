"""Replace active vehicle inventory with farm equipment listings."""

from datetime import datetime
import json
from pathlib import Path

from alembic import op
import sqlalchemy as sa


revision = "20260930_0014"
down_revision = "20260928_0013"
branch_labels = None
depends_on = None


def equipment_table():
    return sa.Table(
        "equipment",
        sa.MetaData(),
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("slug", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        sa.Column("brand", sa.String(), nullable=False),
        sa.Column("model", sa.String(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("condition", sa.String(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("stock_number", sa.String()),
        sa.Column("serial_number", sa.String()),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("engine_hours", sa.Integer()),
        sa.Column("power_hp", sa.Integer()),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("short_description", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("images", sa.JSON(), nullable=False),
        sa.Column("features", sa.JSON(), nullable=False),
        sa.Column("specs", sa.JSON(), nullable=False),
        sa.Column("featured", sa.Boolean(), nullable=False),
        sa.Column("financing_available", sa.Boolean(), nullable=False),
        sa.Column("delivery_available", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )


def upgrade():
    op.create_table(
        "equipment",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("slug", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False),
        sa.Column("brand", sa.String(), nullable=False),
        sa.Column("model", sa.String(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("condition", sa.String(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("stock_number", sa.String()),
        sa.Column("serial_number", sa.String()),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("engine_hours", sa.Integer()),
        sa.Column("power_hp", sa.Integer()),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("short_description", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("images", sa.JSON(), nullable=False),
        sa.Column("features", sa.JSON(), nullable=False),
        sa.Column("specs", sa.JSON(), nullable=False),
        sa.Column("featured", sa.Boolean(), nullable=False),
        sa.Column("financing_available", sa.Boolean(), nullable=False),
        sa.Column("delivery_available", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.create_index("ix_equipment_slug", "equipment", ["slug"], unique=True)
    for column in ("category", "brand", "year", "condition", "status", "price", "featured"):
        op.create_index(f"ix_equipment_{column}", "equipment", [column])
    op.create_index("ix_equipment_stock_number", "equipment", ["stock_number"], unique=True)

    seed_path = Path(__file__).resolve().parents[2] / "app" / "data" / "equipment_seed.json"
    rows = json.loads(seed_path.read_text())
    created_at = datetime.utcnow()
    op.bulk_insert(equipment_table(), [{**row, "created_at": created_at} for row in rows])

    op.drop_constraint("leads_vehicle_id_fkey", "leads", type_="foreignkey")
    op.execute(sa.text("UPDATE leads SET vehicle_id = NULL WHERE vehicle_id IS NOT NULL"))
    op.alter_column("leads", "vehicle_id", new_column_name="equipment_id")
    op.create_foreign_key("leads_equipment_id_fkey", "leads", "equipment", ["equipment_id"], ["id"])
    op.drop_table("vehicles")


def downgrade():
    op.create_table(
        "vehicles",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("slug", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("make", sa.String(), nullable=False),
        sa.Column("model", sa.String(), nullable=False),
        sa.Column("trim", sa.String()),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("stock_number", sa.String()),
        sa.Column("vin", sa.String()),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("mileage", sa.Integer(), nullable=False),
        sa.Column("body_type", sa.String(), nullable=False),
        sa.Column("transmission", sa.String()),
        sa.Column("drivetrain", sa.String()),
        sa.Column("engine", sa.String()),
        sa.Column("exterior_color", sa.String()),
        sa.Column("interior_color", sa.String()),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("short_description", sa.String(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("images", sa.JSON(), nullable=False),
        sa.Column("features", sa.JSON(), nullable=False),
        sa.Column("specs", sa.JSON(), nullable=False),
        sa.Column("details", sa.JSON(), nullable=False),
        sa.Column("featured", sa.Boolean(), nullable=False),
        sa.Column("financing_available", sa.Boolean(), nullable=False),
        sa.Column("warranty_available", sa.Boolean(), nullable=False),
        sa.Column("delivery_available", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )
    op.drop_constraint("leads_equipment_id_fkey", "leads", type_="foreignkey")
    op.execute(sa.text("UPDATE leads SET equipment_id = NULL WHERE equipment_id IS NOT NULL"))
    op.alter_column("leads", "equipment_id", new_column_name="vehicle_id")
    op.create_foreign_key("leads_vehicle_id_fkey", "leads", "vehicles", ["vehicle_id"], ["id"])
    op.drop_table("equipment")
