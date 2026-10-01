"""Create inventory and leads tables.

Revision ID: 20260709_0001
Revises:
Create Date: 2026-07-09
"""

from alembic import op


revision = "20260709_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS vehicles (
            id VARCHAR PRIMARY KEY,
            slug VARCHAR NOT NULL UNIQUE,
            title VARCHAR NOT NULL,
            make VARCHAR NOT NULL,
            model VARCHAR NOT NULL,
            trim VARCHAR,
            year INTEGER NOT NULL,
            status VARCHAR NOT NULL,
            stock_number VARCHAR UNIQUE,
            vin VARCHAR UNIQUE,
            price INTEGER NOT NULL,
            mileage INTEGER NOT NULL,
            body_type VARCHAR NOT NULL,
            transmission VARCHAR,
            drivetrain VARCHAR,
            engine VARCHAR,
            exterior_color VARCHAR,
            interior_color VARCHAR,
            location VARCHAR NOT NULL,
            short_description VARCHAR NOT NULL,
            description TEXT NOT NULL,
            images JSON NOT NULL,
            features JSON NOT NULL,
            specs JSON NOT NULL,
            featured BOOLEAN NOT NULL,
            financing_available BOOLEAN NOT NULL,
            warranty_available BOOLEAN NOT NULL,
            delivery_available BOOLEAN NOT NULL,
            created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL
        )
        """
    )
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_slug ON vehicles (slug)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_make ON vehicles (make)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_model ON vehicles (model)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_year ON vehicles (year)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_status ON vehicles (status)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_stock_number ON vehicles (stock_number)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_vin ON vehicles (vin)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_price ON vehicles (price)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_mileage ON vehicles (mileage)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_body_type ON vehicles (body_type)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_transmission ON vehicles (transmission)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_drivetrain ON vehicles (drivetrain)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_exterior_color ON vehicles (exterior_color)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_vehicles_featured ON vehicles (featured)")

    op.execute(
        """
        CREATE TABLE IF NOT EXISTS leads (
            id VARCHAR PRIMARY KEY,
            vehicle_id VARCHAR REFERENCES vehicles(id),
            lead_type VARCHAR NOT NULL,
            customer_name VARCHAR NOT NULL,
            phone VARCHAR NOT NULL,
            email VARCHAR,
            subject VARCHAR,
            preferred_contact VARCHAR,
            zip_code VARCHAR,
            message TEXT,
            source_page VARCHAR,
            consent_to_contact BOOLEAN NOT NULL,
            created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL
        )
        """
    )


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS leads")
    op.execute("DROP TABLE IF EXISTS vehicles")
