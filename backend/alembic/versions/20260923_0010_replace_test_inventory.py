"""Seed the current Smith's Sales & Services vehicle inventory.

Revision ID: 20260923_0010
Revises: 20260923_0009
Create Date: 2026-09-23
"""

from datetime import datetime
from pathlib import Path
from typing import Optional

from alembic import op
import sqlalchemy as sa


revision = "20260923_0010"
down_revision = "20260923_0009"
branch_labels = None
depends_on = None


CREATED_AT = datetime(2026, 9, 23)
MEDIA_ROOT = Path(__file__).resolve().parents[2] / "app" / "static" / "media" / "vehicles"


def media_images(slug: str) -> list[str]:
    """Expose every supplied site photo and omit caller-only files."""
    folder = MEDIA_ROOT / slug
    if not folder.is_dir():
        return []
    return [
        f"/media/vehicles/{slug}/{image.name}"
        for image in sorted(folder.iterdir(), key=lambda item: item.name.lower())
        if image.is_file() and image.suffix.lower() in {".webp"}
    ]


def vehicle(
    slug: str, title: str, make: str, model: str, trim: str, year: int, price: int,
    mileage: int, body_type: str, engine: str, drivetrain: str, exterior: str,
    interior: str, vin: Optional[str], features: list[str], description: str,
) -> dict:
    images = media_images(slug)
    return {
        "id": slug,
        "slug": slug,
        "title": title,
        "make": make,
        "model": model,
        "trim": trim,
        "year": year,
        "status": "Available",
        "stock_number": None,
        "vin": vin,
        "price": price,
        "mileage": mileage,
        "body_type": body_type,
        "transmission": "Automatic",
        "drivetrain": drivetrain,
        "engine": engine,
        "exterior_color": exterior,
        "interior_color": interior,
        "location": "Commodore, PA",
        "short_description": f"{title} with {mileage:,} miles.",
        "description": description,
        "images": images,
        "features": features,
        "specs": {},
        "details": {"info": [
            {"label": "Mileage", "value": f"{mileage:,} miles"},
            {"label": "Engine", "value": engine},
            {"label": "Transmission", "value": "Automatic"},
            {"label": "Drivetrain", "value": drivetrain},
            {"label": "Exterior Color", "value": exterior},
            {"label": "Interior Color", "value": interior},
        ]},
        "featured": len(VEHICLES) < 6,
        "financing_available": True,
        "warranty_available": True,
        "delivery_available": True,
    }


VEHICLES: list[dict] = []
VEHICLES.extend([
    vehicle("2021-porsche-cayenne-turbo", "2021 Porsche Cayenne Turbo", "Porsche", "Cayenne", "Turbo", 2021, 53499, 65000, "SUV", "Twin-Turbocharged 4.0L V8", "AWD", "Carmine Red", "Cohiba & Truffle Brown Club Leather", "WP1AF2AY0MDA36559", ["Off-Road & Premium Plus Packages", "Sport Chrono Package", "Burmester 3D Sound System", "Porsche Ceramic Composite Brakes", "Night Vision Assist"], "Carmine Red Cayenne Turbo with Club Leather, Sport Chrono, Premium Plus, ceramic brakes, and more than $57k in original options."),
    vehicle("2019-tesla-model-x-performance", "2019 Tesla Model X Performance", "Tesla", "Model X", "Performance", 2019, 27499, 63000, "SUV", "Dual Three-Phase AC Induction Motors", "AWD", "Black with Satin Black Vinyl Wrap", "Black Leather", "5YJXCBE42KF212836", ["Ludicrous Mode", "Falcon Wing rear doors", "Heated seats", "Self-Driving Capability"], "Model X Performance with Ludicrous Mode, satin black wrap, Falcon Wing doors, and self-driving capability."),
    vehicle("2020-audi-s8", "2020 Audi S8", "Audi", "S8", "", 2020, 36499, 60000, "Sedan", "Twin-Turbocharged 4.0-Liter TFSI V8", "Quattro AWD", "Terra Gray Metallic", "Merlot Red Leather", "WAU8SBF80LN008674", ["Executive & Cold Weather Packages", "Rear-wheel steering", "Top-view camera", "Seat heat, venting, & massage", "Bang & Olufsen sound"], "Terra Gray S8 with Merlot Red leather, executive rear-seat comfort, laser lighting, and Bang & Olufsen audio."),
    vehicle("2023-chevrolet-silverado-1500-rst-black-widow", "2023 Chevrolet Silverado 1500 Crew Cab RST Z71 4×4 Black Widow", "Chevrolet", "Silverado 1500", "RST Z71 Black Widow", 2023, 38499, 24000, "Truck", "5.3-Liter V8", "4WD", "Glacier Blue Metallic", "Leather", "1GCUDEED4PZ267307", ["Black Widow Package", "Z71 Off-Road Package", "All Star Edition Plus", "Tonneau cover"], "Glacier Blue Silverado RST Z71 4×4 with the Black Widow package, 22-inch wheels,."),
    vehicle("2021-ford-f-150-raptor-supercrew", "2021 Ford F-150 Raptor SuperCrew", "Ford", "F-150", "Raptor SuperCrew", 2021, 46499, 39000, "Truck", "Twin-Turbocharged 3.5-Liter V6", "4WD", "Antimatter Blue Metallic", "Black Nirvana Leather", "1FTFW1RG1MFC60005", ["Fox Live-Valve shocks", "Twin-panel sunroof", "Raptor Carbon Fiber Package", "Heated & ventilated front seats", "SYNC 4 infotainment"], "Antimatter Blue Raptor SuperCrew with Fox Live-Valve shocks, carbon-fiber trim, and extensive comfort and tow technology."),
    vehicle("2024-ram-1500-trx-final-edition", "2024 Ram 1500 TRX Crew Cab 4×4 Final Edition", "Ram", "1500", "TRX Final Edition", 2024, 77499, 6000, "Truck", "Supercharged 6.2-Liter Hemi V8", "4WD", "Billet Silver & Diamond Black Crystal", "Black & Gray Leather & Microsuede", "1C6SRFU98RN223520", ["TRX Level 1 & 2 packages", "20-inch Vossen HF6-4 wheels", "Bilstein adaptive dampers", "Dual-panel sunroof", "Harman Kardon sound"], "Low-mile Final Edition TRX with a supercharged Hemi V8, Vossen wheels, adaptive dampers, and premium equipment."),
    vehicle("2024-chevrolet-corvette-stingray-3lt-z51", "2024 Chevrolet Corvette Stingray Coupe 3LT Z51", "Chevrolet", "Corvette", "Stingray Coupe 3LT Z51", 2024, 61499, 8000, "Coupe", "6.2-Liter LT2 V8", "RWD", "Black", "Jet Black Leather", "1G1YC2D47R5116114", ["Z51 Performance Package", "Magnetic Selective Ride Control", "Front lift system", "Borla ATAK exhaust", "Eventuri carbon-fiber upgrades"], "8k-mile Corvette Stingray 3LT Z51 with a front lift system, magnetic ride, and selected performance upgrades."),
    vehicle("2022-gmc-sierra-1500-limited-harley-davidson", "2022 GMC Sierra 1500 Limited SLT Crew Cab Official Harley-Davidson", "GMC", "Sierra 1500", "Limited SLT Harley-Davidson", 2022, 43499, 29000, "Truck", "5.3-Liter V8", "4WD", "Onyx Black", "Black Leather", "1GTU9DED5NZ161859", ["Official Harley-Davidson conversion", "22-inch Harley-Davidson wheels", "Lifted suspension", "Power-retractable running boards", "Bose sound"], "Onyx Black Sierra SLT Crew Cab with the official Harley-Davidson conversion, lifted stance, and documentation."),
    vehicle("2021-toyota-land-cruiser-urj200-23k", "2021 Toyota Land Cruiser URJ200", "Toyota", "Land Cruiser", "URJ200", 2021, 64999, 23000, "SUV", "5.7-Liter V8", "4WD", "Midnight Black Metallic", "Terra Leather", "JTMCY7AJXM4107061", ["Kinetic Dynamic Suspension", "Glass sunroof", "Heated & ventilated front seats", "Bird's Eye View camera", "JBL audio"], "23k-mile Land Cruiser URJ200 finished in Midnight Black with Terra leather, KDSS,."),
    vehicle("2020-chevrolet-corvette-stingray-2lt", "2020 Chevrolet Corvette Stingray Coupe 2LT", "Chevrolet", "Corvette", "Stingray Coupe 2LT", 2020, 44999, 13000, "Coupe", "Mid-Mounted 6.2-Liter V8", "RWD", "Elkhart Lake Blue Metallic", "Natural Leather", "1G1Y72D42L5105663", ["Performance exhaust", "Front-axle lift", "Heated & ventilated seats", "Heads-up display"], "Elkhart Lake Blue Corvette Stingray 2LT with front-axle lift, performance exhaust, heads-up display, and 13k miles."),
    vehicle("2023-cadillac-escalade-v", "2023 Cadillac Escalade-V", "Cadillac", "Escalade", "V", 2023, 84999, 25000, "SUV", "Supercharged 6.2-Liter V8", "AWD", "Raven Black with Matte Black PPF", "Black Leather", "1GYS4HK92PR260374", ["Air Ride Adaptive Suspension", "Magnetic Ride Control", "Onyx Package", "Super Cruise", "36-speaker AKG Studio Reference audio"], "Raven Black Escalade-V with matte PPF, the Onyx Package, Super Cruise, and 36-speaker AKG audio."),
    vehicle("2025-toyota-land-cruiser-j250", "2025 Toyota Land Cruiser J250", "Toyota", "Land Cruiser", "J250", 2025, 46499, 12000, "SUV", "Turbocharged 2.4-Liter Hybrid Inline-Four", "4WD", "Underground", "Black SofTex", "JTEABFAJ3S5009169", ["Locking center & rear differentials", "Running boards", "Receiver hitch", "Toyota Safety Sense 3.0"], "Underground Land Cruiser J250 with hybrid power, locking differentials, receiver hitch,."),
    # The supplied source repeats the VIN from the 23k-mile Land Cruiser above.
    # Keep the second listing while leaving its duplicate chassis field unset.
    vehicle("2021-toyota-land-cruiser-urj200-22k", "2021 Toyota Land Cruiser URJ200", "Toyota", "Land Cruiser", "URJ200", 2021, 66499, 22000, "SUV", "5.7-Liter V8", "4WD", "Midnight Black Metallic", "Terra Leather", None, ["LED headlights", "Heated & ventilated front seats", "Heated second-row seats", "Third-row seating"], "22k-mile Land Cruiser URJ200 finished in Midnight Black with Terra leather, three-row seating,."),
    vehicle("2024-chevrolet-corvette-z06-convertible-3lz", "2024 Chevrolet Corvette Z06 Convertible 3LZ", "Chevrolet", "Corvette", "Z06 Convertible 3LZ", 2024, 85499, 367, "Convertible", "5.5-Liter LT6 V8", "RWD", "Red Mist Metallic Tintcoat", "Black & Adrenaline Red", "1G1YF3D39R5602038", ["3LZ Equipment Group", "Front-axle lift", "Power hardtop", "Performance Data & Video Recorder", "GT2 seats"], "367-mile Z06 Convertible 3LZ in Red Mist with the LT6 V8, front lift, power hardtop, and GT2 seats."),
    vehicle("2019-mercedes-amg-g63", "2019 Mercedes-AMG G63", "Mercedes-AMG", "G-Class", "G63", 2019, 77499, 61000, "SUV", "Twin-Turbocharged 4.0-Liter V8", "AWD", "Obsidian Black Metallic", "Designo Classic Red & Black Nappa Leather", "WDCYC7HJ6KX331735", ["Exclusive Interior Package Plus", "Night & Parking Packages", "Three locking differentials", "Surround-view camera", "Burmester sound"], "Obsidian Black G63 with Designo Nappa leather, three locking differentials, and the Exclusive Interior Package Plus."),
    vehicle("2024-gmc-sierra-2500hd-denali-ultimate", "2024 GMC Sierra 2500HD Denali Ultimate Crew Cab Duramax 4×4", "GMC", "Sierra 2500HD", "Denali Ultimate", 2024, 51499, 26000, "Truck", "6.6-Liter Duramax Turbodiesel V8", "4WD", "Onyx Black", "Alpine Umber Leather", "1GT49XEY9RF186405", ["22-inch Hostile Warrior wheels", "BDS 4-inch suspension lift", "Multipro tailgate", "Power-assist steps", "Bose sound"], "Onyx Black Sierra 2500HD Denali Ultimate with Duramax power, Hostile wheels, BDS lift, and Alpine Umber leather."),
])


def vehicles_table() -> sa.Table:
    return sa.table(
        "vehicles",
        sa.column("id", sa.String), sa.column("slug", sa.String), sa.column("title", sa.String),
        sa.column("make", sa.String), sa.column("model", sa.String), sa.column("trim", sa.String),
        sa.column("year", sa.Integer), sa.column("status", sa.String), sa.column("stock_number", sa.String),
        sa.column("vin", sa.String), sa.column("price", sa.Integer), sa.column("mileage", sa.Integer),
        sa.column("body_type", sa.String), sa.column("transmission", sa.String), sa.column("drivetrain", sa.String),
        sa.column("engine", sa.String), sa.column("exterior_color", sa.String), sa.column("interior_color", sa.String),
        sa.column("location", sa.String), sa.column("short_description", sa.String), sa.column("description", sa.Text),
        sa.column("images", sa.JSON), sa.column("features", sa.JSON), sa.column("specs", sa.JSON),
        sa.column("details", sa.JSON), sa.column("featured", sa.Boolean), sa.column("financing_available", sa.Boolean),
        sa.column("warranty_available", sa.Boolean), sa.column("delivery_available", sa.Boolean), sa.column("created_at", sa.DateTime),
    )


def upgrade() -> None:
    connection = op.get_bind()
    connection.execute(sa.text("UPDATE leads SET vehicle_id = NULL WHERE vehicle_id IS NOT NULL"))
    connection.execute(sa.text("DELETE FROM vehicles"))
    op.bulk_insert(vehicles_table(), [{**item, "created_at": CREATED_AT} for item in VEHICLES])


def downgrade() -> None:
    connection = op.get_bind()
    vehicle_ids = [item["id"] for item in VEHICLES]
    connection.execute(
        sa.text("UPDATE leads SET vehicle_id = NULL WHERE vehicle_id IN :vehicle_ids").bindparams(
            sa.bindparam("vehicle_ids", expanding=True)
        ),
        {"vehicle_ids": vehicle_ids},
    )
    connection.execute(
        sa.text("DELETE FROM vehicles WHERE id IN :vehicle_ids").bindparams(
            sa.bindparam("vehicle_ids", expanding=True)
        ),
        {"vehicle_ids": vehicle_ids},
    )
