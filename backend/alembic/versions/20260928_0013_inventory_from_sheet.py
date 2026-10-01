"""Replace the active inventory with the spreadsheet listings.

Revision ID: 20260928_0013
Revises: 20260927_0012
Create Date: 2026-09-28
"""

from datetime import datetime
import importlib.util
from pathlib import Path

from alembic import op
import sqlalchemy as sa


revision = "20260928_0013"
down_revision = "20260927_0012"
branch_labels = None
depends_on = None

CREATED_AT = datetime(2026, 9, 28)


def vehicle(
    slug: str,
    title: str,
    make: str,
    model: str,
    trim: str,
    year: int,
    price: int,
    mileage: int,
    body_type: str,
    engine: str,
    transmission: str,
    drivetrain: str,
    exterior: str,
    interior: str,
    features: list[str],
    description: str,
) -> dict:
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
        "vin": None,
        "price": price,
        "mileage": mileage,
        "body_type": body_type,
        "transmission": transmission,
        "drivetrain": drivetrain,
        "engine": engine,
        "exterior_color": exterior,
        "interior_color": interior,
        "location": "Commodore, PA",
        "short_description": description,
        "description": description,
        "images": [],
        "features": features,
        "specs": {},
        "details": {"info": [
            {"label": "Mileage", "value": f"{mileage:,} miles"},
            {"label": "Engine", "value": engine},
            {"label": "Transmission", "value": transmission},
            {"label": "Drivetrain", "value": drivetrain},
            {"label": "Exterior Color", "value": exterior},
            {"label": "Interior Color", "value": interior},
        ]},
        "featured": False,
        "financing_available": False,
        "warranty_available": True,
        "delivery_available": True,
    }


VEHICLES = [
    vehicle("2018-toyota-land-cruiser-urj200", "2018 Toyota Land Cruiser URJ200", "Toyota", "Land Cruiser", "URJ200", 2018, 74499, 7000, "SUV", "5.7L V8", "8-Speed Automatic", "4WD", "Midnight Black Metallic", "Black Leather", ["Kinetic Dynamic Suspension", "Crawl Control", "Sunroof", "Heated & ventilated front seats", "JBL audio"], "Midnight Black Land Cruiser with a 5.7L V8, KDSS, Crawl Control, a sunroof, and heated leather seating."),
    vehicle("2022-bmw-m5-competition-package", "2022 BMW M5 Competition Package", "BMW", "M5", "Competition Package", 2022, 54999, 26000, "Sedan", "Twin-Turbocharged 4.4L V8", "8-Speed Automatic", "AWD", "Motegi Red Metallic", "Silverstone Merino Leather", ["Competition Package", "Carbon-fiber roof", "Driving Assistance Professional", "Massaging front seats", "Bowers & Wilkins audio"], "Motegi Red M5 Competition with a 617-hp twin-turbo V8, carbon-fiber roof, and Silverstone Merino interior."),
    vehicle("2024-ford-f-250-super-duty-black-widow", "2024 Ford F-250 Super Duty Crew Cab Lariat Power Stroke 4×4 Black Widow", "Ford", "F-250 Super Duty", "Lariat Black Widow", 2024, 57499, 11000, "Truck", "6.7L High Output Power Stroke Turbo Diesel V8", "10-Speed Automatic", "4WD", "Carbonized Gray", "Black Onyx Leather", ["SCA Black Widow package", "BDS lift kit", "FOX shocks", "22-inch Black Widow wheels", "Panoramic sunroof"], "Carbonized Gray F-250 Black Widow with a High Output Power Stroke diesel, BDS lift, FOX shocks, and 22-inch wheels."),
    vehicle("2023-porsche-cayenne-platinum-edition", "2023 Porsche Cayenne Platinum Edition", "Porsche", "Cayenne", "Platinum Edition", 2023, 41499, 44000, "SUV", "Turbocharged 3.0L V6", "8-Speed Automatic", "AWD", "White", "Bordeaux Red Leather", ["Platinum Edition", "Panoramic sunroof", "22-inch 911 Turbo Design wheels", "Surround View camera", "Bose audio"], "White Cayenne Platinum Edition with Bordeaux Red leather, a panoramic roof, 22-inch wheels, and Bose audio."),
    vehicle("2024-chevrolet-corvette-stingray-convertible-z51-2lt", "2024 Chevrolet Corvette Stingray Convertible Z51 2LT", "Chevrolet", "Corvette Stingray", "Convertible Z51 2LT", 2024, 49999, 12000, "Convertible", "6.2L LT2 V8", "8-Speed Dual-Clutch Automatic", "RWD", "Carbon Flash Metallic", "Sky Cool Gray & Jet Black Leather", ["Z51 Performance Package", "Power-retractable hardtop", "Brembo brakes", "GT2 seats", "Performance Data Recorder"], "Carbon Flash Corvette Stingray convertible with the Z51 package, a 495-hp V8, and a power-retractable hardtop."),
    vehicle("2024-mercedes-amg-g63", "2024 Mercedes-AMG G63", "Mercedes-Benz", "G-Class", "AMG G63", 2024, 145999, 369, "SUV", "Twin-Turbocharged 4.0L V8", "9-Speed Automatic", "4WD", "Black", "Bengal Red Nappa Leather", ["Three locking differentials", "21-inch AMG wheels", "Massaging front seats", "Burmester surround sound", "MBUX navigation"], "Black AMG G63 with Bengal Red Nappa leather, a 577-hp twin-turbo V8, and three locking differentials."),
    vehicle("2020-cadillac-escalade-esv-platinum-4wd", "2020 Cadillac Escalade ESV Platinum 4WD", "Cadillac", "Escalade ESV", "Platinum 4WD", 2020, 29999, 40000, "SUV", "6.2L V8", "10-Speed Automatic", "4WD", "Crystal White Tricoat", "Maple Sugar Nappa Leather", ["Magnetic Ride Control", "22-inch Vogue Tyre wheels", "Heated & cooled front seats", "Head-up display", "Rear-seat entertainment"], "Crystal White Escalade ESV Platinum with Maple Sugar leather, Magnetic Ride Control, and rear-seat entertainment."),
    vehicle("2022-tesla-model-s-plaid", "2022 Tesla Model S Plaid", "Tesla", "Model S", "Plaid", 2022, 39999, 22000, "Sedan", "Tri-Motor Electric Powertrain", "Single-Speed", "AWD", "Red Multi-Coat", "Cream & Black Upholstery", ["1,020-hp tri-motor powertrain", "Full Self-Driving Capability", "Panoramic glass roof", "17-inch center display", "22-speaker audio"], "Red Model S Plaid with tri-motor all-wheel drive, Full Self-Driving Capability, and a panoramic glass roof."),
    vehicle("2021-ford-f-150-shelby-raptor-baja-supercrew", "2021 Ford F-150 Shelby Raptor Baja SuperCrew", "Ford", "F-150", "Shelby Raptor Baja SuperCrew", 2021, 79999, 23000, "Truck", "Twin-Turbocharged 3.5L EcoBoost V6", "10-Speed Automatic", "4WD", "Lead Foot", "Black & Red Shelby Upholstery", ["Shelby Baja #125", "Whipple revised tuning", "FOX remote-reservoir shocks", "37-inch BFGoodrich tires", "Bang & Olufsen audio"], "Lead Foot Shelby Raptor Baja with Whipple-tuned power, FOX suspension, Shelby details, and 37-inch tires."),
    vehicle("2023-bmw-x6-m50i", "2023 BMW X6 M50i", "BMW", "X6", "M50i", 2023, 46999, 18000, "SUV", "Twin-Turbocharged 4.4L V8", "8-Speed Automatic", "AWD", "Black Sapphire Metallic", "Ivory White Merino Leather", ["Executive Package", "Driving Assistance Pro", "22-inch M wheels", "M Sport differential", "Harman Kardon audio"], "Black Sapphire X6 M50i with a 523-hp twin-turbo V8, Ivory White Merino leather, and xDrive all-wheel drive."),
    vehicle("2025-gmc-sierra-1500-pro-4x4", "2025 GMC Sierra 1500 PRO 4×4", "GMC", "Sierra 1500", "PRO 4×4", 2025, 29999, 2000, "Truck", "Turbocharged 2.7L TurboMax Inline-Four", "8-Speed Automatic", "4WD", "Onyx Black", "Jet Black Cloth", ["Regular cab", "Color-matched exterior trim", "Tonneau cover", "Lowered suspension", "24-inch alloy wheels"], "Low-mile Onyx Black Sierra PRO with a turbocharged 2.7L engine, custom 24-inch wheels, and a lowered stance."),
    vehicle("2022-cadillac-ct5-v-blackwing-6-speed", "2022 Cadillac CT5-V Blackwing 6-Speed", "Cadillac", "CT5-V Blackwing", "6-Speed", 2022, 61999, 23000, "Sedan", "Supercharged 6.2L V8", "6-Speed Manual", "RWD", "Rift Metallic", "Jet Black Leather", ["668-hp supercharged V8", "Magnetic Ride Control", "Brembo brakes", "Massaging front seats", "AKG audio"], "Rift Metallic CT5-V Blackwing with a 668-hp supercharged V8, six-speed manual, and Magnetic Ride Control."),
    vehicle("2018-porsche-718-cayman-gts", "2018 Porsche 718 Cayman GTS", "Porsche", "718 Cayman", "GTS", 2018, 30999, 105000, "Coupe", "Turbocharged 2.5L Flat-Four", "7-Speed PDK Automatic", "RWD", "Agate Gray Metallic", "Black & Dark Silver Leather with Sport-Tex", ["PASM sport suspension", "20-inch Carrera Classic II wheels", "Adaptive Sport Seats Plus", "Carbon-fiber trim", "Bose audio"], "Agate Gray 718 Cayman GTS with a turbocharged flat-four, PDK transmission, PASM suspension, and Sport-Tex accents."),
    vehicle("2024-toyota-4runner-trd-off-road-premium-4x4", "2024 Toyota 4Runner TRD Off-Road Premium 4×4", "Toyota", "4Runner", "TRD Off-Road Premium 4×4", 2024, 38999, 8000, "SUV", "4.0L V6", "5-Speed Automatic", "4WD", "Underground", "Black SofTex", ["Kinetic Dynamic Suspension System", "Bilstein suspension", "RSG-Offroad rock sliders", "Front & rear dashcams", "Navigation"], "Underground 4Runner TRD Off-Road Premium with KDSS, Bilstein suspension, rock sliders, and four-wheel drive."),
    vehicle("2023-cadillac-escalade-v-esv", "2023 Cadillac Escalade-V ESV", "Cadillac", "Escalade-V ESV", "ESV", 2023, 84999, 11000, "SUV", "Supercharged 6.2L V8", "10-Speed Automatic", "AWD", "Black Raven", "Jet Black Leather", ["682-hp supercharged V8", "Air Ride Adaptive Suspension", "Magnetic Ride Control", "Super Cruise", "AKG audio"], "Black Raven Escalade-V ESV with a 682-hp supercharged V8, Super Cruise, and adaptive air suspension."),
]
for index, item in enumerate(VEHICLES):
    item["featured"] = index < 6


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


def _previous_inventory() -> list[dict]:
    migration_path = Path(__file__).with_name("20260923_0010_replace_test_inventory.py")
    spec = importlib.util.spec_from_file_location("previous_inventory_migration", migration_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load the prior inventory migration for downgrade")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.VEHICLES


def upgrade() -> None:
    connection = op.get_bind()
    connection.execute(sa.text("UPDATE leads SET vehicle_id = NULL WHERE vehicle_id IS NOT NULL"))
    connection.execute(sa.text("DELETE FROM vehicles"))
    op.bulk_insert(vehicles_table(), [{**item, "created_at": CREATED_AT} for item in VEHICLES])


def downgrade() -> None:
    connection = op.get_bind()
    connection.execute(sa.text("UPDATE leads SET vehicle_id = NULL WHERE vehicle_id IS NOT NULL"))
    connection.execute(sa.text("DELETE FROM vehicles"))
    previous = _previous_inventory()
    op.bulk_insert(vehicles_table(), [
        {**item, "created_at": datetime(2026, 9, 23)} for item in previous
    ])
