"""add vehicle source details

Revision ID: 20260721_0004
Revises: 20260721_0003
Create Date: 2026-07-21
"""

from alembic import op
import sqlalchemy as sa


revision = "20260721_0004"
down_revision = "20260721_0003"
branch_labels = None
depends_on = None


VEHICLE_DETAILS = {
    "2022-porsche-911-carrera-s-coupe": {
        "info": [
            {
                "label": "Title",
                "value": "2022 Porsche 911 Carrera S Coupe"
            },
            {
                "label": "Make",
                "value": "Porsche"
            },
            {
                "label": "Engine",
                "value": "3.0L Turbocharged Flat-6"
            },
            {
                "label": "Model",
                "value": "992 911Save"
            },
            {
                "label": "Drivetrain",
                "value": "Rear-wheel drive"
            },
            {
                "label": "Mileage",
                "value": "11,900"
            },
            {
                "label": "Transmission",
                "value": "Manual (7-Speed)"
            },
            {
                "label": "VIN",
                "value": "WP0AB2A99NS220109"
            },
            {
                "label": "Body Style",
                "value": "Coupe"
            },
            {
                "label": "Title Status",
                "value": "Clean (MA)"
            },
            {
                "label": "Exterior Color",
                "value": "Chalk"
            },
            {
                "label": "Location",
                "value": "Canton, MA 02021"
            },
            {
                "label": "Interior Color",
                "value": "Black"
            },
            {
                "label": "Seller",
                "value": "jklane"
            },
            {
                "label": "Seller Type",
                "value": "Private Party"
            }
        ],
        "sections": [
            {
                "title": "HIGHLIGHTS",
                "content": "THIS... is a 2022 Porsche 911 Carrera S Coupe, finished in Chalk with a black interior.\n  - This 911 is equipped with the desirable 7-speed manual transmission, and its odometer displays about 11,900 miles.\n  - The attachedCarfaxhistory report lists no accidents or mileage inconsistencies in this car's past.\n  - According to the Monroney Label provided in the gallery, notable factory equipment includes the SportDesign, Sport, and Premium packages, 20-inch front and 21-inch rear wheels, Adaptive Sport Seats Plus, and more as detailed below. The seller reports no notable modifications.\n  - Porsche released the 992 generation of the 911 for 2020. Slightly longer and wider than its predecessor, it received evolutionary design updates and much more significant changes under the body, including revised engines and an 8-speed automatic transmission. Production continues in 2023.\n  - Power comes from a 3.0-liter twin-turbocharged flat-6, rated at 443 horsepower and 390 lb-ft of torque. It spins the rear wheels via a 7-speed manual transmission."
            },
            {
                "title": "EQUIPMENT",
                "content": "A Monroney Label is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - SportDesign Package in Gloss Black (option code 2D5)\n  - Sport Package\n  - Premium Package\n  - 20-inch front and 21-inch rear wheels\n  - 18-way power-adjustable, heated, and ventilated Adaptive Sport Seats Plus\n  - GT Sport steering wheel\n  - Dual 7-inch screens in the instrument cluster"
            },
            {
                "title": "RECENT SERVICE HISTORY",
                "content": "The attachedCarfaxhistory report shows that the following services have been performed:\n  - April 2026 (11,723 miles): Engine oil and filter changed\n  - March 2025 (9,571 miles): Engine oil and filter changed, brake fluid flushed/changed\n  - January 2024 (8,104 miles): Engine oil and filter changed, spark plug(s) replaced"
            },
            {
                "title": "OTHER ITEMS INCLUDED IN SALE",
                "content": "- 2 keys\n  - Owner's manuals"
            },
            {
                "title": "OWNERSHIP HISTORY",
                "content": "The seller reportedly purchased this 911 in April 2025 and has added about 2,200 miles since."
            },
            {
                "title": "SELLER NOTES",
                "content": "- The seller states that paint protection film has been applied to the front end and to high-impact zones.\n  - There is a loan on this vehicle, and sale proceeds will be used to satisfy the loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif agreed to by both the buyer and the seller. Please note that the title may only be availableafterthe loan has been paid off."
            }
        ],
        "raw_description": "HIGHLIGHTS\n\nTHIS... is a 2022 Porsche 911 Carrera S Coupe, finished in Chalk with a black interior.\n  - This 911 is equipped with the desirable 7-speed manual transmission, and its odometer displays about 11,900 miles.\n  - The attachedCarfaxhistory report lists no accidents or mileage inconsistencies in this car's past.\n  - According to the Monroney Label provided in the gallery, notable factory equipment includes the SportDesign, Sport, and Premium packages, 20-inch front and 21-inch rear wheels, Adaptive Sport Seats Plus, and more as detailed below. The seller reports no notable modifications.\n  - Porsche released the 992 generation of the 911 for 2020. Slightly longer and wider than its predecessor, it received evolutionary design updates and much more significant changes under the body, including revised engines and an 8-speed automatic transmission. Production continues in 2023.\n  - Power comes from a 3.0-liter twin-turbocharged flat-6, rated at 443 horsepower and 390 lb-ft of torque. It spins the rear wheels via a 7-speed manual transmission.\n\nEQUIPMENT\n\nA Monroney Label is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - SportDesign Package in Gloss Black (option code 2D5)\n  - Sport Package\n  - Premium Package\n  - 20-inch front and 21-inch rear wheels\n  - 18-way power-adjustable, heated, and ventilated Adaptive Sport Seats Plus\n  - GT Sport steering wheel\n  - Dual 7-inch screens in the instrument cluster\n\nRECENT SERVICE HISTORY\n\nThe attachedCarfaxhistory report shows that the following services have been performed:\n  - April 2026 (11,723 miles): Engine oil and filter changed\n  - March 2025 (9,571 miles): Engine oil and filter changed, brake fluid flushed/changed\n  - January 2024 (8,104 miles): Engine oil and filter changed, spark plug(s) replaced\n\nOTHER ITEMS INCLUDED IN SALE\n\n  - 2 keys\n  - Owner's manuals\n\nOWNERSHIP HISTORY\n\nThe seller reportedly purchased this 911 in April 2025 and has added about 2,200 miles since.\n\nSELLER NOTES\n\n  - The seller states that paint protection film has been applied to the front end and to high-impact zones.\n  - There is a loan on this vehicle, and sale proceeds will be used to satisfy the loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif agreed to by both the buyer and the seller. Please note that the title may only be availableafterthe loan has been paid off."
    },
    "2025-ford-f-150-raptor": {
        "info": [
            {
                "label": "Title",
                "value": "2025 Ford F-150 Raptor"
            },
            {
                "label": "Make",
                "value": "Ford"
            },
            {
                "label": "Engine",
                "value": "3.5L Turbocharged V6"
            },
            {
                "label": "Model",
                "value": "F-150 RaptorSave"
            },
            {
                "label": "Drivetrain",
                "value": "4WD/AWD"
            },
            {
                "label": "Mileage",
                "value": "13,800"
            },
            {
                "label": "Transmission",
                "value": "Automatic (10-Speed)"
            },
            {
                "label": "VIN",
                "value": "1FTFW1RG7SFA59271"
            },
            {
                "label": "Body Style",
                "value": "Truck"
            },
            {
                "label": "Title Status",
                "value": "Clean (CA)"
            },
            {
                "label": "Exterior Color",
                "value": "Carbonized Gray Metallic"
            },
            {
                "label": "Location",
                "value": "Oroville, CA 95966"
            },
            {
                "label": "Interior Color",
                "value": "Black"
            },
            {
                "label": "Seller",
                "value": "sleeperbuildconnoisseur"
            },
            {
                "label": "Seller Type",
                "value": "Private Party"
            }
        ],
        "sections": [
            {
                "title": "HIGHLIGHTS",
                "content": "THIS... is a 2025 Ford F-150 Raptor, finished in Carbonized Gray Metallic with a black interior.\n  - The attachedCarfaxvehicle history report shows no accidents or mileage discrepancies in this F-150’s past.\n  - According to the window sticker provided in the gallery, this F-150 is a Raptor model, and notable factory equipment includes the Equipment Group 801A, an electronically locking rear axle, a dual exhaust system, a Tough Bed spray-in bedliner, heated and ventilated front bucket seats, a Bang & Olufson Unleashed sound system, and Pro Trailer Backup Assist.\n  - Notable modifications reported by the seller include a 2.2-inch Eibach Pro-Lift spring kit, 17-inch Method wheels on BFGoodrich All-Terrain T/A KO2 tires, a color-matched front bumper and skid plate, a short antenna, and auto start-stop and seat belt warning chime disablers.\n  - Designed to speed across the desert like a Baja racer, the third-generation F-150 Raptor made its debut for the 2021 model year. In addition to styling changes, Ford upgraded the rear suspension from leaf springs to a coil-spring setup. Additionally, the new Raptor received a fully digital instrument cluster, a 12-inch touchscreen infotainment system, and a shift lever that folds flat into the center console area.\n  - Power comes from a twin-turbocharged 3.5-liter V6 engine, rated at about 450 horsepower and 510 lb-ft of torque. Output is sent to the rear or all four wheels via a 10-speed automatic transmission."
            },
            {
                "title": "EQUIPMENT",
                "content": "This F-150 is a Raptor model. A window sticker is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - Equipment Group 801A\n  - Electronically locking rear axle\n  - Dual exhaust system\n  - Tough Bed spray-in bedliner\n  - Heated and ventilated front bucket seats\n  - Bang & Olufsen Unleashed sound system\n  - Pro Trailer Backup Assist"
            },
            {
                "title": "MODIFICATIONS",
                "content": "Notable modifications reported by the seller include:\n  - 2.2-inch Eibach Pro-Lift spring kit\n  - 17-inch Method wheels\n  - 37-inch BFGoodrich All-Terrain T/A KO2 tires\n  - Color-matched front bumper and skid plate\n  - Short antenna\n  - Auto start-stop disabler\n  - Seat belt warning chime disabled"
            },
            {
                "title": "KNOWN FLAWS",
                "content": "- Some scratches on exterior panels as seen in gallery photos"
            },
            {
                "title": "RECENT SERVICE HISTORY",
                "content": "The attachedCarfaxhistory report shows that the following services have been performed:\n  - June 2026 (13,258 miles): Trim repaired\n  - December 2025 (9,222 miles): Engine oil and filter changed\n  - June 2025 (3,863 miles): Engine oil and filter changed\nAdditional service history is detailed in the attachedCarfaxhistory report."
            },
            {
                "title": "OTHER ITEMS INCLUDED IN SALE",
                "content": "- 2 keys\n  - Owner's manuals\n  - Window sticker\n  - Factory coil springs\n  - Foutz Motorsports front light mount kit"
            },
            {
                "title": "OWNERSHIP HISTORY",
                "content": "The seller reportedly purchased this F-150 new in March 2023."
            },
            {
                "title": "SELLER NOTES",
                "content": "- There is a loan on this vehicle, and sale proceeds will be used to satisfy the loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif agreed to by both the buyer and the seller. Please note that the title may only be availableafterthe loan has been paid off.\n  - The seller reports that a ceramic window tint has been applied to the windows and windshield."
            }
        ],
        "raw_description": "HIGHLIGHTS\n\nTHIS... is a 2025 Ford F-150 Raptor, finished in Carbonized Gray Metallic with a black interior.\n  - The attachedCarfaxvehicle history report shows no accidents or mileage discrepancies in this F-150’s past.\n  - According to the window sticker provided in the gallery, this F-150 is a Raptor model, and notable factory equipment includes the Equipment Group 801A, an electronically locking rear axle, a dual exhaust system, a Tough Bed spray-in bedliner, heated and ventilated front bucket seats, a Bang & Olufson Unleashed sound system, and Pro Trailer Backup Assist.\n  - Notable modifications reported by the seller include a 2.2-inch Eibach Pro-Lift spring kit, 17-inch Method wheels on BFGoodrich All-Terrain T/A KO2 tires, a color-matched front bumper and skid plate, a short antenna, and auto start-stop and seat belt warning chime disablers.\n  - Designed to speed across the desert like a Baja racer, the third-generation F-150 Raptor made its debut for the 2021 model year. In addition to styling changes, Ford upgraded the rear suspension from leaf springs to a coil-spring setup. Additionally, the new Raptor received a fully digital instrument cluster, a 12-inch touchscreen infotainment system, and a shift lever that folds flat into the center console area.\n  - Power comes from a twin-turbocharged 3.5-liter V6 engine, rated at about 450 horsepower and 510 lb-ft of torque. Output is sent to the rear or all four wheels via a 10-speed automatic transmission.\n\nEQUIPMENT\n\nThis F-150 is a Raptor model. A window sticker is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - Equipment Group 801A\n  - Electronically locking rear axle\n  - Dual exhaust system\n  - Tough Bed spray-in bedliner\n  - Heated and ventilated front bucket seats\n  - Bang & Olufsen Unleashed sound system\n  - Pro Trailer Backup Assist\n\nMODIFICATIONS\n\nNotable modifications reported by the seller include:\n  - 2.2-inch Eibach Pro-Lift spring kit\n  - 17-inch Method wheels\n  - 37-inch BFGoodrich All-Terrain T/A KO2 tires\n  - Color-matched front bumper and skid plate\n  - Short antenna\n  - Auto start-stop disabler\n  - Seat belt warning chime disabled\n\nKNOWN FLAWS\n\n  - Some scratches on exterior panels as seen in gallery photos\n\nRECENT SERVICE HISTORY\n\nThe attachedCarfaxhistory report shows that the following services have been performed:\n  - June 2026 (13,258 miles): Trim repaired\n  - December 2025 (9,222 miles): Engine oil and filter changed\n  - June 2025 (3,863 miles): Engine oil and filter changed\nAdditional service history is detailed in the attachedCarfaxhistory report.\n\nOTHER ITEMS INCLUDED IN SALE\n\n  - 2 keys\n  - Owner's manuals\n  - Window sticker\n  - Factory coil springs\n  - Foutz Motorsports front light mount kit\n\nOWNERSHIP HISTORY\n\nThe seller reportedly purchased this F-150 new in March 2023.\n\nSELLER NOTES\n\n  - There is a loan on this vehicle, and sale proceeds will be used to satisfy the loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif agreed to by both the buyer and the seller. Please note that the title may only be availableafterthe loan has been paid off.\n  - The seller reports that a ceramic window tint has been applied to the windows and windshield."
    },
    "2017-porsche-macan-gts": {
        "info": [
            {
                "label": "Title",
                "value": "2017 Porsche Macan GTS"
            },
            {
                "label": "Make",
                "value": "Porsche"
            },
            {
                "label": "Engine",
                "value": "3.0L Turbocharged V6"
            },
            {
                "label": "Model",
                "value": "MacanSave"
            },
            {
                "label": "Drivetrain",
                "value": "4WD/AWD"
            },
            {
                "label": "Mileage",
                "value": "92,400"
            },
            {
                "label": "Transmission",
                "value": "Automatic (7-Speed)"
            },
            {
                "label": "VIN",
                "value": "WP1AG2A58HLB50291"
            },
            {
                "label": "Body Style",
                "value": "SUV/Crossover"
            },
            {
                "label": "Title Status",
                "value": "Clean (RI)"
            },
            {
                "label": "Exterior Color",
                "value": "Carmine Red"
            },
            {
                "label": "Location",
                "value": "Providence, RI 02906"
            },
            {
                "label": "Interior Color",
                "value": "Black"
            },
            {
                "label": "Seller",
                "value": "jmelfi"
            },
            {
                "label": "Seller Type",
                "value": "Private Party"
            }
        ],
        "sections": [
            {
                "title": "HIGHLIGHTS",
                "content": "THIS... is a 2017 Porsche Macan GTS, finished in Carmine Red with a black interior.\n  - The attachedCarfaxvehicle history report lists no accidents or mileage discrepancies in this Porsche's past.\n  - According to the build sheet provided in the gallery, this Macan is a GTS model, and notable factory equipment includes the Premium Package Plus, Sport Chrono, Carbon Fiber Interior, and Leather packages, Porsche Torque Vectoring Plus, SportDesign side mirrors, LED headlights with PDLS+, adaptive sport seats, and a heated multifunction sport steering wheel in carbon fiber.\n  - Notable modifications reported by the seller include Euro-style side marker lights, Flat 6 Motorsports sequential LED turn signal lights, gold GTS side blade letters, rear lettering in gloss black, and smoker Package components.\n  - Encouraged by the Cayenne's success and eager to tap into one of the biggest segments of the market, Porsche introduced the Macan as its entry-level SUV for 2015. Some of the model's underpinnings came from Audi, but Porsche dialed in a level of performance and handling that's unusual to find in a compact SUV.\n  - Power comes from a 3.0-liter twin-turbocharged V6, rated at 360 horsepower and 369 lb-ft of torque. Output is sent to all four wheels via a 7-speed PDK dual-clutch automatic transmission."
            },
            {
                "title": "EQUIPMENT",
                "content": "This Macan is a GTS model. A build sheet is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - Premium Package Plus\n  - Sport Chrono Package\n  - Carbon Fiber Interior Package\n  - Leather Package\n  - Porsche Torque Vectoring Plus\n  - SportDesign side mirrors\n  - LED headlights with PDLS+\n  - Adaptive sport seats\n  - Heated multifunction sport steering wheel in carbon fiber"
            },
            {
                "title": "MODIFICATIONS",
                "content": "Notable modifications reported by the seller include:\n  - Euro-style side marker lights\n  - Flat 6 Motorsports sequential LED turn signal lights\n  - Gold GTS side blade letters\n  - Rear lettering in gloss black\n  - Smoker Package components"
            },
            {
                "title": "KNOWN FLAWS",
                "content": "- Some stone chips on forward-facing surfaces (many repaired)\n  - Scuffs on driver-side side blades and door sills\n  - Wear on inner exhaust tips\n  - Creases on driver's seat bolsters"
            },
            {
                "title": "RECENT SERVICE HISTORY",
                "content": "Service documentation in the photo gallery indicates that the following maintenance has been performed:\n  - December 2025 (92,256 miles): Exhaust flex pipe vibration repaired\n  - November 2025 (91,177 miles): Fuel filler flap replaced, right front wheel refinished\n  - November 2025 (91,076 miles): Wheel refinish performed, passenger-side fender well fabric realigned\n  - October 2025 (90,452 miles): Door molding replaced\n  - September 2025 (90,038 miles): Front timing cover resealed, A/C line, lower radiator hose, various seals and hardware replaced, alignment performed\n  - July 2025 (89,687 miles): Spark plugs replaced, engine oil and filter changed\n  - May 2025 (87,729 miles): Rear brake pads, rotors, and sender wire replaced\n  - March 2025 (85,368 miles): Cooling flap assembly replaced\n  - January 2025 (83,761 miles): Coolant reservoir replaced\n  - November 2024 (82,819 miles): Wheels balanced\n  - October 2024 (82,160 miles): Rear suspension level sensor replaced\n  - August 2024 (80,400 miles): Driver's sun visor replaced\n  - August 2024 (80,118 miles): Transmission serviced, brake fluid flushed\n  - August 2024 (79,697 miles): 80,000-mile service performed\n  - July 2024 (79,477 miles): Suspension level sensors replaced\n  - July 2023 (72,530 miles): Engine oil and filter changed\n  - May 2023 (70,464 miles): A/C recharged, A/C line seals replaced\n  - April 2023 (69,443 miles): Front wheel bearing replaced, A/C recharged\n  - March 2023 (61,416 miles): 1 headlight and upper center console cover replaced\n  - October 2022 (61,416 miles): Outer sunroof seal replaced\nParts receipts are included in the photo gallery, and the seller reports that the following services have been performed:\n  - Plastic engine covers, hood insulation pad, under-hood bolts, and key covers replaced\n  - Sunroof drains cleared"
            },
            {
                "title": "OTHER ITEMS INCLUDED IN SALE",
                "content": "- 2 keys\n  - Owner's manual\n  - 2 spare lower window trim pieces\n  - 2 spare Porsche rear seat covers\n  - 2 spare Porsche front seatback covers\n  - Spare cabin air filter\n  - Porsche winter floor mats\n  - Porsche wheel covers\n  - Porsche Exclusive Manufaktur floor mat with red stitching\n  - Porsche Exclusive Manufaktur ignition switch in Carmine Red\n  - Porsche pen"
            },
            {
                "title": "OWNERSHIP HISTORY",
                "content": "The seller reports that they purchased this Porsche in September 2022 and have added about 30,900 miles since."
            },
            {
                "title": "SELLER NOTES",
                "content": "- There is a loan on this vehicle, and sale proceeds will be used to satisfy the loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif agreed to by both the buyer and the seller. Please note that the title may only be availableafterthe loan has been paid off.\n  - The seller reports that the hood and front bumper were recently repainted and that a paint correction was performed due to stone chips; an invoice is provided in the gallery.\n  - The seller notes that paint protection film has been applied to the front bumper, lower valence, hood, fenders, side blades, door handle cups, and door sills, that XPEL ceramic coating has been applied to the exterior, wheels, interior trim, glass, and leather, and that the front windows have been tinted with ceramic tint."
            }
        ],
        "raw_description": "HIGHLIGHTS\n\nTHIS... is a 2017 Porsche Macan GTS, finished in Carmine Red with a black interior.\n  - The attachedCarfaxvehicle history report lists no accidents or mileage discrepancies in this Porsche's past.\n  - According to the build sheet provided in the gallery, this Macan is a GTS model, and notable factory equipment includes the Premium Package Plus, Sport Chrono, Carbon Fiber Interior, and Leather packages, Porsche Torque Vectoring Plus, SportDesign side mirrors, LED headlights with PDLS+, adaptive sport seats, and a heated multifunction sport steering wheel in carbon fiber.\n  - Notable modifications reported by the seller include Euro-style side marker lights, Flat 6 Motorsports sequential LED turn signal lights, gold GTS side blade letters, rear lettering in gloss black, and smoker Package components.\n  - Encouraged by the Cayenne's success and eager to tap into one of the biggest segments of the market, Porsche introduced the Macan as its entry-level SUV for 2015. Some of the model's underpinnings came from Audi, but Porsche dialed in a level of performance and handling that's unusual to find in a compact SUV.\n  - Power comes from a 3.0-liter twin-turbocharged V6, rated at 360 horsepower and 369 lb-ft of torque. Output is sent to all four wheels via a 7-speed PDK dual-clutch automatic transmission.\n\nEQUIPMENT\n\nThis Macan is a GTS model. A build sheet is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - Premium Package Plus\n  - Sport Chrono Package\n  - Carbon Fiber Interior Package\n  - Leather Package\n  - Porsche Torque Vectoring Plus\n  - SportDesign side mirrors\n  - LED headlights with PDLS+\n  - Adaptive sport seats\n  - Heated multifunction sport steering wheel in carbon fiber\n\nMODIFICATIONS\n\nNotable modifications reported by the seller include:\n  - Euro-style side marker lights\n  - Flat 6 Motorsports sequential LED turn signal lights\n  - Gold GTS side blade letters\n  - Rear lettering in gloss black\n  - Smoker Package components\n\nKNOWN FLAWS\n\n  - Some stone chips on forward-facing surfaces (many repaired)\n  - Scuffs on driver-side side blades and door sills\n  - Wear on inner exhaust tips\n  - Creases on driver's seat bolsters\n\nRECENT SERVICE HISTORY\n\nService documentation in the photo gallery indicates that the following maintenance has been performed:\n  - December 2025 (92,256 miles): Exhaust flex pipe vibration repaired\n  - November 2025 (91,177 miles): Fuel filler flap replaced, right front wheel refinished\n  - November 2025 (91,076 miles): Wheel refinish performed, passenger-side fender well fabric realigned\n  - October 2025 (90,452 miles): Door molding replaced\n  - September 2025 (90,038 miles): Front timing cover resealed, A/C line, lower radiator hose, various seals and hardware replaced, alignment performed\n  - July 2025 (89,687 miles): Spark plugs replaced, engine oil and filter changed\n  - May 2025 (87,729 miles): Rear brake pads, rotors, and sender wire replaced\n  - March 2025 (85,368 miles): Cooling flap assembly replaced\n  - January 2025 (83,761 miles): Coolant reservoir replaced\n  - November 2024 (82,819 miles): Wheels balanced\n  - October 2024 (82,160 miles): Rear suspension level sensor replaced\n  - August 2024 (80,400 miles): Driver's sun visor replaced\n  - August 2024 (80,118 miles): Transmission serviced, brake fluid flushed\n  - August 2024 (79,697 miles): 80,000-mile service performed\n  - July 2024 (79,477 miles): Suspension level sensors replaced\n  - July 2023 (72,530 miles): Engine oil and filter changed\n  - May 2023 (70,464 miles): A/C recharged, A/C line seals replaced\n  - April 2023 (69,443 miles): Front wheel bearing replaced, A/C recharged\n  - March 2023 (61,416 miles): 1 headlight and upper center console cover replaced\n  - October 2022 (61,416 miles): Outer sunroof seal replaced\nParts receipts are included in the photo gallery, and the seller reports that the following services have been performed:\n  - Plastic engine covers, hood insulation pad, under-hood bolts, and key covers replaced\n  - Sunroof drains cleared\n\nOTHER ITEMS INCLUDED IN SALE\n\n  - 2 keys\n  - Owner's manual\n  - 2 spare lower window trim pieces\n  - 2 spare Porsche rear seat covers\n  - 2 spare Porsche front seatback covers\n  - Spare cabin air filter\n  - Porsche winter floor mats\n  - Porsche wheel covers\n  - Porsche Exclusive Manufaktur floor mat with red stitching\n  - Porsche Exclusive Manufaktur ignition switch in Carmine Red\n  - Porsche pen\n\nOWNERSHIP HISTORY\n\nThe seller reports that they purchased this Porsche in September 2022 and have added about 30,900 miles since.\n\nSELLER NOTES\n\n  - There is a loan on this vehicle, and sale proceeds will be used to satisfy the loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif agreed to by both the buyer and the seller. Please note that the title may only be availableafterthe loan has been paid off.\n  - The seller reports that the hood and front bumper were recently repainted and that a paint correction was performed due to stone chips; an invoice is provided in the gallery.\n  - The seller notes that paint protection film has been applied to the front bumper, lower valence, hood, fenders, side blades, door handle cups, and door sills, that XPEL ceramic coating has been applied to the exterior, wheels, interior trim, glass, and leather, and that the front windows have been tinted with ceramic tint."
    },
    "2015-dodge-challenger-srt-hellcat": {
        "info": [
            {
                "label": "Title",
                "value": "2015 Dodge Challenger SRT Hellcat"
            },
            {
                "label": "Make",
                "value": "Dodge"
            },
            {
                "label": "Engine",
                "value": "6.2L Supercharged V8"
            },
            {
                "label": "Model",
                "value": "ChallengerSave"
            },
            {
                "label": "Drivetrain",
                "value": "Rear-wheel drive"
            },
            {
                "label": "Mileage",
                "value": "41,800"
            },
            {
                "label": "Transmission",
                "value": "Manual (6-Speed)"
            },
            {
                "label": "VIN",
                "value": "2C3CDZC90FH887771"
            },
            {
                "label": "Body Style",
                "value": "Coupe"
            },
            {
                "label": "Title Status",
                "value": "Clean (FL)"
            },
            {
                "label": "Exterior Color",
                "value": "Pitch Black"
            },
            {
                "label": "Location",
                "value": "Fort Lauderdale, FL 33315"
            },
            {
                "label": "Interior Color",
                "value": "Black"
            },
            {
                "label": "Seller",
                "value": "SpencerMilligan"
            },
            {
                "label": "Seller Type",
                "value": "Private Party"
            }
        ],
        "sections": [
            {
                "title": "HIGHLIGHTS",
                "content": "THIS... is a 2015 Dodge Challenger SRT Hellcat, finished in Pitch Black with a black interior.\n  - This coupe is equipped with the desirable 6-speed manual transmission, and its odometer displays about 41,800 miles.\n  - The attachedCarfaxhistory report lists no mileage inconsistencies in this Challenger's past. It also shows that this car has been Florida-owned since new.\n  - A window sticker is provided in the gallery, and a partial list of notable equipment reported by the seller includes an SRT-tuned Bilstein 3-mode active suspension system, Laguna leather upholstery, and heated and ventilated front seats. The only notable modifications reported by the seller are a K&N intake system and a Borla exhaust system.\n  - Released for the 2015 model year, the Challenger Hellcat significantly upped the stakes of the 21st Century Detroit Muscle War, debuting with an astonishing 707 horsepower. Performance was impressive to say the least, including a 3.6-second run to 60 mph and a top speed just 1 mph shy of the magical 200 figure.\n  - Power comes from a 6.2-liter supercharged V8 engine, rated at 707 horsepower and 650 lb-ft of torque. Output is sent to the rear wheels via a 6-speed manual transmission."
            },
            {
                "title": "EQUIPMENT",
                "content": "A window sticker is provided in the gallery, and a partial list of notable equipment reported by the seller includes:\n  - SRT-tuned Bilstein 3-mode active suspension system\n  - 20-inch wheels\n  - Laguna leather upholstery\n  - Heated and ventilated front seats\n  - Uconnect 8.4AN infotainment system"
            },
            {
                "title": "MODIFICATIONS",
                "content": "Notable modifications reported by the seller include:\n  - K&N intake system\n  - Borla exhaust system\n  - Red front intake tubes\n  - Red badges\n  - Black film on reflectors"
            },
            {
                "title": "KNOWN FLAWS",
                "content": "- The attachedCarfaxhistory report notes that this car sustained \"minor damage\" to its rear and right rear in a rear-end collision with another vehicle in May 2018. The report describes the damage as \"functional,\" but notes that the airbags did not deploy. The seller states that another car hit this Challenger \"at idle speed in bumper-to-bumper traffic\" and that the rear bumper was replaced.\n  - Some exterior chips, scratches, and dings\n  - Creases on the front seats"
            },
            {
                "title": "RECENT SERVICE HISTORY",
                "content": "The attachedCarfaxhistory report shows that the following services have been performed:\n  - October 2024 (39,057 miles): Engine oil and filter changed\n  - July 2021 (32,556 miles): Engine oil and filter changed"
            },
            {
                "title": "OTHER ITEMS INCLUDED IN SALE",
                "content": "- 1 red key\n  - Owner's manual"
            },
            {
                "title": "OWNERSHIP HISTORY",
                "content": "The seller reportedly purchased this Challenger in April 2018, sold it to a family member in December 2021, and bought it back in October 2024."
            },
            {
                "title": "SELLER NOTES",
                "content": "The seller states that the windows have been tinted."
            }
        ],
        "raw_description": "HIGHLIGHTS\n\nTHIS... is a 2015 Dodge Challenger SRT Hellcat, finished in Pitch Black with a black interior.\n  - This coupe is equipped with the desirable 6-speed manual transmission, and its odometer displays about 41,800 miles.\n  - The attachedCarfaxhistory report lists no mileage inconsistencies in this Challenger's past. It also shows that this car has been Florida-owned since new.\n  - A window sticker is provided in the gallery, and a partial list of notable equipment reported by the seller includes an SRT-tuned Bilstein 3-mode active suspension system, Laguna leather upholstery, and heated and ventilated front seats. The only notable modifications reported by the seller are a K&N intake system and a Borla exhaust system.\n  - Released for the 2015 model year, the Challenger Hellcat significantly upped the stakes of the 21st Century Detroit Muscle War, debuting with an astonishing 707 horsepower. Performance was impressive to say the least, including a 3.6-second run to 60 mph and a top speed just 1 mph shy of the magical 200 figure.\n  - Power comes from a 6.2-liter supercharged V8 engine, rated at 707 horsepower and 650 lb-ft of torque. Output is sent to the rear wheels via a 6-speed manual transmission.\n\nEQUIPMENT\n\nA window sticker is provided in the gallery, and a partial list of notable equipment reported by the seller includes:\n  - SRT-tuned Bilstein 3-mode active suspension system\n  - 20-inch wheels\n  - Laguna leather upholstery\n  - Heated and ventilated front seats\n  - Uconnect 8.4AN infotainment system\n\nMODIFICATIONS\n\nNotable modifications reported by the seller include:\n  - K&N intake system\n  - Borla exhaust system\n  - Red front intake tubes\n  - Red badges\n  - Black film on reflectors\n\nKNOWN FLAWS\n\n  - The attachedCarfaxhistory report notes that this car sustained \"minor damage\" to its rear and right rear in a rear-end collision with another vehicle in May 2018. The report describes the damage as \"functional,\" but notes that the airbags did not deploy. The seller states that another car hit this Challenger \"at idle speed in bumper-to-bumper traffic\" and that the rear bumper was replaced.\n  - Some exterior chips, scratches, and dings\n  - Creases on the front seats\n\nRECENT SERVICE HISTORY\n\nThe attachedCarfaxhistory report shows that the following services have been performed:\n  - October 2024 (39,057 miles): Engine oil and filter changed\n  - July 2021 (32,556 miles): Engine oil and filter changed\n\nOTHER ITEMS INCLUDED IN SALE\n\n  - 1 red key\n  - Owner's manual\n\nOWNERSHIP HISTORY\n\nThe seller reportedly purchased this Challenger in April 2018, sold it to a family member in December 2021, and bought it back in October 2024.\n\nSELLER NOTES\n\nThe seller states that the windows have been tinted."
    },
    "2025-bmw-m3-competition-xdrive": {
        "info": [
            {
                "label": "Title",
                "value": "2025 BMW M3 Competition xDrive"
            },
            {
                "label": "Make",
                "value": "BMW"
            },
            {
                "label": "Engine",
                "value": "3.0L Turbocharged I6"
            },
            {
                "label": "Model",
                "value": "G80 M3Save"
            },
            {
                "label": "Drivetrain",
                "value": "4WD/AWD"
            },
            {
                "label": "Mileage",
                "value": "11,000"
            },
            {
                "label": "Transmission",
                "value": "Automatic (8-Speed)"
            },
            {
                "label": "VIN",
                "value": "WBS33HJ00SFT72772"
            },
            {
                "label": "Body Style",
                "value": "Sedan"
            },
            {
                "label": "Title Status",
                "value": "Clean (NY)"
            },
            {
                "label": "Exterior Color",
                "value": "Dravit Gray Metallic"
            },
            {
                "label": "Location",
                "value": "Old Westbury, NY 11568"
            },
            {
                "label": "Interior Color",
                "value": "Black"
            },
            {
                "label": "Seller",
                "value": "scenic25"
            },
            {
                "label": "Seller Type",
                "value": "Private Party"
            }
        ],
        "sections": [
            {
                "title": "HIGHLIGHTS",
                "content": "THIS… is a 2025 BMW M3 Competition xDrive, finished in Dravit Gray Metallic with a black interior.\n  - The attachedCarfaxvehicle history report shows no accidents or mileage discrepancies in this M3's past.\n  - According to the window sticker provided in the gallery, notable factory equipment includes the Executive, Driving Assistance, and Parking Assistance packages, 19-inch front and 20-inch rear wheels, and an M Sport differential.\n  - Notable modifications reported by the seller include wheel spacers, an Autotecknic carbon fiber front grille and bumper vents, and blue-finished brake calipers.\n  - The G80 is the sixth incarnation of BMW's iconic M3, bringing a drastically new look and ever-increasing performance figures to the M3 lineage. The M3 is available in two flavors: a standard model with a 6-speed manual transmission and Competition trim with an 8-speed automatic. Building upon the previous generation M3's usage of forced induction, power availability has increased dramatically to between 463 horsepower (non-Competition models) and above 500 horsepower (Competition models).\n  - Power comes from a 3.0-liter twin-turbocharged inline-6, rated at 523 horsepower and 479 lb-ft of torque. Output is sent to all four wheels via an 8-speed automatic transmission."
            },
            {
                "title": "EQUIPMENT",
                "content": "A window sticker is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - Executive Package\n  - Driving Assistance Package\n  - Parking Assistance Package\n  - 19-inch front and 20-inch rear wheels\n  - M Sport differential\n  - Carbon fiber trim\n  - Extended Merino leather upholstery\n  - Power-adjustable, heated, and ventilated front seats"
            },
            {
                "title": "MODIFICATIONS",
                "content": "Notable modifications reported by the seller include:\n  - 10mm front and 12mm rear wheel spacers\n  - AutoTecknic dry carbon fiber Competizione GT4 front grille\n  - AutoTecknic dry carbon fiber bumper vents\n  - Blue-finished brake calipers\n  - Crystal door lock pin set and control panel nameplate"
            },
            {
                "title": "KNOWN FLAWS",
                "content": "- Scratch on the front paint protection film"
            },
            {
                "title": "RECENT SERVICE HISTORY",
                "content": "The attachedCarfaxhistory report shows that the following services have been performed:\n  - January 2026 (8,623 miles): Tire(s) replaced\n  - December 2025 (5,234 miles): Engine oil and filter changed, cabin air filter replaced"
            },
            {
                "title": "OTHER ITEMS INCLUDED IN SALE",
                "content": "- 3 keys (1 inoperable)\n  - Owner's manuals\n  - Window sticker\n  - Floor mats\n  - 1 extra tire"
            },
            {
                "title": "OWNERSHIP HISTORY",
                "content": "The seller reportedly purchased this M3 new in September 2024."
            },
            {
                "title": "SELLER NOTES",
                "content": "- There is a loan on this vehicle, and sale proceeds will be used to satisfy the loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif agreed to by both the buyer and the seller. Please note that the title may only be availableafterthe loan has been paid off.\n  - The seller states that paint protection film has been applied to the front end, rear, sides, and roof, that a ceramic coating has been applied, and that the windows have been tinted."
            }
        ],
        "raw_description": "HIGHLIGHTS\n\nTHIS… is a 2025 BMW M3 Competition xDrive, finished in Dravit Gray Metallic with a black interior.\n  - The attachedCarfaxvehicle history report shows no accidents or mileage discrepancies in this M3's past.\n  - According to the window sticker provided in the gallery, notable factory equipment includes the Executive, Driving Assistance, and Parking Assistance packages, 19-inch front and 20-inch rear wheels, and an M Sport differential.\n  - Notable modifications reported by the seller include wheel spacers, an Autotecknic carbon fiber front grille and bumper vents, and blue-finished brake calipers.\n  - The G80 is the sixth incarnation of BMW's iconic M3, bringing a drastically new look and ever-increasing performance figures to the M3 lineage. The M3 is available in two flavors: a standard model with a 6-speed manual transmission and Competition trim with an 8-speed automatic. Building upon the previous generation M3's usage of forced induction, power availability has increased dramatically to between 463 horsepower (non-Competition models) and above 500 horsepower (Competition models).\n  - Power comes from a 3.0-liter twin-turbocharged inline-6, rated at 523 horsepower and 479 lb-ft of torque. Output is sent to all four wheels via an 8-speed automatic transmission.\n\nEQUIPMENT\n\nA window sticker is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - Executive Package\n  - Driving Assistance Package\n  - Parking Assistance Package\n  - 19-inch front and 20-inch rear wheels\n  - M Sport differential\n  - Carbon fiber trim\n  - Extended Merino leather upholstery\n  - Power-adjustable, heated, and ventilated front seats\n\nMODIFICATIONS\n\nNotable modifications reported by the seller include:\n  - 10mm front and 12mm rear wheel spacers\n  - AutoTecknic dry carbon fiber Competizione GT4 front grille\n  - AutoTecknic dry carbon fiber bumper vents\n  - Blue-finished brake calipers\n  - Crystal door lock pin set and control panel nameplate\n\nKNOWN FLAWS\n\n  - Scratch on the front paint protection film\n\nRECENT SERVICE HISTORY\n\nThe attachedCarfaxhistory report shows that the following services have been performed:\n  - January 2026 (8,623 miles): Tire(s) replaced\n  - December 2025 (5,234 miles): Engine oil and filter changed, cabin air filter replaced\n\nOTHER ITEMS INCLUDED IN SALE\n\n  - 3 keys (1 inoperable)\n  - Owner's manuals\n  - Window sticker\n  - Floor mats\n  - 1 extra tire\n\nOWNERSHIP HISTORY\n\nThe seller reportedly purchased this M3 new in September 2024.\n\nSELLER NOTES\n\n  - There is a loan on this vehicle, and sale proceeds will be used to satisfy the loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif agreed to by both the buyer and the seller. Please note that the title may only be availableafterthe loan has been paid off.\n  - The seller states that paint protection film has been applied to the front end, rear, sides, and roof, that a ceramic coating has been applied, and that the windows have been tinted."
    },
    "2020-range-rover-sport-svr": {
        "info": [
            {
                "label": "Title",
                "value": "2020 Range Rover Sport SVR"
            },
            {
                "label": "Make",
                "value": "Land Rover"
            },
            {
                "label": "Engine",
                "value": "5.0L Supercharged V8"
            },
            {
                "label": "Model",
                "value": "Range Rover SportSave"
            },
            {
                "label": "Drivetrain",
                "value": "4WD/AWD"
            },
            {
                "label": "Mileage",
                "value": "59,800"
            },
            {
                "label": "Transmission",
                "value": "Automatic (8-Speed)"
            },
            {
                "label": "VIN",
                "value": "SALWZ2RE8LA717067"
            },
            {
                "label": "Body Style",
                "value": "SUV/Crossover"
            },
            {
                "label": "Title Status",
                "value": "Clean (FL)"
            },
            {
                "label": "Exterior Color",
                "value": "Santorini Black"
            },
            {
                "label": "Location",
                "value": "Miami Beach, FL 33140"
            },
            {
                "label": "Interior Color",
                "value": "Ebony/Vintage Tan"
            },
            {
                "label": "Seller",
                "value": "jona12"
            },
            {
                "label": "Seller Type",
                "value": "Dealer"
            }
        ],
        "sections": [
            {
                "title": "HIGHLIGHTS",
                "content": "THIS… is a 2020 Range Rover Sport SVR, finished in Santorini Black with an Ebony and Vintage Tan interior.\n  - The attachedCarfaxvehicle history report shows no mileage discrepancies in this Range Rover’s past. It also shows that this SVR has been registered in Florida since new.\n  - According to the build sheet provided in the gallery, this Range Rover Sport is an SVR model, and notable factory equipment includes the Driver Assist and Towing packs, heated and cooled front and rear seats, and a Meridian surround sound system. The selling dealer reports no notable modifications.\n  - Land Rover released the second-generation Range Rover Sport for the 2014 model year. It ditched its predecessor's angular design and adopted a softer, more rounded look inspired by the full-size Range Rover, but it continued to offer a unique blend of on-road performance and off-road prowess. Entry-level models received a V6, but upmarket trim levels like the SVR benefited from Land Rover's mighty V8.\n  - Power comes from a 5.0-liter supercharged V8 engine, rated at 575 horsepower and 516 lb-ft of torque. Output is sent to all four wheels via an 8-speed automatic transmission."
            },
            {
                "title": "EQUIPMENT",
                "content": "This Range Rover Sport is an SVR model. A build sheet is provided in the photo gallery, and a partial list of notable equipment reported by the selling dealer includes:\n  - Driver Assist Pack\n  - Towing Pack\n  - 22-inch Style 5083 wheels\n  - Heated and cooled front and rear seats\n  - Extended leather interior trim\n  - Head-up display\n  - Meridian surround sound system"
            },
            {
                "title": "KNOWN FLAWS",
                "content": "- The attachedCarfaxhistory report indicates that this Range Rover was involved in an accident in March 2024 that resulted in \"minor damage” to the rear.\n  - Some chips on front end and mirror caps"
            },
            {
                "title": "RECENT SERVICE HISTORY",
                "content": "The attachedCarfaxhistory report shows that the following services have been performed:\n  - August 2025: A/C refrigerant recharged\n  - September 2024 (47,908 miles): Tire(s) replaced\n  - June 2024 (45,746 miles): 4-wheel alignment performed, engine oil and filter changed, rear window regulator(s) replaced, tire(s) balanced and rotated\n  - May 2023 (35,469 miles): Air filter and front brake rotors and pads replaced, 4 tires mounted and balanced, 4-wheel alignment performed, engine oil and filter changed, wheels repaired\n  - December 2022 (30,599 miles): Wheel(s) repaired\n  - August 2022 (27,365 miles): 1 tire repaired, rear brake rotor(s) replaced\n  - April 2022 (23,713 miles): Air filter replaced, engine oil and filter changed, tires rotated\n  - November 2021 (20,542 miles): 1 tire repaired\n  - November 2021 (20,035 miles): Tire(s) replaced, wheel(s) repaired\n  - July 2021 (17,219 miles): 1 tire mounted, wheel(s) repaired"
            },
            {
                "title": "OTHER ITEMS INCLUDED IN SALE",
                "content": "- 1 key\n  - Owner's manuals\n  - Rubber floor mats and cargo mat\n  - Spare tire"
            },
            {
                "title": "OWNERSHIP HISTORY",
                "content": "The selling dealer reports that they acquired this Range Rover in November 2025 and have added approximately 4,100 miles since."
            },
            {
                "title": "SELLER NOTES",
                "content": "The selling dealer will collect sales tax from Florida buyers, as well as states that have state tax reciprocity agreements with Florida."
            }
        ],
        "raw_description": "HIGHLIGHTS\n\nTHIS… is a 2020 Range Rover Sport SVR, finished in Santorini Black with an Ebony and Vintage Tan interior.\n  - The attachedCarfaxvehicle history report shows no mileage discrepancies in this Range Rover’s past. It also shows that this SVR has been registered in Florida since new.\n  - According to the build sheet provided in the gallery, this Range Rover Sport is an SVR model, and notable factory equipment includes the Driver Assist and Towing packs, heated and cooled front and rear seats, and a Meridian surround sound system. The selling dealer reports no notable modifications.\n  - Land Rover released the second-generation Range Rover Sport for the 2014 model year. It ditched its predecessor's angular design and adopted a softer, more rounded look inspired by the full-size Range Rover, but it continued to offer a unique blend of on-road performance and off-road prowess. Entry-level models received a V6, but upmarket trim levels like the SVR benefited from Land Rover's mighty V8.\n  - Power comes from a 5.0-liter supercharged V8 engine, rated at 575 horsepower and 516 lb-ft of torque. Output is sent to all four wheels via an 8-speed automatic transmission.\n\nEQUIPMENT\n\nThis Range Rover Sport is an SVR model. A build sheet is provided in the photo gallery, and a partial list of notable equipment reported by the selling dealer includes:\n  - Driver Assist Pack\n  - Towing Pack\n  - 22-inch Style 5083 wheels\n  - Heated and cooled front and rear seats\n  - Extended leather interior trim\n  - Head-up display\n  - Meridian surround sound system\n\nKNOWN FLAWS\n\n  - The attachedCarfaxhistory report indicates that this Range Rover was involved in an accident in March 2024 that resulted in \"minor damage” to the rear.\n  - Some chips on front end and mirror caps\n\nRECENT SERVICE HISTORY\n\nThe attachedCarfaxhistory report shows that the following services have been performed:\n  - August 2025: A/C refrigerant recharged\n  - September 2024 (47,908 miles): Tire(s) replaced\n  - June 2024 (45,746 miles): 4-wheel alignment performed, engine oil and filter changed, rear window regulator(s) replaced, tire(s) balanced and rotated\n  - May 2023 (35,469 miles): Air filter and front brake rotors and pads replaced, 4 tires mounted and balanced, 4-wheel alignment performed, engine oil and filter changed, wheels repaired\n  - December 2022 (30,599 miles): Wheel(s) repaired\n  - August 2022 (27,365 miles): 1 tire repaired, rear brake rotor(s) replaced\n  - April 2022 (23,713 miles): Air filter replaced, engine oil and filter changed, tires rotated\n  - November 2021 (20,542 miles): 1 tire repaired\n  - November 2021 (20,035 miles): Tire(s) replaced, wheel(s) repaired\n  - July 2021 (17,219 miles): 1 tire mounted, wheel(s) repaired\n\nOTHER ITEMS INCLUDED IN SALE\n\n  - 1 key\n  - Owner's manuals\n  - Rubber floor mats and cargo mat\n  - Spare tire\n\nOWNERSHIP HISTORY\n\nThe selling dealer reports that they acquired this Range Rover in November 2025 and have added approximately 4,100 miles since.\n\nSELLER NOTES\n\nThe selling dealer will collect sales tax from Florida buyers, as well as states that have state tax reciprocity agreements with Florida."
    },
    "2025-bmw-m2": {
        "info": [
            {
                "label": "Title",
                "value": "2025 BMW M2"
            },
            {
                "label": "Make",
                "value": "BMW"
            },
            {
                "label": "Engine",
                "value": "3.0L Turbocharged I6"
            },
            {
                "label": "Model",
                "value": "M2Save"
            },
            {
                "label": "Drivetrain",
                "value": "Rear-wheel drive"
            },
            {
                "label": "Mileage",
                "value": "15,400"
            },
            {
                "label": "Transmission",
                "value": "Manual (6-Speed)"
            },
            {
                "label": "VIN",
                "value": "3MF23DM09S8F25064"
            },
            {
                "label": "Body Style",
                "value": "Coupe"
            },
            {
                "label": "Title Status",
                "value": "Clean (TN)"
            },
            {
                "label": "Exterior Color",
                "value": "Zandvoort Blue"
            },
            {
                "label": "Location",
                "value": "Marietta, GA 30062"
            },
            {
                "label": "Interior Color",
                "value": "Black"
            },
            {
                "label": "Seller",
                "value": "SCoastMotors"
            },
            {
                "label": "Seller Type",
                "value": "Dealer ($449 Document Fee)"
            }
        ],
        "sections": [
            {
                "title": "HIGHLIGHTS",
                "content": "THIS... is a 2025 BMW M2, finished in Zandvoort Blue with a black interior.\n  - This M2 features the desirable 6-speed manual transmission.\n  - The attachedCarfaxvehicle history report shows no accidents or mileage discrepancies in this M2’s past.\n  - According to the window sticker provided in the gallery, notable factory equipment includes the M Drive Professional and Lighting packages, 19-inch front and 20-inch rear Style 930M wheels, an adaptive M suspension, an M Sport differential, a carbon fiber interior trim, the Live Cockpit Pro system, and a Harman/Kardon surround sound system. The selling dealer reports no notable modifications.\n  - Introduced in 2023 and marked by its muscular exterior design, flared fenders, and a departure from the oversized kidney grilles seen on other recent BMWs, the second-gen M2 reemphasized traditional M division values. Lauded for its compact dimensions, agile, rear-wheel-drive chassis, and powerful turbocharged straight-six, the G87 is among the most compelling German-engineered driver's cars on sale today, particularly when paired with a 6-speed manual like this example. The 2025 M2 saw a 20-horsepower bump in output over previous model years.\n  - Power comes from a 3.0-liter twin-turbocharged inline-6, rated at 473 horsepower and 406 lb-ft of torque. Output is sent to the rear wheels via a 6-speed manual transmission."
            },
            {
                "title": "EQUIPMENT",
                "content": "A window sticker is provided in the photo gallery, and a partial list of notable equipment reported by the selling dealer includes:\n  - M Drive Professional Package\n  - Lighting Package\n  - 19-inch front and 20-inch rear Style 930M wheels\n  - Adaptive M suspension\n  - M Sport differential\n  - Carbon fiber interior trim\n  - Live Cockpit Pro\n  - Harman/Kardon surround sound system"
            },
            {
                "title": "KNOWN FLAWS",
                "content": "- Some curb rash on rear wheels and a scuff on the passenger's side rear tire sidewall"
            },
            {
                "title": "RECENT SERVICE HISTORY",
                "content": "A service sticker in the photo gallery indicates that the following maintenance has been performed:\n  - January 2025: Fabric protection, glass protection, interior protective coating, and paint protection coating applied\nThe attachedCarfaxhistory report shows that the following services have been performed:\n  - November 2025 (9,912 miles): Anti-theft/keyless remote battery replaced, engine oil and filter changed\n  - February 2025 (1,130 miles): Computer reprogrammed, engine oil and filter changed\n  - January 2025: Four tires replaced and mounted, two-wheel alignment performed\nSome additional service history is detailed in the attachedCarfaxhistory report."
            },
            {
                "title": "OTHER ITEMS INCLUDED IN SALE",
                "content": "- 2 keys\n  - Owner's manuals\n  - Window sticker\n  - Floor mats"
            },
            {
                "title": "OWNERSHIP HISTORY",
                "content": "The selling dealer reports that they acquired this M2 in May 2026 and have added minimal miles since."
            },
            {
                "title": "SELLER NOTES",
                "content": "- The selling dealer charges a $449 documentation fee to the winning bidder and will collect sales tax from Georgia buyers.\n  - The selling dealer reports that fabric protection has been applied to the upholstery, and that paint protection coating has been applied to the exterior."
            }
        ],
        "raw_description": "HIGHLIGHTS\n\nTHIS... is a 2025 BMW M2, finished in Zandvoort Blue with a black interior.\n  - This M2 features the desirable 6-speed manual transmission.\n  - The attachedCarfaxvehicle history report shows no accidents or mileage discrepancies in this M2’s past.\n  - According to the window sticker provided in the gallery, notable factory equipment includes the M Drive Professional and Lighting packages, 19-inch front and 20-inch rear Style 930M wheels, an adaptive M suspension, an M Sport differential, a carbon fiber interior trim, the Live Cockpit Pro system, and a Harman/Kardon surround sound system. The selling dealer reports no notable modifications.\n  - Introduced in 2023 and marked by its muscular exterior design, flared fenders, and a departure from the oversized kidney grilles seen on other recent BMWs, the second-gen M2 reemphasized traditional M division values. Lauded for its compact dimensions, agile, rear-wheel-drive chassis, and powerful turbocharged straight-six, the G87 is among the most compelling German-engineered driver's cars on sale today, particularly when paired with a 6-speed manual like this example. The 2025 M2 saw a 20-horsepower bump in output over previous model years.\n  - Power comes from a 3.0-liter twin-turbocharged inline-6, rated at 473 horsepower and 406 lb-ft of torque. Output is sent to the rear wheels via a 6-speed manual transmission.\n\nEQUIPMENT\n\nA window sticker is provided in the photo gallery, and a partial list of notable equipment reported by the selling dealer includes:\n  - M Drive Professional Package\n  - Lighting Package\n  - 19-inch front and 20-inch rear Style 930M wheels\n  - Adaptive M suspension\n  - M Sport differential\n  - Carbon fiber interior trim\n  - Live Cockpit Pro\n  - Harman/Kardon surround sound system\n\nKNOWN FLAWS\n\n  - Some curb rash on rear wheels and a scuff on the passenger's side rear tire sidewall\n\nRECENT SERVICE HISTORY\n\nA service sticker in the photo gallery indicates that the following maintenance has been performed:\n  - January 2025: Fabric protection, glass protection, interior protective coating, and paint protection coating applied\nThe attachedCarfaxhistory report shows that the following services have been performed:\n  - November 2025 (9,912 miles): Anti-theft/keyless remote battery replaced, engine oil and filter changed\n  - February 2025 (1,130 miles): Computer reprogrammed, engine oil and filter changed\n  - January 2025: Four tires replaced and mounted, two-wheel alignment performed\nSome additional service history is detailed in the attachedCarfaxhistory report.\n\nOTHER ITEMS INCLUDED IN SALE\n\n  - 2 keys\n  - Owner's manuals\n  - Window sticker\n  - Floor mats\n\nOWNERSHIP HISTORY\n\nThe selling dealer reports that they acquired this M2 in May 2026 and have added minimal miles since.\n\nSELLER NOTES\n\n  - The selling dealer charges a $449 documentation fee to the winning bidder and will collect sales tax from Georgia buyers.\n  - The selling dealer reports that fabric protection has been applied to the upholstery, and that paint protection coating has been applied to the exterior."
    },
    "2021-ford-f-350-super-duty-platinum-4x4": {
        "info": [
            {
                "label": "Title",
                "value": "2021 Ford F-350 Super Duty Platinum 4x4"
            },
            {
                "label": "Make",
                "value": "Ford"
            },
            {
                "label": "Engine",
                "value": "6.7L Turbodiesel V8"
            },
            {
                "label": "Model",
                "value": "Super DutySave"
            },
            {
                "label": "Drivetrain",
                "value": "4WD/AWD"
            },
            {
                "label": "Mileage",
                "value": "50,200"
            },
            {
                "label": "Transmission",
                "value": "Automatic (10-Speed)"
            },
            {
                "label": "VIN",
                "value": "1FT8W3BT4MEC15786"
            },
            {
                "label": "Body Style",
                "value": "Truck"
            },
            {
                "label": "Title Status",
                "value": "Clean (WA)"
            },
            {
                "label": "Exterior Color",
                "value": "Iconic Silver"
            },
            {
                "label": "Location",
                "value": "Lake Geneva, WI 53147"
            },
            {
                "label": "Interior Color",
                "value": "Black"
            },
            {
                "label": "Seller",
                "value": "Laura70"
            },
            {
                "label": "Seller Type",
                "value": "Private Party"
            }
        ],
        "sections": [
            {
                "title": "HIGHLIGHTS",
                "content": "THIS... is a 2021 Ford F-350 Super Duty Platinum 4x4, finished in Iconic Silver with a black interior.\n  - This F-350 is a Canadian-spec Ford that's titled in Washington and located in Wisconsin.\n  - The attachedCarfaxvehicle history report shows no accidents or mileage discrepancies in this Ford’s past.\n  - According to the digital window sticker provided in the gallery, notable factory equipment includes the Tremor Off-Road and 5th Wheel Hitch Prep packages, a Tough Bed spray-in bedliner, and a power twin-panel sunroof. The seller reports no notable modifications.\n  - Ford released the fourth-generation F-Series Super Duty for the 2017 model year. Offered in a diverse selection of configurations, the truck weighed up to 350 pounds less than its predecessor, thanks in part to the widespread use of aluminum, a trick learned from the smaller F-150. More powerful engines, beefier four-wheel drive hardware, and a longer list of available tech and comfort features rounded out the list of updates.\n  - Power comes from a Power Stroke 6.7-liter turbodiesel V8, rated at 475 horsepower and 1,050 lb-ft of torque. Output is sent to the rear or all four wheels via a 10-speed automatic transmission and a 2-speed transfer case."
            },
            {
                "title": "EQUIPMENT",
                "content": "This F-350 is a Platinum model. A digital window sticker is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - Tremor Off-Road Package\n  - 5th Wheel Hitch Prep Package\n  - Tough Bed spray-in bedliner\n  - Tailgate step\n  - Power twin-panel sunroof\n  - Leather upholstery\n  - Power-adjustable, heated, and ventilated front seats with massage function\n  - Heated rear seats"
            },
            {
                "title": "KNOWN FLAWS",
                "content": "- Chips and scratches around the exterior\n  - Some creases on front seat bolsters\n  - Wear on interior touch points"
            },
            {
                "title": "RECENT SERVICE HISTORY",
                "content": "The attachedCarfaxhistory report shows that the following services have been performed:\n  - July 2023 (39,611 miles): Four tires and fuel filler cap replaced\n  - June 2023 (39,395 miles): Engine oil and filter changed\n  - January 2023 (30,546 miles): Engine oil and filter changed\n  - September 2022 (23,052 miles): 5,000-mile service performed, engine oil and filter changed, engine/powertrain computer/module reprogrammed\n  - March 2022: Engine oil and filter changed\nThe seller reports that the following services have been performed, although no documentation was provided to verify:\n  - April 2026: Batteries replaced\nAdditional service history is detailed in the attachedCarfaxreport."
            },
            {
                "title": "OTHER ITEMS INCLUDED IN SALE",
                "content": "- 2 key fobs\n  - Factory all-weather floor mats\n  - Andersen hitch"
            },
            {
                "title": "OWNERSHIP HISTORY",
                "content": "The seller reports that they purchased this F-350 in April 2022."
            }
        ],
        "raw_description": "HIGHLIGHTS\n\nTHIS... is a 2021 Ford F-350 Super Duty Platinum 4x4, finished in Iconic Silver with a black interior.\n  - This F-350 is a Canadian-spec Ford that's titled in Washington and located in Wisconsin.\n  - The attachedCarfaxvehicle history report shows no accidents or mileage discrepancies in this Ford’s past.\n  - According to the digital window sticker provided in the gallery, notable factory equipment includes the Tremor Off-Road and 5th Wheel Hitch Prep packages, a Tough Bed spray-in bedliner, and a power twin-panel sunroof. The seller reports no notable modifications.\n  - Ford released the fourth-generation F-Series Super Duty for the 2017 model year. Offered in a diverse selection of configurations, the truck weighed up to 350 pounds less than its predecessor, thanks in part to the widespread use of aluminum, a trick learned from the smaller F-150. More powerful engines, beefier four-wheel drive hardware, and a longer list of available tech and comfort features rounded out the list of updates.\n  - Power comes from a Power Stroke 6.7-liter turbodiesel V8, rated at 475 horsepower and 1,050 lb-ft of torque. Output is sent to the rear or all four wheels via a 10-speed automatic transmission and a 2-speed transfer case.\n\nEQUIPMENT\n\nThis F-350 is a Platinum model. A digital window sticker is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - Tremor Off-Road Package\n  - 5th Wheel Hitch Prep Package\n  - Tough Bed spray-in bedliner\n  - Tailgate step\n  - Power twin-panel sunroof\n  - Leather upholstery\n  - Power-adjustable, heated, and ventilated front seats with massage function\n  - Heated rear seats\n\nKNOWN FLAWS\n\n  - Chips and scratches around the exterior\n  - Some creases on front seat bolsters\n  - Wear on interior touch points\n\nRECENT SERVICE HISTORY\n\nThe attachedCarfaxhistory report shows that the following services have been performed:\n  - July 2023 (39,611 miles): Four tires and fuel filler cap replaced\n  - June 2023 (39,395 miles): Engine oil and filter changed\n  - January 2023 (30,546 miles): Engine oil and filter changed\n  - September 2022 (23,052 miles): 5,000-mile service performed, engine oil and filter changed, engine/powertrain computer/module reprogrammed\n  - March 2022: Engine oil and filter changed\nThe seller reports that the following services have been performed, although no documentation was provided to verify:\n  - April 2026: Batteries replaced\nAdditional service history is detailed in the attachedCarfaxreport.\n\nOTHER ITEMS INCLUDED IN SALE\n\n  - 2 key fobs\n  - Factory all-weather floor mats\n  - Andersen hitch\n\nOWNERSHIP HISTORY\n\nThe seller reports that they purchased this F-350 in April 2022."
    },
    "2022-ford-f-150-lightning-lariat": {
        "info": [
            {
                "label": "Title",
                "value": "2022 Ford F-150 Lightning Lariat"
            },
            {
                "label": "Make",
                "value": "Ford"
            },
            {
                "label": "Engine",
                "value": "Dual Electric Motors"
            },
            {
                "label": "Model",
                "value": "F-150Save"
            },
            {
                "label": "Drivetrain",
                "value": "4WD/AWD"
            },
            {
                "label": "Mileage",
                "value": "65,800"
            },
            {
                "label": "Transmission",
                "value": "Automatic"
            },
            {
                "label": "VIN",
                "value": "1FT6W1EV6NWG07592"
            },
            {
                "label": "Body Style",
                "value": "Truck"
            },
            {
                "label": "Title Status",
                "value": "Clean (MD)"
            },
            {
                "label": "Exterior Color",
                "value": "Atlas Blue Metallic"
            },
            {
                "label": "Location",
                "value": "Ellicott City, MD 21042"
            },
            {
                "label": "Interior Color",
                "value": "Black/Gray"
            },
            {
                "label": "Seller",
                "value": "robatumd21"
            },
            {
                "label": "Seller Type",
                "value": "Private Party"
            }
        ],
        "sections": [
            {
                "title": "HIGHLIGHTS",
                "content": "THIS... is a 2022 Ford F-150 Lightning Lariat, finished in Atlas Blue Metallic with a black and gray interior.\n  - The attachedCarfaxhistory report lists no accidents or mileage discrepancies in this Lightning's past.\n  - According to the window sticker provided in the gallery, this F-150 Lightning is a Lariat model, and notable factory equipment includes 20-inch wheels, an extended range battery, a twin panel sunroof, leather upholstery, heated and ventilated front seats, a 360-degree camera, Ford Co-Pilot360 Active 2.0 with BlueCruise, and a Bang & Olufsen sound system.\n  - Notable modifications reported by the seller are limited to an A.R.E. Classic truck cap and a BedRug bed liner.\n  - Formerly used on a high-performance variant of the F-150, the Lightning nameplate was revived for the 2022 model year for Ford's first series-produced electric truck. Every member of the line-up offers dual electric motors for through-the-road four-wheel drive, but buyers have two battery packs to choose from and driving range varies accordingly.\n  - Power comes from a pair of electric motors (one per axle), which draw electricity from a 131-kilowatt-hour lithium-ion battery pack to turn all four wheels with 580 horsepower and 775 lb-ft of torque. In 2022, the Lightning with the extended-range battery received a maximum driving range rating of 320 miles from the EPA."
            },
            {
                "title": "EQUIPMENT",
                "content": "This  F-150 Lightning is a Lariat model. A window sticker is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - 20-inch wheels\n  - Extended-range battery\n  - Electric drive e-lock rear axle\n  - Twin panel sunroof\n  - Leather upholstery\n  - Heated and ventilated front seats\n  - Heated rear seats\n  - 360-degree camera\n  - Ford Co-Pilot360 Active 2.0 with BlueCruise\n  - Bang & Olufsen sound system"
            },
            {
                "title": "MODIFICATIONS",
                "content": "Notable modifications reported by the seller include:\n  - A.R.E. Classic truck cap\n  - BedRug bed liner"
            },
            {
                "title": "KNOWN FLAWS",
                "content": "- Some chips and scratches around the exterior"
            },
            {
                "title": "RECENT SERVICE HISTORY",
                "content": "Service documentation in the photo gallery indicates that the following maintenance has been performed:\n  - June 2026 (65,688 miles): Recall campaigns performed, multi-point inspection performed\n  - January 2026 (61,559 miles): Multi-point inspection performed\n  - April 2025 (51,842 miles): 12-volt battery replaced, software updated\n  - March 2025 (50,940 miles): Recall campaigns performed\n  - April 2024 (38,782 miles):  Tires rotated, multi-point inspection performed\n  - December 2023 (33,279 miles): Recall campaigns performed"
            },
            {
                "title": "OTHER ITEMS INCLUDED IN SALE",
                "content": "- 2 keys\n  - Owner's manual\n  - Window sticker\n  - Service records\n  - Charging cable and adapter"
            },
            {
                "title": "OWNERSHIP HISTORY",
                "content": "The seller reportedly purchased this Lightning in July 2023."
            },
            {
                "title": "SELLER NOTES",
                "content": "There is a loan on this vehicle, and sale proceeds will be used to satisfy the loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif agreed to by both the buyer and the seller. Please note that the title may only be availableafterthe loan has been paid off."
            }
        ],
        "raw_description": "HIGHLIGHTS\n\nTHIS... is a 2022 Ford F-150 Lightning Lariat, finished in Atlas Blue Metallic with a black and gray interior.\n  - The attachedCarfaxhistory report lists no accidents or mileage discrepancies in this Lightning's past.\n  - According to the window sticker provided in the gallery, this F-150 Lightning is a Lariat model, and notable factory equipment includes 20-inch wheels, an extended range battery, a twin panel sunroof, leather upholstery, heated and ventilated front seats, a 360-degree camera, Ford Co-Pilot360 Active 2.0 with BlueCruise, and a Bang & Olufsen sound system.\n  - Notable modifications reported by the seller are limited to an A.R.E. Classic truck cap and a BedRug bed liner.\n  - Formerly used on a high-performance variant of the F-150, the Lightning nameplate was revived for the 2022 model year for Ford's first series-produced electric truck. Every member of the line-up offers dual electric motors for through-the-road four-wheel drive, but buyers have two battery packs to choose from and driving range varies accordingly.\n  - Power comes from a pair of electric motors (one per axle), which draw electricity from a 131-kilowatt-hour lithium-ion battery pack to turn all four wheels with 580 horsepower and 775 lb-ft of torque. In 2022, the Lightning with the extended-range battery received a maximum driving range rating of 320 miles from the EPA.\n\nEQUIPMENT\n\nThis  F-150 Lightning is a Lariat model. A window sticker is provided in the photo gallery, and a partial list of notable equipment reported by the seller includes:\n  - 20-inch wheels\n  - Extended-range battery\n  - Electric drive e-lock rear axle\n  - Twin panel sunroof\n  - Leather upholstery\n  - Heated and ventilated front seats\n  - Heated rear seats\n  - 360-degree camera\n  - Ford Co-Pilot360 Active 2.0 with BlueCruise\n  - Bang & Olufsen sound system\n\nMODIFICATIONS\n\nNotable modifications reported by the seller include:\n  - A.R.E. Classic truck cap\n  - BedRug bed liner\n\nKNOWN FLAWS\n\n  - Some chips and scratches around the exterior\n\nRECENT SERVICE HISTORY\n\nService documentation in the photo gallery indicates that the following maintenance has been performed:\n  - June 2026 (65,688 miles): Recall campaigns performed, multi-point inspection performed\n  - January 2026 (61,559 miles): Multi-point inspection performed\n  - April 2025 (51,842 miles): 12-volt battery replaced, software updated\n  - March 2025 (50,940 miles): Recall campaigns performed\n  - April 2024 (38,782 miles):  Tires rotated, multi-point inspection performed\n  - December 2023 (33,279 miles): Recall campaigns performed\n\nOTHER ITEMS INCLUDED IN SALE\n\n  - 2 keys\n  - Owner's manual\n  - Window sticker\n  - Service records\n  - Charging cable and adapter\n\nOWNERSHIP HISTORY\n\nThe seller reportedly purchased this Lightning in July 2023.\n\nSELLER NOTES\n\nThere is a loan on this vehicle, and sale proceeds will be used to satisfy the loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif agreed to by both the buyer and the seller. Please note that the title may only be availableafterthe loan has been paid off."
    }
}


def upgrade() -> None:
    op.add_column("vehicles", sa.Column("details", sa.JSON(), nullable=True))

    vehicles = sa.table(
        "vehicles",
        sa.column("id", sa.String),
        sa.column("details", sa.JSON),
    )
    connection = op.get_bind()

    for vehicle_id, details in VEHICLE_DETAILS.items():
        connection.execute(
            vehicles.update().where(vehicles.c.id == vehicle_id).values(details=details)
        )

    connection.execute(
        vehicles.update().where(vehicles.c.details.is_(None)).values(details={})
    )
    op.alter_column("vehicles", "details", nullable=False)


def downgrade() -> None:
    op.drop_column("vehicles", "details")
