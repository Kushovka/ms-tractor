"""add more inventory and prices

Revision ID: 20260728_0005
Revises: 20260721_0004
Create Date: 2026-07-28
"""

from datetime import datetime

from alembic import op
import sqlalchemy as sa


revision = "20260728_0005"
down_revision = "20260721_0004"
branch_labels = None
depends_on = None


CREATED_AT = datetime(2026, 7, 28)


PRICE_UPDATES = {'2022-porsche-911-carrera-s-coupe': 94999,
 '2025-ford-f-150-raptor': 58999,
 '2017-porsche-macan-gts': 16999,
 '2015-dodge-challenger-srt-hellcat': 31999,
 '2025-bmw-m3-competition-xdrive': 62999,
 '2020-range-rover-sport-svr': 34999,
 '2025-bmw-m2': 46999,
 '2021-ford-f-350-super-duty-platinum-4x4': 39999,
 '2022-ford-f-150-lightning-lariat': 23999,
 '2018-ford-f-150-raptor': 28999,
 '2024-ford-f-150-raptor-r': 80999,
 '2025-ford-f-150-raptor-r': 94999,
 '2024-ford-f-450-super-duty-limited-4x4': 59999,
 '2021-mercedes-amg-e63-s-sedan': 52999,
 '2024-audi-rs-q8': 81999,
 '2026-ram-1500-rho-crew-cab-4x4': 49999}


NEW_VEHICLES = [{'id': '2018-ford-f-150-raptor',
  'slug': '2018-ford-f-150-raptor',
  'title': '2018 Ford F-150 Raptor',
  'make': 'Ford',
  'model': 'F-150',
  'trim': 'Raptor',
  'year': 2018,
  'status': 'Available',
  'stock_number': 'RUC82906',
  'vin': '1FTFW1RG5JFB82906',
  'price': 28999,
  'mileage': 82100,
  'body_type': 'Truck',
  'transmission': 'Automatic (10-Speed)',
  'drivetrain': '4WD/AWD',
  'engine': '3.5L Turbocharged V6',
  'exterior_color': 'Lightning Blue',
  'interior_color': 'Black',
  'location': 'Commodore, PA',
  'short_description': '2018 Ford F-150 Raptor finished in Lightning Blue with a Black interior, 82,100 miles, and '
                       '3.5L Turbocharged V6.',
  'description': 'THIS... is a 2018 Ford F-150 Raptor, finished in Lightning Blue with a black interior.',
  'images': ['/media/vehicles/2018-ford-f-150-raptor/01.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/02.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/03.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/04.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/05.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/06.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/07.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/08.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/09.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/10.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/11.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/12.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/13.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/14.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/15.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/16.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/17.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/18.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/19.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/20.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/21.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/22.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/23.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/24.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/25.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/26.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/27.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/28.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/29.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/30.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/31.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/32.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/33.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/34.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/35.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/36.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/37.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/38.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/39.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/40.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/41.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/42.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/43.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/44.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/45.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/46.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/47.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/48.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/49.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/50.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/51.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/52.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/53.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/54.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/55.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/56.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/57.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/58.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/59.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/60.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/61.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/62.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/63.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/64.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/65.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/66.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/67.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/68.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/69.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/70.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/71.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/72.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/73.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/74.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/75.jpg',
             '/media/vehicles/2018-ford-f-150-raptor/76.png',
             '/media/vehicles/2018-ford-f-150-raptor/77.png',
             '/media/vehicles/2018-ford-f-150-raptor/78.png'],
  'features': ['Equipment Group 800A', 'Running boards', 'Cloth upholstery', 'Air conditioning', 'CD player'],
  'specs': {},
  'details': {'info': [{'label': 'Title', 'value': '2018 Ford F-150 Raptor'},
                       {'label': 'Make', 'value': 'Ford'},
                       {'label': 'Engine', 'value': '3.5L Turbocharged V6'},
                       {'label': 'Model', 'value': 'F-150 RaptorSave'},
                       {'label': 'Drivetrain', 'value': '4WD/AWD'},
                       {'label': 'Mileage', 'value': '82,100'},
                       {'label': 'Transmission', 'value': 'Automatic (10-Speed)'},
                       {'label': 'VIN', 'value': '1FTFW1RG5JFB82906'},
                       {'label': 'Body Style', 'value': 'Truck'},
                       {'label': 'Title Status', 'value': 'Clean (AZ)'},
                       {'label': 'Exterior Color', 'value': 'Lightning Blue'},
                       {'label': 'Location', 'value': 'Phoenix, AZ 85015'},
                       {'label': 'Interior Color', 'value': 'Black'},
                       {'label': 'Seller', 'value': 'istillwannarock'},
                       {'label': 'Seller Type', 'value': 'Private Party'}],
              'sections': [{'title': 'HIGHLIGHTS',
                            'content': 'THIS... is a 2018 Ford F-150 Raptor, finished in Lightning Blue with a black '
                                       'interior.\n'
                                       '  - The attachedCarfaxvehicle history report shows no accidents or mileage '
                                       'discrepancies in this Raptor’s past.\n'
                                       '  - According to the digital window sticker provided in the gallery, notable '
                                       'factory equipment includes Equipment Group 800A, running boards, cloth '
                                       'upholstery, and a rearview camera.\n'
                                       '  - Notable modifications reported by the seller include 17-inch Gen-3 Raptor '
                                       'wheels, a Goosetuned TCM tune, aftermarket fog lights, a LINE-X spray-on '
                                       'bedliner, and a folding bed cover.\n'
                                       '  - Designed to speed across the desert, Baja racing-style, the '
                                       'second-generation F-150 Raptor made its debut for the 2017 model year with an '
                                       'impressive list of off-road hardware and more horsepower from a downsized, '
                                       'twin-turbocharged V6 engine. It weighed about 500 pounds less than its '
                                       'predecessor, thanks in part to the widespread use of aluminum. Production '
                                       'ended in 2020.\n'
                                       '  - Power comes from a 3.5-liter twin-turbocharged V6, rated at 450 horsepower '
                                       'and 510 lb-ft of torque. Output is sent to the rear or all four wheels via a '
                                       '10-speed automatic transmission and a 2-speed transfer case.'},
                           {'title': 'EQUIPMENT',
                            'content': 'A digital window sticker is provided in the photo gallery, and a partial list '
                                       'of notable equipment reported by the seller includes:\n'
                                       '  - Equipment Group 800A\n'
                                       '  - Running boards\n'
                                       '  - Cloth upholstery\n'
                                       '  - Air conditioning\n'
                                       '  - CD player\n'
                                       '  - Cruise control\n'
                                       '  - Rearview camera'},
                           {'title': 'MODIFICATIONS',
                            'content': 'Notable modifications reported by the seller include:\n'
                                       '  - 17-inch Gen-3 Raptor wheels\n'
                                       '  - Goosetuned TCM tune\n'
                                       '  - Aftermarket fog lights\n'
                                       '  - LINE-X spray-on bedliner\n'
                                       '  - Folding bed cover'},
                           {'title': 'KNOWN FLAWS',
                            'content': '- Chips on front-end components; some scratches on plastic fender flares\n'
                                       '  - Scratches on glove box lid'},
                           {'title': 'RECENT SERVICE HISTORY',
                            'content': 'Service documentation in the photo gallery indicates that the following '
                                       'maintenance has been performed:\n'
                                       '  - March 2026: Engine oil and filter changed, ignition coils replaced\n'
                                       '  - December 2025 (75,192 miles): Fuel induction service performed\n'
                                       '  - October 2025 (73,709 miles): VCT camshaft phasers, camshaft sprockets, '
                                       'valve cover bolts, and water pump gasket replaced\n'
                                       '  - July 2025 (70,515 miles): Engine oil and filter changed, spark plugs, '
                                       'ignition coils, and cabin air filter replaced\n'
                                       '  - June 2025 (68,253 miles): Key programmed\n'
                                       'The attachedCarfaxhistory report shows that the following services have been '
                                       'performed:\n'
                                       '  - October 2023 (63,513 miles): Air filter replaced, engine oil and filter '
                                       'changed\n'
                                       '  - August 2022 (57,211 miles): Front wiper blades/refills replaced, fuel '
                                       'injection system and fuel system cleaned/serviced, engine oil and filter '
                                       'changed\n'
                                       'Additional service history is detailed in the attachedCarfaxhistory report.'},
                           {'title': 'OTHER ITEMS INCLUDED IN SALE',
                            'content': '- 2 keys\n'
                                       '  - Service records\n'
                                       '  - Full Race Motorsports transmission oil cooler\n'
                                       '  - COBB Tuning Accessport V3'},
                           {'title': 'OWNERSHIP HISTORY',
                            'content': 'The seller reports that they purchased this Raptor in May 2025 and have added '
                                       'approximately 14,000 miles since.'},
                           {'title': 'SELLER NOTES',
                            'content': 'There is a loan on this vehicle, and sale proceeds will be used to satisfy the '
                                       'loan. We recommend handling the loan payoff securely throughCars & Bids '
                                       'SafePayif agreed to by both the buyer and the seller. Please note that the '
                                       'title may only be availableafterthe loan has been paid off.'}],
              'raw_description': 'HIGHLIGHTS\n'
                                 '\n'
                                 'THIS... is a 2018 Ford F-150 Raptor, finished in Lightning Blue with a black '
                                 'interior.\n'
                                 '  - The attachedCarfaxvehicle history report shows no accidents or mileage '
                                 'discrepancies in this Raptor’s past.\n'
                                 '  - According to the digital window sticker provided in the gallery, notable factory '
                                 'equipment includes Equipment Group 800A, running boards, cloth upholstery, and a '
                                 'rearview camera.\n'
                                 '  - Notable modifications reported by the seller include 17-inch Gen-3 Raptor '
                                 'wheels, a Goosetuned TCM tune, aftermarket fog lights, a LINE-X spray-on bedliner, '
                                 'and a folding bed cover.\n'
                                 '  - Designed to speed across the desert, Baja racing-style, the second-generation '
                                 'F-150 Raptor made its debut for the 2017 model year with an impressive list of '
                                 'off-road hardware and more horsepower from a downsized, twin-turbocharged V6 engine. '
                                 'It weighed about 500 pounds less than its predecessor, thanks in part to the '
                                 'widespread use of aluminum. Production ended in 2020.\n'
                                 '  - Power comes from a 3.5-liter twin-turbocharged V6, rated at 450 horsepower and '
                                 '510 lb-ft of torque. Output is sent to the rear or all four wheels via a 10-speed '
                                 'automatic transmission and a 2-speed transfer case.\n'
                                 '\n'
                                 'EQUIPMENT\n'
                                 '\n'
                                 'A digital window sticker is provided in the photo gallery, and a partial list of '
                                 'notable equipment reported by the seller includes:\n'
                                 '  - Equipment Group 800A\n'
                                 '  - Running boards\n'
                                 '  - Cloth upholstery\n'
                                 '  - Air conditioning\n'
                                 '  - CD player\n'
                                 '  - Cruise control\n'
                                 '  - Rearview camera\n'
                                 '\n'
                                 'MODIFICATIONS\n'
                                 '\n'
                                 'Notable modifications reported by the seller include:\n'
                                 '  - 17-inch Gen-3 Raptor wheels\n'
                                 '  - Goosetuned TCM tune\n'
                                 '  - Aftermarket fog lights\n'
                                 '  - LINE-X spray-on bedliner\n'
                                 '  - Folding bed cover\n'
                                 '\n'
                                 'KNOWN FLAWS\n'
                                 '\n'
                                 '  - Chips on front-end components; some scratches on plastic fender flares\n'
                                 '  - Scratches on glove box lid\n'
                                 '\n'
                                 'RECENT SERVICE HISTORY\n'
                                 '\n'
                                 'Service documentation in the photo gallery indicates that the following maintenance '
                                 'has been performed:\n'
                                 '  - March 2026: Engine oil and filter changed, ignition coils replaced\n'
                                 '  - December 2025 (75,192 miles): Fuel induction service performed\n'
                                 '  - October 2025 (73,709 miles): VCT camshaft phasers, camshaft sprockets, valve '
                                 'cover bolts, and water pump gasket replaced\n'
                                 '  - July 2025 (70,515 miles): Engine oil and filter changed, spark plugs, ignition '
                                 'coils, and cabin air filter replaced\n'
                                 '  - June 2025 (68,253 miles): Key programmed\n'
                                 'The attachedCarfaxhistory report shows that the following services have been '
                                 'performed:\n'
                                 '  - October 2023 (63,513 miles): Air filter replaced, engine oil and filter changed\n'
                                 '  - August 2022 (57,211 miles): Front wiper blades/refills replaced, fuel injection '
                                 'system and fuel system cleaned/serviced, engine oil and filter changed\n'
                                 'Additional service history is detailed in the attachedCarfaxhistory report.\n'
                                 '\n'
                                 'OTHER ITEMS INCLUDED IN SALE\n'
                                 '\n'
                                 '  - 2 keys\n'
                                 '  - Service records\n'
                                 '  - Full Race Motorsports transmission oil cooler\n'
                                 '  - COBB Tuning Accessport V3\n'
                                 '\n'
                                 'OWNERSHIP HISTORY\n'
                                 '\n'
                                 'The seller reports that they purchased this Raptor in May 2025 and have added '
                                 'approximately 14,000 miles since.\n'
                                 '\n'
                                 'SELLER NOTES\n'
                                 '\n'
                                 'There is a loan on this vehicle, and sale proceeds will be used to satisfy the loan. '
                                 'We recommend handling the loan payoff securely throughCars & Bids SafePayif agreed '
                                 'to by both the buyer and the seller. Please note that the title may only be '
                                 'availableafterthe loan has been paid off.'},
  'featured': False,
  'financing_available': True,
  'warranty_available': True,
  'delivery_available': True},
 {'id': '2024-ford-f-150-raptor-r',
  'slug': '2024-ford-f-150-raptor-r',
  'title': '2024 Ford F-150 Raptor R',
  'make': 'Ford',
  'model': 'F-150',
  'trim': 'Raptor R',
  'year': 2024,
  'status': 'Available',
  'stock_number': 'RUC38480',
  'vin': '1FTFW1RJ9RFB38480',
  'price': 80999,
  'mileage': 21400,
  'body_type': 'Truck',
  'transmission': 'Automatic (10-Speed)',
  'drivetrain': '4WD/AWD',
  'engine': '5.2L Supercharged V8',
  'exterior_color': 'Agate Black Metallic',
  'interior_color': 'Black',
  'location': 'Commodore, PA',
  'short_description': '2024 Ford F-150 Raptor R finished in Agate Black Metallic with a Black interior, 21,400 miles, '
                       'and 5.2L Supercharged V8.',
  'description': 'THIS... is a 2024 Ford F-150 Raptor R, finished in Agate Black Metallic with a black interior.',
  'images': ['/media/vehicles/2024-ford-f-150-raptor-r/01.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/02.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/03.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/04.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/05.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/06.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/07.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/08.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/09.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/10.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/11.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/12.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/13.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/14.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/15.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/16.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/17.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/18.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/19.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/20.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/21.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/22.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/23.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/24.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/25.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/26.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/27.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/28.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/29.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/30.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/31.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/32.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/33.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/34.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/35.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/36.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/37.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/38.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/39.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/40.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/41.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/42.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/43.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/44.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/45.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/46.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/47.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/48.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/49.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/50.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/51.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/52.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/53.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/54.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/55.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/56.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/57.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/58.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/59.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/60.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/61.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/62.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/63.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/64.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/65.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/66.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/67.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/68.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/69.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/70.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/71.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/72.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/73.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/74.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/75.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/76.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/77.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/78.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/79.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/80.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/81.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/82.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/83.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/84.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/85.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/86.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/87.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/88.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/89.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/90.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/91.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/92.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/93.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/94.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/95.jpg',
             '/media/vehicles/2024-ford-f-150-raptor-r/96.png',
             '/media/vehicles/2024-ford-f-150-raptor-r/97.png',
             '/media/vehicles/2024-ford-f-150-raptor-r/98.png',
             '/media/vehicles/2024-ford-f-150-raptor-r/99.png'],
  'features': ['17-inch beadlock-capable wheels',
               'Electronic locking rear axle',
               'FOX Live Valve shocks',
               'R-specific body kit',
               'Twin-panel sunroof'],
  'specs': {},
  'details': {'info': [{'label': 'Title', 'value': '2024 Ford F-150 Raptor R'},
                       {'label': 'Make', 'value': 'Ford'},
                       {'label': 'Engine', 'value': '5.2L Supercharged V8'},
                       {'label': 'Model', 'value': 'F-150 RaptorSave'},
                       {'label': 'Drivetrain', 'value': '4WD/AWD'},
                       {'label': 'Mileage', 'value': '21,400'},
                       {'label': 'Transmission', 'value': 'Automatic (10-Speed)'},
                       {'label': 'VIN', 'value': '1FTFW1RJ9RFB38480'},
                       {'label': 'Body Style', 'value': 'Truck'},
                       {'label': 'Title Status', 'value': 'Clean (GA)'},
                       {'label': 'Exterior Color', 'value': 'Agate Black Metallic'},
                       {'label': 'Location', 'value': 'Woodstock, GA 30189'},
                       {'label': 'Interior Color', 'value': 'Black'},
                       {'label': 'Seller', 'value': 'jackwilliams52'},
                       {'label': 'Seller Type', 'value': 'Private Party'}],
              'sections': [{'title': 'HIGHLIGHTS',
                            'content': 'THIS... is a 2024 Ford F-150 Raptor R, finished in Agate Black Metallic with a '
                                       'black interior.\n'
                                       '  - The attachedCarfaxvehicle history report indicates no accidents or mileage '
                                       'discrepancies in this Raptor’s past.\n'
                                       '  - According to the window sticker provided in the gallery, this Raptor is an '
                                       'R model, and notable factory equipment includes 17-inch wheels, an electronic '
                                       'locking rear axle, and FOX Live Valve shocks. The seller reports no notable '
                                       'modifications.\n'
                                       '  - Ford seriously upped their performance truck game with the introduction of '
                                       'the F-150 Raptor R. Although the truck shares many design cues with the '
                                       'standard, V6-powered F-150 Raptor, loud exterior badging and an oversized hood '
                                       'vent ensure that nobody mistakes it for anything other than an "R". The Raptor '
                                       "R's monstrous supercharged V8 gives it supercar-rivaling acceleration to "
                                       'complement its go-anywhere off-road ability.\n'
                                       '  - Power comes from a 5.2-liter supercharged V8, rated at 720 horsepower and '
                                       '640 lb-ft of torque. Output is sent to the rear or all four wheels via a '
                                       '10-speed automatic transmission and a 2-speed transfer case.'},
                           {'title': 'EQUIPMENT',
                            'content': 'This Raptor is an R model. A window sticker is provided in the photo gallery, '
                                       'and a partial list of notable equipment reported by the seller includes:\n'
                                       '  - 17-inch beadlock-capable wheels\n'
                                       '  - Electronic locking rear axle\n'
                                       '  - FOX Live Valve shocks\n'
                                       '  - R-specific body kit\n'
                                       '  - Twin-panel sunroof\n'
                                       '  - Heated, ventilated, and power-adjustable Recaro front seats\n'
                                       '  - Heated steering wheel'},
                           {'title': 'KNOWN FLAWS',
                            'content': '- Some chips on front end\n  - Some scratches around exterior'},
                           {'title': 'RECENT SERVICE HISTORY',
                            'content': 'The attachedCarfaxhistory report shows that the following services have been '
                                       'performed:\n'
                                       '  - November 2025 (17,315 miles): Engine oil and filter changed, tires '
                                       'rotated\n'
                                       '  - August 2025 (12,419 miles): Engine oil and filter changed, tires rotated\n'
                                       '  - June 2025 (8,815 miles): Engine oil and filter changed, tires rotated\n'
                                       '  - February 2025 (4,209 miles): Engine oil and filter changed, tires rotated'},
                           {'title': 'OTHER ITEMS INCLUDED IN SALE',
                            'content': '- 2 key fobs\n  - All-weather floor mats\n  - Spare tire'},
                           {'title': 'OWNERSHIP HISTORY',
                            'content': 'This Raptor R is titled to the seller’s business. The seller reports that they '
                                       'purchased this truck in March 2026 and have added approximately 2,400 miles '
                                       'since.'},
                           {'title': 'SELLER NOTES',
                            'content': '- There is a loan on this vehicle, and sale proceeds will be used to satisfy '
                                       'the loan. We recommend handling the loan payoff securely throughCars & Bids '
                                       'SafePayif agreed to by both the buyer and the seller. Please note that the '
                                       'title may only be availableafterthe loan has been paid off.\n'
                                       '  - This Raptor R is offered with a transferable warranty valid until March '
                                       '2032 or 150,000 miles. Documentation regarding the service contract is '
                                       'pictured in the photo gallery.\n'
                                       '  - The seller reports that the windows of this Ford have been ceramic '
                                       'tinted.'}],
              'raw_description': 'HIGHLIGHTS\n'
                                 '\n'
                                 'THIS... is a 2024 Ford F-150 Raptor R, finished in Agate Black Metallic with a black '
                                 'interior.\n'
                                 '  - The attachedCarfaxvehicle history report indicates no accidents or mileage '
                                 'discrepancies in this Raptor’s past.\n'
                                 '  - According to the window sticker provided in the gallery, this Raptor is an R '
                                 'model, and notable factory equipment includes 17-inch wheels, an electronic locking '
                                 'rear axle, and FOX Live Valve shocks. The seller reports no notable modifications.\n'
                                 '  - Ford seriously upped their performance truck game with the introduction of the '
                                 'F-150 Raptor R. Although the truck shares many design cues with the standard, '
                                 'V6-powered F-150 Raptor, loud exterior badging and an oversized hood vent ensure '
                                 'that nobody mistakes it for anything other than an "R". The Raptor R\'s monstrous '
                                 'supercharged V8 gives it supercar-rivaling acceleration to complement its '
                                 'go-anywhere off-road ability.\n'
                                 '  - Power comes from a 5.2-liter supercharged V8, rated at 720 horsepower and 640 '
                                 'lb-ft of torque. Output is sent to the rear or all four wheels via a 10-speed '
                                 'automatic transmission and a 2-speed transfer case.\n'
                                 '\n'
                                 'EQUIPMENT\n'
                                 '\n'
                                 'This Raptor is an R model. A window sticker is provided in the photo gallery, and a '
                                 'partial list of notable equipment reported by the seller includes:\n'
                                 '  - 17-inch beadlock-capable wheels\n'
                                 '  - Electronic locking rear axle\n'
                                 '  - FOX Live Valve shocks\n'
                                 '  - R-specific body kit\n'
                                 '  - Twin-panel sunroof\n'
                                 '  - Heated, ventilated, and power-adjustable Recaro front seats\n'
                                 '  - Heated steering wheel\n'
                                 '\n'
                                 'KNOWN FLAWS\n'
                                 '\n'
                                 '  - Some chips on front end\n'
                                 '  - Some scratches around exterior\n'
                                 '\n'
                                 'RECENT SERVICE HISTORY\n'
                                 '\n'
                                 'The attachedCarfaxhistory report shows that the following services have been '
                                 'performed:\n'
                                 '  - November 2025 (17,315 miles): Engine oil and filter changed, tires rotated\n'
                                 '  - August 2025 (12,419 miles): Engine oil and filter changed, tires rotated\n'
                                 '  - June 2025 (8,815 miles): Engine oil and filter changed, tires rotated\n'
                                 '  - February 2025 (4,209 miles): Engine oil and filter changed, tires rotated\n'
                                 '\n'
                                 'OTHER ITEMS INCLUDED IN SALE\n'
                                 '\n'
                                 '  - 2 key fobs\n'
                                 '  - All-weather floor mats\n'
                                 '  - Spare tire\n'
                                 '\n'
                                 'OWNERSHIP HISTORY\n'
                                 '\n'
                                 'This Raptor R is titled to the seller’s business. The seller reports that they '
                                 'purchased this truck in March 2026 and have added approximately 2,400 miles since.\n'
                                 '\n'
                                 'SELLER NOTES\n'
                                 '\n'
                                 '  - There is a loan on this vehicle, and sale proceeds will be used to satisfy the '
                                 'loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif '
                                 'agreed to by both the buyer and the seller. Please note that the title may only be '
                                 'availableafterthe loan has been paid off.\n'
                                 '  - This Raptor R is offered with a transferable warranty valid until March 2032 or '
                                 '150,000 miles. Documentation regarding the service contract is pictured in the photo '
                                 'gallery.\n'
                                 '  - The seller reports that the windows of this Ford have been ceramic tinted.'},
  'featured': True,
  'financing_available': True,
  'warranty_available': True,
  'delivery_available': True},
 {'id': '2025-ford-f-150-raptor-r',
  'slug': '2025-ford-f-150-raptor-r',
  'title': '2025 Ford F-150 Raptor R',
  'make': 'Ford',
  'model': 'F-150',
  'trim': 'Raptor R',
  'year': 2025,
  'status': 'Available',
  'stock_number': 'RUC93369',
  'vin': '1FTFW1RJ9SFB93369',
  'price': 94999,
  'mileage': 200,
  'body_type': 'Truck',
  'transmission': 'Automatic (10-Speed)',
  'drivetrain': '4WD/AWD',
  'engine': '5.2L Supercharged V8',
  'exterior_color': 'Carbonized Gray Metallic',
  'interior_color': 'Black',
  'location': 'Commodore, PA',
  'short_description': '2025 Ford F-150 Raptor R finished in Carbonized Gray Metallic with a Black interior, 200 '
                       'miles, and 5.2L Supercharged V8.',
  'description': 'THIS... is a 2025 Ford F-150 Raptor R, finished in Carbonized Gray Metallic with a black interior.',
  'images': ['/media/vehicles/2025-ford-f-150-raptor-r/01.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/02.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/03.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/04.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/05.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/06.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/07.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/08.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/09.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/10.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/11.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/12.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/13.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/14.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/15.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/16.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/17.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/18.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/19.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/20.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/21.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/22.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/23.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/24.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/25.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/26.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/27.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/28.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/29.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/30.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/31.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/32.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/33.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/34.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/35.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/36.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/37.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/38.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/39.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/40.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/41.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/42.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/43.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/44.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/45.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/46.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/47.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/48.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/49.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/50.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/51.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/52.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/53.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/54.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/55.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/56.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/57.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/58.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/59.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/60.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/61.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/62.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/63.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/64.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/65.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/66.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/67.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/68.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/69.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/70.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/71.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/72.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/73.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/74.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/75.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/76.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/77.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/78.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/79.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/80.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/81.jpg',
             '/media/vehicles/2025-ford-f-150-raptor-r/82.png',
             '/media/vehicles/2025-ford-f-150-raptor-r/83.png',
             '/media/vehicles/2025-ford-f-150-raptor-r/84.png'],
  'features': ['Code Orange-painted wheel trim (dealer-installed)',
               'Dual exhaust system',
               'Heated, ventilated, and power-adjustable Recaro front seats',
               'Heated rear seats',
               'Bang & Olufsen sound system'],
  'specs': {},
  'details': {'info': [{'label': 'Title', 'value': '2025 Ford F-150 Raptor R'},
                       {'label': 'Make', 'value': 'Ford'},
                       {'label': 'Engine', 'value': '5.2L Supercharged V8'},
                       {'label': 'Model', 'value': 'F-150 RaptorSave'},
                       {'label': 'Drivetrain', 'value': '4WD/AWD'},
                       {'label': 'Mileage', 'value': '200'},
                       {'label': 'Transmission', 'value': 'Automatic (10-Speed)'},
                       {'label': 'VIN', 'value': '1FTFW1RJ9SFB93369'},
                       {'label': 'Body Style', 'value': 'Truck'},
                       {'label': 'Title Status', 'value': 'Clean (MT)'},
                       {'label': 'Exterior Color', 'value': 'Carbonized Gray Metallic'},
                       {'label': 'Location', 'value': 'Naples, FL 34102'},
                       {'label': 'Interior Color', 'value': 'Black'},
                       {'label': 'Seller', 'value': 'TruckKingUSA'},
                       {'label': 'Seller Type', 'value': 'Private Party'}],
              'sections': [{'title': 'HIGHLIGHTS',
                            'content': 'THIS... is a 2025 Ford F-150 Raptor R, finished in Carbonized Gray Metallic '
                                       'with a black interior.\n'
                                       '  - The odometer on this F-150 Raptor R currently displays approximately 200 '
                                       'miles.\n'
                                       '  - The attachedCarfaxhistory report indicates no accidents or mileage '
                                       "discrepancies in this Raptor's brief past.\n"
                                       '  - According to the window sticker provided in the gallery, notable factory '
                                       'equipment includes Equipment Group 803A, a dual exhaust system, heated and '
                                       'ventilated Recaro front seats, heated rear seats, and a Bang & Olufsen sound '
                                       'system. The seller reports no notable modifications.\n'
                                       '  - The F-150 Raptor R was introduced as the most powerful variant of the '
                                       'F-150 Raptor lineup, offering upgraded off-road capability and '
                                       'high-performance features. It is distinguished by its supercharged V8 engine, '
                                       'advanced suspension systems, and a suite of features designed for both on-road '
                                       'comfort and off-road prowess. Since its debut, the Raptor R has attracted '
                                       'enthusiasts looking for a high-performance truck with factory-backed '
                                       'ruggedness and capability.\n'
                                       '  - Power comes from a supercharged 5.2-liter V8, rated at 720 horsepower and '
                                       '640 lb-ft of torque. Output is sent to the rear or all four wheels via a '
                                       '10-speed automatic transmission and a 2-speed transfer case.'},
                           {'title': 'EQUIPMENT',
                            'content': 'A window sticker is provided in the photo gallery, and a partial list of '
                                       'notable equipment reported by the seller includes:\n'
                                       '  - Equipment Group 803A (Raptor series, 17-inch forged aluminum '
                                       'beadlock-capable wheels, dual-valve shocks)\n'
                                       '  - Code Orange-painted wheel trim (dealer-installed)\n'
                                       '  - Dual exhaust system\n'
                                       '  - Heated, ventilated, and power-adjustable Recaro front seats\n'
                                       '  - Heated rear seats\n'
                                       '  - Bang & Olufsen sound system'},
                           {'title': 'RECENT SERVICE HISTORY',
                            'content': 'The seller states that this Ford has not required service due to its low '
                                       'mileage.'},
                           {'title': 'OTHER ITEMS INCLUDED IN SALE',
                            'content': "- 2 keys\n  - Owner's manual\n  - Window sticker\n  - Set of gray wheel trim"},
                           {'title': 'OWNERSHIP HISTORY',
                            'content': 'This Raptor R is titled to the seller’s LLC. The seller reports that they '
                                       'purchased this truck new in November 2025.'}],
              'raw_description': 'HIGHLIGHTS\n'
                                 '\n'
                                 'THIS... is a 2025 Ford F-150 Raptor R, finished in Carbonized Gray Metallic with a '
                                 'black interior.\n'
                                 '  - The odometer on this F-150 Raptor R currently displays approximately 200 miles.\n'
                                 '  - The attachedCarfaxhistory report indicates no accidents or mileage discrepancies '
                                 "in this Raptor's brief past.\n"
                                 '  - According to the window sticker provided in the gallery, notable factory '
                                 'equipment includes Equipment Group 803A, a dual exhaust system, heated and '
                                 'ventilated Recaro front seats, heated rear seats, and a Bang & Olufsen sound system. '
                                 'The seller reports no notable modifications.\n'
                                 '  - The F-150 Raptor R was introduced as the most powerful variant of the F-150 '
                                 'Raptor lineup, offering upgraded off-road capability and high-performance features. '
                                 'It is distinguished by its supercharged V8 engine, advanced suspension systems, and '
                                 'a suite of features designed for both on-road comfort and off-road prowess. Since '
                                 'its debut, the Raptor R has attracted enthusiasts looking for a high-performance '
                                 'truck with factory-backed ruggedness and capability.\n'
                                 '  - Power comes from a supercharged 5.2-liter V8, rated at 720 horsepower and 640 '
                                 'lb-ft of torque. Output is sent to the rear or all four wheels via a 10-speed '
                                 'automatic transmission and a 2-speed transfer case.\n'
                                 '\n'
                                 'EQUIPMENT\n'
                                 '\n'
                                 'A window sticker is provided in the photo gallery, and a partial list of notable '
                                 'equipment reported by the seller includes:\n'
                                 '  - Equipment Group 803A (Raptor series, 17-inch forged aluminum beadlock-capable '
                                 'wheels, dual-valve shocks)\n'
                                 '  - Code Orange-painted wheel trim (dealer-installed)\n'
                                 '  - Dual exhaust system\n'
                                 '  - Heated, ventilated, and power-adjustable Recaro front seats\n'
                                 '  - Heated rear seats\n'
                                 '  - Bang & Olufsen sound system\n'
                                 '\n'
                                 'RECENT SERVICE HISTORY\n'
                                 '\n'
                                 'The seller states that this Ford has not required service due to its low mileage.\n'
                                 '\n'
                                 'OTHER ITEMS INCLUDED IN SALE\n'
                                 '\n'
                                 '  - 2 keys\n'
                                 "  - Owner's manual\n"
                                 '  - Window sticker\n'
                                 '  - Set of gray wheel trim\n'
                                 '\n'
                                 'OWNERSHIP HISTORY\n'
                                 '\n'
                                 'This Raptor R is titled to the seller’s LLC. The seller reports that they purchased '
                                 'this truck new in November 2025.'},
  'featured': True,
  'financing_available': True,
  'warranty_available': True,
  'delivery_available': True},
 {'id': '2024-ford-f-450-super-duty-limited-4x4',
  'slug': '2024-ford-f-450-super-duty-limited-4x4',
  'title': '2024 Ford F-450 Super Duty Limited 4x4',
  'make': 'Ford',
  'model': 'F-450 Super Duty',
  'trim': 'Limited 4x4',
  'year': 2024,
  'status': 'Available',
  'stock_number': 'RUC94419',
  'vin': '1FT8W4DM1RED94419',
  'price': 59999,
  'mileage': 18300,
  'body_type': 'Truck',
  'transmission': 'Automatic (10-Speed)',
  'drivetrain': '4WD/AWD',
  'engine': '6.7L Turbodiesel V8',
  'exterior_color': 'Agate Black',
  'interior_color': 'Admiral Blue/Light Slate',
  'location': 'Commodore, PA',
  'short_description': '2024 Ford F-450 Super Duty Limited 4x4 finished in Agate Black with a Admiral Blue/Light Slate '
                       'interior, 18,300 miles, and 6.7L Turbodiesel V8.',
  'description': 'The current Ford F-450 Super Duty is a fantastic truck with incredible capabilities, great '
                 'technology, and – in this case – a Power Stroke turbodiesel V8 with an impressive 1,200 lb-ft of '
                 "torque. This F-450 is also a desirable Limited model that's equipped with 4-wheel drive and dual "
                 'rear wheels – and it boasts some neat upgrades including 24-inch American Force Wheels with 35-inch '
                 'all-terrain tires, an aftermarket leveling kit, a LEER truck cap, and a CargoGlide bed slide-out '
                 'tray. On top of all that, this F-450 comes with a clean, accident-free Carfax report, further adding '
                 'to the appeal.',
  'images': ['/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/01.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/02.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/03.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/04.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/05.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/06.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/07.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/08.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/09.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/10.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/11.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/12.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/13.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/14.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/15.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/16.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/17.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/18.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/19.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/20.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/21.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/22.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/23.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/24.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/25.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/26.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/27.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/28.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/29.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/30.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/31.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/32.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/33.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/34.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/35.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/36.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/37.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/38.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/39.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/40.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/41.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/42.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/43.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/44.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/45.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/46.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/47.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/48.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/49.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/50.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/51.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/52.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/53.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/54.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/55.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/56.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/57.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/58.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/59.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/60.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/61.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/62.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/63.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/64.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/65.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/66.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/67.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/68.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/69.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/70.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/71.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/72.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/73.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/74.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/75.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/76.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/77.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/78.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/79.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/80.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/81.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/82.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/83.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/84.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/85.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/86.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/87.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/88.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/89.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/90.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/91.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/92.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/93.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/94.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/95.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/96.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/97.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/98.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/99.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/100.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/101.jpg',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/102.png',
             '/media/vehicles/2024-ford-f-450-super-duty-limited-4x4/103.png'],
  'features': ['FX4 Off-Road Package (skid plates, 14,000-pound GVWR package)',
               'Rapid heat supplemental heater',
               'Power deployable running boards',
               'Tough Bed spray in bedliner',
               'Power twin-panel sunroof'],
  'specs': {},
  'details': {'info': [{'label': 'Title', 'value': '2024 Ford F-450 Super Duty Limited 4x4'},
                       {'label': 'Make', 'value': 'Ford'},
                       {'label': 'Engine', 'value': '6.7L Turbodiesel V8'},
                       {'label': 'Model', 'value': 'Super DutySave'},
                       {'label': 'Drivetrain', 'value': '4WD/AWD'},
                       {'label': 'Mileage', 'value': '18,300'},
                       {'label': 'Transmission', 'value': 'Automatic (10-Speed)'},
                       {'label': 'VIN', 'value': '1FT8W4DM1RED94419'},
                       {'label': 'Body Style', 'value': 'Truck'},
                       {'label': 'Title Status', 'value': 'Clean (WY)'},
                       {'label': 'Exterior Color', 'value': 'Agate Black'},
                       {'label': 'Location', 'value': 'Chesterfield, MO 63017'},
                       {'label': 'Interior Color', 'value': 'Admiral Blue/Light Slate'},
                       {'label': 'Seller', 'value': 'hunco'},
                       {'label': 'Seller Type', 'value': 'Private Party'}],
              'sections': [{'title': "DOUG'S TAKE",
                            'content': 'The current Ford F-450 Super Duty is a fantastic truck with incredible '
                                       'capabilities, great technology, and – in this case – a Power Stroke '
                                       'turbodiesel V8 with an impressive 1,200 lb-ft of torque. This F-450 is also a '
                                       "desirable Limited model that's equipped with 4-wheel drive and dual rear "
                                       'wheels – and it boasts some neat upgrades including 24-inch American Force '
                                       'Wheels with 35-inch all-terrain tires, an aftermarket leveling kit, a LEER '
                                       'truck cap, and a CargoGlide bed slide-out tray. On top of all that, this F-450 '
                                       'comes with a clean, accident-free Carfax report, further adding to the '
                                       'appeal.'},
                           {'title': 'HIGHLIGHTS',
                            'content': 'THIS... is a 2024 Ford F-450 Super Duty Limited 4x4, finished in Agate Black '
                                       'with an Admiral Blue and Light Slate interior.\n'
                                       '  - The attached Carfax vehicle history report shows no accidents or mileage '
                                       'discrepancies in this F-450’s past.\n'
                                       '  - According to the digital window sticker provided in the gallery, this '
                                       'F-450 is a Limited model, and notable factory equipment includes the FX4 '
                                       'Off-Road Package, Tough Bed spray-in bedliner, a power twin-panel sunroof, and '
                                       'a Bang & Olufsen sound system.\n'
                                       '  - Notable modifications reported by the seller include 24-inch American '
                                       'Force Wheels, 35-inch Nitto Recon Grappler A/T tires, an aftermarket leveling '
                                       'kit, a LEER truck cap, and a CargoGlide CG1000 truck bed slide-out tray.\n'
                                       "  - The F-450 Super Duty Limited represents Ford's top-tier offering in the "
                                       'heavy-duty pickup segment for the 2024 model year. Known for its combination '
                                       'of luxury features and exceptional towing capability, the F-450 is designed to '
                                       'meet the demands of both personal and commercial users. This generation '
                                       'continues to appeal to buyers seeking advanced technology and robust '
                                       'performance in a versatile truck platform.\n'
                                       '  - Power comes from a high-output 6.7-liter Power Stroke turbodiesel V8, '
                                       'rated at 500 horsepower and 1,200 lb-ft of torque. Output is sent to the rear '
                                       'or all four wheels via a 10-speed automatic transmission and a 2-speed '
                                       'transfer case.'},
                           {'title': 'EQUIPMENT',
                            'content': 'This F-450 is a Limited model. A digital window sticker is provided in the '
                                       'photo gallery, and a partial list of notable equipment reported by the seller '
                                       'includes:\n'
                                       '  - FX4 Off-Road Package (skid plates, 14,000-pound GVWR package)\n'
                                       '  - Rapid heat supplemental heater\n'
                                       '  - Power deployable running boards\n'
                                       '  - Tough Bed spray in bedliner\n'
                                       '  - Power twin-panel sunroof\n'
                                       '  - Heated and ventilated multi-contour front seats\n'
                                       '  - Bang & Olufsen sound system'},
                           {'title': 'MODIFICATIONS',
                            'content': 'Notable modifications reported by the seller include:\n'
                                       '  - 24-inch American Force Wheels\n'
                                       '  - 35-inch Nitto Recon Grappler A/T tires\n'
                                       '  - Aftermarket levelling kit\n'
                                       '  - LEER truck cap\n'
                                       '  - CargoGlide CG1000 truck bed slide-out tray'},
                           {'title': 'KNOWN FLAWS',
                            'content': '- Scratch on passenger-side rear wheel well\n'
                                       "  - Creases on driver's seat bolster"},
                           {'title': 'RECENT SERVICE HISTORY',
                            'content': 'Service documentation in the photo gallery indicates that the following '
                                       'maintenance has been performed:\n'
                                       '  - September 2025 (15,456 miles): Engine oil and filter changed\n'
                                       '  - May 2025 (8,360 miles): Engine oil and filter changed\n'
                                       'The attached Carfax history report shows that the following services have been '
                                       'performed:\n'
                                       '  - July 2025 (11,095 miles): Computer reprogrammed'},
                           {'title': 'OTHER ITEMS INCLUDED IN SALE', 'content': "- 2 keys\n  - Owner's manual"},
                           {'title': 'OWNERSHIP HISTORY',
                            'content': 'The seller reports that they purchased this F-450 in February 2025.'},
                           {'title': 'SELLER NOTES',
                            'content': '- There is a loan on this vehicle, and sale proceeds will be used to satisfy '
                                       'the loan. We recommend handling the loan payoff securely throughCars & Bids '
                                       'SafePayif agreed to by both the buyer and the seller. Please note that the '
                                       'title may only be availableafterthe loan has been paid off.\n'
                                       '  - The seller reports that the windows have been tinted and that paint '
                                       'protection film has been applied to the front bumper, hood, and lower side '
                                       'panels of this F-450.'}],
              'raw_description': "DOUG'S TAKE\n"
                                 '\n'
                                 'The current Ford F-450 Super Duty is a fantastic truck with incredible capabilities, '
                                 'great technology, and – in this case – a Power Stroke turbodiesel V8 with an '
                                 'impressive 1,200 lb-ft of torque. This F-450 is also a desirable Limited model '
                                 "that's equipped with 4-wheel drive and dual rear wheels – and it boasts some neat "
                                 'upgrades including 24-inch American Force Wheels with 35-inch all-terrain tires, an '
                                 'aftermarket leveling kit, a LEER truck cap, and a CargoGlide bed slide-out tray. On '
                                 'top of all that, this F-450 comes with a clean, accident-free Carfax report, further '
                                 'adding to the appeal.\n'
                                 '\n'
                                 'HIGHLIGHTS\n'
                                 '\n'
                                 'THIS... is a 2024 Ford F-450 Super Duty Limited 4x4, finished in Agate Black with an '
                                 'Admiral Blue and Light Slate interior.\n'
                                 '  - The attached Carfax vehicle history report shows no accidents or mileage '
                                 'discrepancies in this F-450’s past.\n'
                                 '  - According to the digital window sticker provided in the gallery, this F-450 is a '
                                 'Limited model, and notable factory equipment includes the FX4 Off-Road Package, '
                                 'Tough Bed spray-in bedliner, a power twin-panel sunroof, and a Bang & Olufsen sound '
                                 'system.\n'
                                 '  - Notable modifications reported by the seller include 24-inch American Force '
                                 'Wheels, 35-inch Nitto Recon Grappler A/T tires, an aftermarket leveling kit, a LEER '
                                 'truck cap, and a CargoGlide CG1000 truck bed slide-out tray.\n'
                                 "  - The F-450 Super Duty Limited represents Ford's top-tier offering in the "
                                 'heavy-duty pickup segment for the 2024 model year. Known for its combination of '
                                 'luxury features and exceptional towing capability, the F-450 is designed to meet the '
                                 'demands of both personal and commercial users. This generation continues to appeal '
                                 'to buyers seeking advanced technology and robust performance in a versatile truck '
                                 'platform.\n'
                                 '  - Power comes from a high-output 6.7-liter Power Stroke turbodiesel V8, rated at '
                                 '500 horsepower and 1,200 lb-ft of torque. Output is sent to the rear or all four '
                                 'wheels via a 10-speed automatic transmission and a 2-speed transfer case.\n'
                                 '\n'
                                 'EQUIPMENT\n'
                                 '\n'
                                 'This F-450 is a Limited model. A digital window sticker is provided in the photo '
                                 'gallery, and a partial list of notable equipment reported by the seller includes:\n'
                                 '  - FX4 Off-Road Package (skid plates, 14,000-pound GVWR package)\n'
                                 '  - Rapid heat supplemental heater\n'
                                 '  - Power deployable running boards\n'
                                 '  - Tough Bed spray in bedliner\n'
                                 '  - Power twin-panel sunroof\n'
                                 '  - Heated and ventilated multi-contour front seats\n'
                                 '  - Bang & Olufsen sound system\n'
                                 '\n'
                                 'MODIFICATIONS\n'
                                 '\n'
                                 'Notable modifications reported by the seller include:\n'
                                 '  - 24-inch American Force Wheels\n'
                                 '  - 35-inch Nitto Recon Grappler A/T tires\n'
                                 '  - Aftermarket levelling kit\n'
                                 '  - LEER truck cap\n'
                                 '  - CargoGlide CG1000 truck bed slide-out tray\n'
                                 '\n'
                                 'KNOWN FLAWS\n'
                                 '\n'
                                 '  - Scratch on passenger-side rear wheel well\n'
                                 "  - Creases on driver's seat bolster\n"
                                 '\n'
                                 'RECENT SERVICE HISTORY\n'
                                 '\n'
                                 'Service documentation in the photo gallery indicates that the following maintenance '
                                 'has been performed:\n'
                                 '  - September 2025 (15,456 miles): Engine oil and filter changed\n'
                                 '  - May 2025 (8,360 miles): Engine oil and filter changed\n'
                                 'The attached Carfax history report shows that the following services have been '
                                 'performed:\n'
                                 '  - July 2025 (11,095 miles): Computer reprogrammed\n'
                                 '\n'
                                 'OTHER ITEMS INCLUDED IN SALE\n'
                                 '\n'
                                 '  - 2 keys\n'
                                 "  - Owner's manual\n"
                                 '\n'
                                 'OWNERSHIP HISTORY\n'
                                 '\n'
                                 'The seller reports that they purchased this F-450 in February 2025.\n'
                                 '\n'
                                 'SELLER NOTES\n'
                                 '\n'
                                 '  - There is a loan on this vehicle, and sale proceeds will be used to satisfy the '
                                 'loan. We recommend handling the loan payoff securely throughCars & Bids SafePayif '
                                 'agreed to by both the buyer and the seller. Please note that the title may only be '
                                 'availableafterthe loan has been paid off.\n'
                                 '  - The seller reports that the windows have been tinted and that paint protection '
                                 'film has been applied to the front bumper, hood, and lower side panels of this '
                                 'F-450.'},
  'featured': False,
  'financing_available': True,
  'warranty_available': True,
  'delivery_available': True},
 {'id': '2021-mercedes-amg-e63-s-sedan',
  'slug': '2021-mercedes-amg-e63-s-sedan',
  'title': '2021 Mercedes-AMG E63 S Sedan',
  'make': 'Mercedes-AMG',
  'model': 'E63 S',
  'trim': 'Sedan',
  'year': 2021,
  'status': 'Available',
  'stock_number': 'RUC40570',
  'vin': 'W1KZF8KB4MA940570',
  'price': 52999,
  'mileage': 58900,
  'body_type': 'Sedan',
  'transmission': 'Automatic (9-Speed)',
  'drivetrain': '4WD/AWD',
  'engine': '4.0L Turbocharged V8',
  'exterior_color': 'Obsidian Black Metallic',
  'interior_color': 'Titanium Gray/Black',
  'location': 'Commodore, PA',
  'short_description': '2021 Mercedes-AMG E63 S Sedan finished in Obsidian Black Metallic with a Titanium Gray/Black '
                       'interior, 58,900 miles, and 4.0L Turbocharged V8.',
  'description': 'THIS... is a 2021 Mercedes-AMG E63 S Sedan, finished in Obsidian Black Metallic with a Satin Dark '
                 'Gray exterior wrap and a Titanium Gray and black interior.',
  'images': ['/media/vehicles/2021-mercedes-amg-e63-s-sedan/01.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/02.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/03.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/04.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/05.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/06.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/07.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/08.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/09.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/10.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/11.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/12.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/13.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/14.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/15.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/16.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/17.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/18.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/19.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/20.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/21.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/22.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/23.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/24.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/25.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/26.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/27.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/28.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/29.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/30.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/31.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/32.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/33.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/34.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/35.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/36.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/37.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/38.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/39.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/40.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/41.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/42.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/43.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/44.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/45.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/46.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/47.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/48.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/49.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/50.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/51.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/52.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/53.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/54.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/55.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/56.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/57.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/58.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/59.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/60.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/61.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/62.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/63.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/64.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/65.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/66.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/67.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/68.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/69.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/70.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/71.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/72.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/73.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/74.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/75.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/76.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/77.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/78.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/79.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/80.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/81.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/82.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/83.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/84.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/85.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/86.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/87.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/88.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/89.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/90.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/91.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/92.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/93.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/94.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/95.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/96.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/97.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/98.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/99.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/100.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/101.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/102.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/103.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/104.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/105.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/106.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/107.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/108.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/109.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/110.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/111.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/112.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/113.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/114.jpg',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/115.png',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/116.png',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/117.png',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/118.png',
             '/media/vehicles/2021-mercedes-amg-e63-s-sedan/119.png'],
  'features': ['Driver Assistance Package',
               'Exterior Lighting Package',
               'AMG Night Package',
               '20-inch wheels',
               'Heated and ventilated front seats'],
  'specs': {},
  'details': {'info': [{'label': 'Title', 'value': '2021 Mercedes-AMG E63 S Sedan'},
                       {'label': 'Make', 'value': 'Mercedes-Benz'},
                       {'label': 'Engine', 'value': '4.0L Turbocharged V8'},
                       {'label': 'Model', 'value': 'W213 E-Class AMGSave'},
                       {'label': 'Drivetrain', 'value': '4WD/AWD'},
                       {'label': 'Mileage', 'value': '58,900'},
                       {'label': 'Transmission', 'value': 'Automatic (9-Speed)'},
                       {'label': 'VIN', 'value': 'W1KZF8KB4MA940570'},
                       {'label': 'Body Style', 'value': 'Sedan'},
                       {'label': 'Title Status', 'value': 'Clean (CA)'},
                       {'label': 'Exterior Color', 'value': 'Obsidian Black Metallic'},
                       {'label': 'Location', 'value': 'Los Angeles, CA 90016'},
                       {'label': 'Interior Color', 'value': 'Titanium Gray/Black'},
                       {'label': 'Seller', 'value': 'Ant0u0'},
                       {'label': 'Seller Type', 'value': 'Private Party'}],
              'sections': [{'title': 'HIGHLIGHTS',
                            'content': 'THIS... is a 2021 Mercedes-AMG E63 S Sedan, finished in Obsidian Black '
                                       'Metallic with a Satin Dark Gray exterior wrap and a Titanium Gray and black '
                                       'interior.\n'
                                       '  - The attachedCarfaxhistory report shows that this E63 has been '
                                       'California-owned since new.\n'
                                       '  - Notable modifications reported by the seller include a DME Tuning Stage 1 '
                                       'tune, CTS Turbo cat-less downpipes, and a Valvetronic Designs electronic '
                                       'exhaust valve control kit. The factory downpipes are reportedly included in '
                                       'the sale.\n'
                                       '  - A window sticker is provided in the gallery, and a partial list of notable '
                                       'equipment reported by the seller includes the Driver Assistance and AMG Night '
                                       'packages, heated and ventilated front seats, heated rear seats, and a '
                                       'Burmester surround sound system.\n'
                                       '  - Released for 2018, the W213-based E63 arrived with a more fluid exterior '
                                       'design, a smaller yet more powerful engine, and an even longer list of '
                                       'standard features than its predecessor. Mercedes-AMG offered two variants: the '
                                       'base E63 and the pricier S model, which received upgrades like a more powerful '
                                       'engine and a drift mode.\n'
                                       '  - Power comes from a 4.0-liter twin-turbocharged V8, rated at 603 horsepower '
                                       'and 627 lb-ft of torque in stock form. The seller states that the '
                                       'modifications increase horsepower to 750, but a dyno sheet was not provided to '
                                       'confirm. Output is sent to all four wheels via a 9-speed automatic '
                                       'transmission.'},
                           {'title': 'EQUIPMENT',
                            'content': 'A window sticker is provided in the gallery, and a partial list of notable '
                                       'equipment reported by the seller includes:\n'
                                       '  - Driver Assistance Package\n'
                                       '  - Exterior Lighting Package\n'
                                       '  - AMG Night Package\n'
                                       '  - 20-inch wheels\n'
                                       '  - Heated and ventilated front seats\n'
                                       '  - Heated rear seats\n'
                                       '  - Carbon fiber interior trim\n'
                                       '  - Burmester surround sound system\n'
                                       '  - Head-up display\n'
                                       '  - Dashcam'},
                           {'title': 'MODIFICATIONS',
                            'content': 'Notable modifications reported by the seller include:\n'
                                       '  - DME Tuning Stage 1 tune\n'
                                       '  - CTS Turbo cat-less downpipes\n'
                                       '  - Valvetronic Designs electronic exhaust valve control kit\n'
                                       '  - RennTech EVM exhaust module\n'
                                       '  - Lowering module\n'
                                       '  - Avery Dennison Satin Dark Gray exterior wrap'},
                           {'title': 'KNOWN FLAWS',
                            'content': '- The attachedCarfaxhistory report notes that this E63 sustained "minor '
                                       'damage" in April 2023. It adds that "minor damage" is usually cosmetic, like '
                                       'dents and scratches on the body.\n'
                                       '  - Some exterior scratches (shown in the gallery)\n'
                                       '  - Some scratches on the driver-side front wheel\n'
                                       "  - Some wear on the driver's seat's outer bolsters"},
                           {'title': 'RECENT SERVICE HISTORY',
                            'content': 'Service documentation in the gallery indicates that the following maintenance '
                                       'has been performed:\n'
                                       '  - January 2026 (52,905 miles): Battery replaced\n'
                                       '  - May 2025: Engine oil and filter changed, engine oil pump valve, engine oil '
                                       'separators, and rear main seal replaced, four-wheel alignment performed\n'
                                       '  - March 2025 (47,947 miles): Engine oil and filter and brake fluid changed, '
                                       'engine air filter and cabin air filter replaced, recall performed\n'
                                       '  - August 2024 (42,884 miles): Engine oil and filter and transfer case fluid '
                                       'changed, spark plugs and wiper blades replaced\n'
                                       '  - February 2024: Exterior wrap applied\n'
                                       '  - September 2023 (37,138 miles): Dent in left-rear fender fixed, mirror '
                                       'assembly replaced\n'
                                       'The attachedCarfaxhistory report shows that the following services have been '
                                       'performed:\n'
                                       '  - May 2026 (56,713 miles): Wiper blades/refills replaced, engine oil and '
                                       'filter changed\n'
                                       '  - January 2026 (53,027 miles): Alignment performed\n'
                                       '  - April 2024 (41,083 miles): Alignment performed\n'
                                       '  - August 2023 (36,651 miles): Brake fluid flushed/changed, four-wheel '
                                       'alignment performed, front brake pads and two tires replaced, engine oil and '
                                       'filter changed\n'
                                       '  - March 2023 (32,478 miles): Tire(s) mounted\n'
                                       '  - December 2022 (29,961 miles): Air filter replaced, engine oil and filter '
                                       'and transmission fluid and filter changed\n'
                                       '  - August 2022 (24,266 miles): Radiator and thermostat replaced\n'
                                       '  - May 2022 (21,448 miles): A/C receiver/dryer, front brake pads, and rear '
                                       'brake pads replaced, antifreeze/coolant flushed/changed, four-wheel alignment '
                                       'performed\n'
                                       '  - March 2022 (19,114 miles): Brake fluid flushed/changed, cabin air filter '
                                       'replaced/cleaned, engine oil and filter changed\n'
                                       '  - October 2021 (10,868 miles): Adaptive cruise control sensor aligned, '
                                       'windshield replaced\n'
                                       '  - September 2021 (9,452 miles): Engine oil and filter changed\n'
                                       '  - August 2021 (8,738 miles): Engine/powertrain computer/module reprogrammed\n'
                                       '  - July 2021 (6,068 miles): Engine/powertrain computer/module reprogrammed'},
                           {'title': 'OTHER ITEMS INCLUDED IN SALE',
                            'content': "- 2 keys\n  - Owner's manual\n  - Service records\n  - Factory downpipes"},
                           {'title': 'OWNERSHIP HISTORY',
                            'content': 'The seller reportedly purchased this E63 in August 2023 and has added about '
                                       '23,000 miles since.'},
                           {'title': 'SELLER NOTES',
                            'content': '- The seller states that the windows are tinted.\n'
                                       '  - Due to the modifications performed to this E63, it may not pass emissions '
                                       "testing in some states. As always, it's thebuyer's responsibilityto perform "
                                       'all due diligence regarding registering this car in their respective '
                                       'stateprior to placing a bid.'}],
              'raw_description': 'HIGHLIGHTS\n'
                                 '\n'
                                 'THIS... is a 2021 Mercedes-AMG E63 S Sedan, finished in Obsidian Black Metallic with '
                                 'a Satin Dark Gray exterior wrap and a Titanium Gray and black interior.\n'
                                 '  - The attachedCarfaxhistory report shows that this E63 has been California-owned '
                                 'since new.\n'
                                 '  - Notable modifications reported by the seller include a DME Tuning Stage 1 tune, '
                                 'CTS Turbo cat-less downpipes, and a Valvetronic Designs electronic exhaust valve '
                                 'control kit. The factory downpipes are reportedly included in the sale.\n'
                                 '  - A window sticker is provided in the gallery, and a partial list of notable '
                                 'equipment reported by the seller includes the Driver Assistance and AMG Night '
                                 'packages, heated and ventilated front seats, heated rear seats, and a Burmester '
                                 'surround sound system.\n'
                                 '  - Released for 2018, the W213-based E63 arrived with a more fluid exterior design, '
                                 'a smaller yet more powerful engine, and an even longer list of standard features '
                                 'than its predecessor. Mercedes-AMG offered two variants: the base E63 and the '
                                 'pricier S model, which received upgrades like a more powerful engine and a drift '
                                 'mode.\n'
                                 '  - Power comes from a 4.0-liter twin-turbocharged V8, rated at 603 horsepower and '
                                 '627 lb-ft of torque in stock form. The seller states that the modifications increase '
                                 'horsepower to 750, but a dyno sheet was not provided to confirm. Output is sent to '
                                 'all four wheels via a 9-speed automatic transmission.\n'
                                 '\n'
                                 'EQUIPMENT\n'
                                 '\n'
                                 'A window sticker is provided in the gallery, and a partial list of notable equipment '
                                 'reported by the seller includes:\n'
                                 '  - Driver Assistance Package\n'
                                 '  - Exterior Lighting Package\n'
                                 '  - AMG Night Package\n'
                                 '  - 20-inch wheels\n'
                                 '  - Heated and ventilated front seats\n'
                                 '  - Heated rear seats\n'
                                 '  - Carbon fiber interior trim\n'
                                 '  - Burmester surround sound system\n'
                                 '  - Head-up display\n'
                                 '  - Dashcam\n'
                                 '\n'
                                 'MODIFICATIONS\n'
                                 '\n'
                                 'Notable modifications reported by the seller include:\n'
                                 '  - DME Tuning Stage 1 tune\n'
                                 '  - CTS Turbo cat-less downpipes\n'
                                 '  - Valvetronic Designs electronic exhaust valve control kit\n'
                                 '  - RennTech EVM exhaust module\n'
                                 '  - Lowering module\n'
                                 '  - Avery Dennison Satin Dark Gray exterior wrap\n'
                                 '\n'
                                 'KNOWN FLAWS\n'
                                 '\n'
                                 '  - The attachedCarfaxhistory report notes that this E63 sustained "minor damage" in '
                                 'April 2023. It adds that "minor damage" is usually cosmetic, like dents and '
                                 'scratches on the body.\n'
                                 '  - Some exterior scratches (shown in the gallery)\n'
                                 '  - Some scratches on the driver-side front wheel\n'
                                 "  - Some wear on the driver's seat's outer bolsters\n"
                                 '\n'
                                 'RECENT SERVICE HISTORY\n'
                                 '\n'
                                 'Service documentation in the gallery indicates that the following maintenance has '
                                 'been performed:\n'
                                 '  - January 2026 (52,905 miles): Battery replaced\n'
                                 '  - May 2025: Engine oil and filter changed, engine oil pump valve, engine oil '
                                 'separators, and rear main seal replaced, four-wheel alignment performed\n'
                                 '  - March 2025 (47,947 miles): Engine oil and filter and brake fluid changed, engine '
                                 'air filter and cabin air filter replaced, recall performed\n'
                                 '  - August 2024 (42,884 miles): Engine oil and filter and transfer case fluid '
                                 'changed, spark plugs and wiper blades replaced\n'
                                 '  - February 2024: Exterior wrap applied\n'
                                 '  - September 2023 (37,138 miles): Dent in left-rear fender fixed, mirror assembly '
                                 'replaced\n'
                                 'The attachedCarfaxhistory report shows that the following services have been '
                                 'performed:\n'
                                 '  - May 2026 (56,713 miles): Wiper blades/refills replaced, engine oil and filter '
                                 'changed\n'
                                 '  - January 2026 (53,027 miles): Alignment performed\n'
                                 '  - April 2024 (41,083 miles): Alignment performed\n'
                                 '  - August 2023 (36,651 miles): Brake fluid flushed/changed, four-wheel alignment '
                                 'performed, front brake pads and two tires replaced, engine oil and filter changed\n'
                                 '  - March 2023 (32,478 miles): Tire(s) mounted\n'
                                 '  - December 2022 (29,961 miles): Air filter replaced, engine oil and filter and '
                                 'transmission fluid and filter changed\n'
                                 '  - August 2022 (24,266 miles): Radiator and thermostat replaced\n'
                                 '  - May 2022 (21,448 miles): A/C receiver/dryer, front brake pads, and rear brake '
                                 'pads replaced, antifreeze/coolant flushed/changed, four-wheel alignment performed\n'
                                 '  - March 2022 (19,114 miles): Brake fluid flushed/changed, cabin air filter '
                                 'replaced/cleaned, engine oil and filter changed\n'
                                 '  - October 2021 (10,868 miles): Adaptive cruise control sensor aligned, windshield '
                                 'replaced\n'
                                 '  - September 2021 (9,452 miles): Engine oil and filter changed\n'
                                 '  - August 2021 (8,738 miles): Engine/powertrain computer/module reprogrammed\n'
                                 '  - July 2021 (6,068 miles): Engine/powertrain computer/module reprogrammed\n'
                                 '\n'
                                 'OTHER ITEMS INCLUDED IN SALE\n'
                                 '\n'
                                 '  - 2 keys\n'
                                 "  - Owner's manual\n"
                                 '  - Service records\n'
                                 '  - Factory downpipes\n'
                                 '\n'
                                 'OWNERSHIP HISTORY\n'
                                 '\n'
                                 'The seller reportedly purchased this E63 in August 2023 and has added about 23,000 '
                                 'miles since.\n'
                                 '\n'
                                 'SELLER NOTES\n'
                                 '\n'
                                 '  - The seller states that the windows are tinted.\n'
                                 '  - Due to the modifications performed to this E63, it may not pass emissions '
                                 "testing in some states. As always, it's thebuyer's responsibilityto perform all due "
                                 'diligence regarding registering this car in their respective stateprior to placing a '
                                 'bid.'},
  'featured': False,
  'financing_available': True,
  'warranty_available': True,
  'delivery_available': True},
 {'id': '2024-audi-rs-q8',
  'slug': '2024-audi-rs-q8',
  'title': '2024 Audi RS Q8',
  'make': 'Audi',
  'model': 'RS Q8',
  'trim': '',
  'year': 2024,
  'status': 'Available',
  'stock_number': 'RUC07255',
  'vin': 'WU1ARBF12RD007255',
  'price': 81999,
  'mileage': 14900,
  'body_type': 'SUV/Crossover',
  'transmission': 'Automatic (8-Speed)',
  'drivetrain': '4WD/AWD',
  'engine': '4.0L Turbocharged V8',
  'exterior_color': 'Mythos Black Metallic',
  'interior_color': 'Black',
  'location': 'Commodore, PA',
  'short_description': '2024 Audi RS Q8 finished in Mythos Black Metallic with a Black interior, 14,900 miles, and '
                       '4.0L Turbocharged V8.',
  'description': 'THIS... is a 2024 Audi RS Q8, finished in Mythos Black Metallic with a black interior.',
  'images': ['/media/vehicles/2024-audi-rs-q8/01.jpg',
             '/media/vehicles/2024-audi-rs-q8/02.jpg',
             '/media/vehicles/2024-audi-rs-q8/03.jpg',
             '/media/vehicles/2024-audi-rs-q8/04.jpg',
             '/media/vehicles/2024-audi-rs-q8/05.jpg',
             '/media/vehicles/2024-audi-rs-q8/06.jpg',
             '/media/vehicles/2024-audi-rs-q8/07.jpg',
             '/media/vehicles/2024-audi-rs-q8/08.jpg',
             '/media/vehicles/2024-audi-rs-q8/09.jpg',
             '/media/vehicles/2024-audi-rs-q8/10.jpg',
             '/media/vehicles/2024-audi-rs-q8/11.jpg',
             '/media/vehicles/2024-audi-rs-q8/12.jpg',
             '/media/vehicles/2024-audi-rs-q8/13.jpg',
             '/media/vehicles/2024-audi-rs-q8/14.jpg',
             '/media/vehicles/2024-audi-rs-q8/15.jpg',
             '/media/vehicles/2024-audi-rs-q8/16.jpg',
             '/media/vehicles/2024-audi-rs-q8/17.jpg',
             '/media/vehicles/2024-audi-rs-q8/18.jpg',
             '/media/vehicles/2024-audi-rs-q8/19.jpg',
             '/media/vehicles/2024-audi-rs-q8/20.jpg',
             '/media/vehicles/2024-audi-rs-q8/21.jpg',
             '/media/vehicles/2024-audi-rs-q8/22.jpg',
             '/media/vehicles/2024-audi-rs-q8/23.jpg',
             '/media/vehicles/2024-audi-rs-q8/24.jpg',
             '/media/vehicles/2024-audi-rs-q8/25.jpg',
             '/media/vehicles/2024-audi-rs-q8/26.jpg',
             '/media/vehicles/2024-audi-rs-q8/27.jpg',
             '/media/vehicles/2024-audi-rs-q8/28.jpg',
             '/media/vehicles/2024-audi-rs-q8/29.jpg',
             '/media/vehicles/2024-audi-rs-q8/30.jpg',
             '/media/vehicles/2024-audi-rs-q8/31.jpg',
             '/media/vehicles/2024-audi-rs-q8/32.jpg',
             '/media/vehicles/2024-audi-rs-q8/33.jpg',
             '/media/vehicles/2024-audi-rs-q8/34.jpg',
             '/media/vehicles/2024-audi-rs-q8/35.jpg',
             '/media/vehicles/2024-audi-rs-q8/36.jpg',
             '/media/vehicles/2024-audi-rs-q8/37.jpg',
             '/media/vehicles/2024-audi-rs-q8/38.jpg',
             '/media/vehicles/2024-audi-rs-q8/39.jpg',
             '/media/vehicles/2024-audi-rs-q8/40.jpg',
             '/media/vehicles/2024-audi-rs-q8/41.jpg',
             '/media/vehicles/2024-audi-rs-q8/42.jpg',
             '/media/vehicles/2024-audi-rs-q8/43.jpg',
             '/media/vehicles/2024-audi-rs-q8/44.jpg',
             '/media/vehicles/2024-audi-rs-q8/45.jpg',
             '/media/vehicles/2024-audi-rs-q8/46.jpg',
             '/media/vehicles/2024-audi-rs-q8/47.jpg',
             '/media/vehicles/2024-audi-rs-q8/48.jpg',
             '/media/vehicles/2024-audi-rs-q8/49.jpg',
             '/media/vehicles/2024-audi-rs-q8/50.jpg',
             '/media/vehicles/2024-audi-rs-q8/51.jpg',
             '/media/vehicles/2024-audi-rs-q8/52.jpg',
             '/media/vehicles/2024-audi-rs-q8/53.jpg',
             '/media/vehicles/2024-audi-rs-q8/54.jpg',
             '/media/vehicles/2024-audi-rs-q8/55.jpg',
             '/media/vehicles/2024-audi-rs-q8/56.jpg',
             '/media/vehicles/2024-audi-rs-q8/57.jpg',
             '/media/vehicles/2024-audi-rs-q8/58.jpg',
             '/media/vehicles/2024-audi-rs-q8/59.jpg',
             '/media/vehicles/2024-audi-rs-q8/60.jpg',
             '/media/vehicles/2024-audi-rs-q8/61.jpg',
             '/media/vehicles/2024-audi-rs-q8/62.jpg',
             '/media/vehicles/2024-audi-rs-q8/63.jpg',
             '/media/vehicles/2024-audi-rs-q8/64.jpg',
             '/media/vehicles/2024-audi-rs-q8/65.jpg',
             '/media/vehicles/2024-audi-rs-q8/66.jpg',
             '/media/vehicles/2024-audi-rs-q8/67.jpg',
             '/media/vehicles/2024-audi-rs-q8/68.jpg',
             '/media/vehicles/2024-audi-rs-q8/69.jpg',
             '/media/vehicles/2024-audi-rs-q8/70.jpg',
             '/media/vehicles/2024-audi-rs-q8/71.jpg',
             '/media/vehicles/2024-audi-rs-q8/72.jpg',
             '/media/vehicles/2024-audi-rs-q8/73.jpg',
             '/media/vehicles/2024-audi-rs-q8/74.jpg',
             '/media/vehicles/2024-audi-rs-q8/75.jpg',
             '/media/vehicles/2024-audi-rs-q8/76.jpg',
             '/media/vehicles/2024-audi-rs-q8/77.jpg',
             '/media/vehicles/2024-audi-rs-q8/78.jpg',
             '/media/vehicles/2024-audi-rs-q8/79.jpg',
             '/media/vehicles/2024-audi-rs-q8/80.jpg',
             '/media/vehicles/2024-audi-rs-q8/81.jpg',
             '/media/vehicles/2024-audi-rs-q8/82.jpg',
             '/media/vehicles/2024-audi-rs-q8/83.jpg',
             '/media/vehicles/2024-audi-rs-q8/84.jpg',
             '/media/vehicles/2024-audi-rs-q8/85.jpg',
             '/media/vehicles/2024-audi-rs-q8/86.jpg',
             '/media/vehicles/2024-audi-rs-q8/87.jpg',
             '/media/vehicles/2024-audi-rs-q8/88.jpg',
             '/media/vehicles/2024-audi-rs-q8/89.jpg',
             '/media/vehicles/2024-audi-rs-q8/90.jpg',
             '/media/vehicles/2024-audi-rs-q8/91.jpg',
             '/media/vehicles/2024-audi-rs-q8/92.jpg',
             '/media/vehicles/2024-audi-rs-q8/93.jpg',
             '/media/vehicles/2024-audi-rs-q8/94.jpg',
             '/media/vehicles/2024-audi-rs-q8/95.jpg',
             '/media/vehicles/2024-audi-rs-q8/96.jpg',
             '/media/vehicles/2024-audi-rs-q8/97.jpg',
             '/media/vehicles/2024-audi-rs-q8/98.jpg',
             '/media/vehicles/2024-audi-rs-q8/99.jpg',
             '/media/vehicles/2024-audi-rs-q8/100.jpg',
             '/media/vehicles/2024-audi-rs-q8/101.jpg',
             '/media/vehicles/2024-audi-rs-q8/102.jpg',
             '/media/vehicles/2024-audi-rs-q8/103.jpg',
             '/media/vehicles/2024-audi-rs-q8/104.jpg',
             '/media/vehicles/2024-audi-rs-q8/105.jpg',
             '/media/vehicles/2024-audi-rs-q8/106.jpg',
             '/media/vehicles/2024-audi-rs-q8/107.jpg',
             '/media/vehicles/2024-audi-rs-q8/108.jpg',
             '/media/vehicles/2024-audi-rs-q8/109.jpg',
             '/media/vehicles/2024-audi-rs-q8/110.jpg',
             '/media/vehicles/2024-audi-rs-q8/111.jpg',
             '/media/vehicles/2024-audi-rs-q8/112.jpg',
             '/media/vehicles/2024-audi-rs-q8/113.jpg',
             '/media/vehicles/2024-audi-rs-q8/114.jpg',
             '/media/vehicles/2024-audi-rs-q8/115.jpg',
             '/media/vehicles/2024-audi-rs-q8/116.jpg',
             '/media/vehicles/2024-audi-rs-q8/117.jpg',
             '/media/vehicles/2024-audi-rs-q8/118.jpg',
             '/media/vehicles/2024-audi-rs-q8/119.jpg',
             '/media/vehicles/2024-audi-rs-q8/120.jpg',
             '/media/vehicles/2024-audi-rs-q8/121.jpg',
             '/media/vehicles/2024-audi-rs-q8/122.jpg',
             '/media/vehicles/2024-audi-rs-q8/123.jpg',
             '/media/vehicles/2024-audi-rs-q8/124.jpg',
             '/media/vehicles/2024-audi-rs-q8/125.png',
             '/media/vehicles/2024-audi-rs-q8/126.png',
             '/media/vehicles/2024-audi-rs-q8/127.png',
             '/media/vehicles/2024-audi-rs-q8/128.png'],
  'features': ['Executive Package',
               'RS Design Package, Red',
               'Luxury Package',
               'Carbon Package',
               'Black Optic Package'],
  'specs': {},
  'details': {'info': [{'label': 'Title', 'value': '2024 Audi RS Q8'},
                       {'label': 'Make', 'value': 'Audi'},
                       {'label': 'Engine', 'value': '4.0L Turbocharged V8'},
                       {'label': 'Model', 'value': 'RS Q8Save'},
                       {'label': 'Drivetrain', 'value': '4WD/AWD'},
                       {'label': 'Mileage', 'value': '14,900'},
                       {'label': 'Transmission', 'value': 'Automatic (8-Speed)'},
                       {'label': 'VIN', 'value': 'WU1ARBF12RD007255'},
                       {'label': 'Body Style', 'value': 'SUV/Crossover'},
                       {'label': 'Title Status', 'value': 'Clean (MD)'},
                       {'label': 'Exterior Color', 'value': 'Mythos Black Metallic'},
                       {'label': 'Location', 'value': 'Severna Park, MD 21146'},
                       {'label': 'Interior Color', 'value': 'Black'},
                       {'label': 'Seller', 'value': 'petersoneill'},
                       {'label': 'Seller Type', 'value': 'Private Party'}],
              'sections': [{'title': 'HIGHLIGHTS',
                            'content': 'THIS... is a 2024 Audi RS Q8, finished in Mythos Black Metallic with a black '
                                       'interior.\n'
                                       '  - This RS Q8 is a Canadian-spec SUV that was imported and declared to meet '
                                       "US highway safety specifications in September 2024. It's equipped with a "
                                       'digital instrument cluster that displays in both metric and imperial units.\n'
                                       '  - The attachedCarfaxhistory report lists no accidents or mileage '
                                       "discrepancies in this RS Q8's past.\n"
                                       '  - According to the build sheet provided in the gallery, notable factory '
                                       'equipment includes the Executive, RS Design, Luxury, Carbon, and Black Optic '
                                       'packages, 23-inch 5-Y-spoke rotor wheels, heated and ventilated front seats, '
                                       'adaptive cruise assist, and a Bang & Olufsen sound system. The seller reports '
                                       'no notable modifications.\n'
                                       '  - The Audi RS Q8 was Audi\'s first foray into the "Super" SUV market, built '
                                       'to compete with other high-performance SUVs like the BMW X6M and the '
                                       'Mercedes-AMG GLE 63. Manufactured on the same underpinnings as the Lamborghini '
                                       'Urus and utilizing the same (albeit slightly de-tuned) twin-turbocharged V8 '
                                       'engine, the RS Q8 can sprint to 60 mph in under 3.8 seconds, a staggering '
                                       'figure considering its almost 5,500 lb. curb weight.\n'
                                       '  - Power comes from a 4.0-liter twin-turbocharged V8 and a 48-volt '
                                       'mild-hybrid system, rated at 591 horsepower and 590 lb-ft of torque. Output is '
                                       "sent to all four wheels via an 8-speed automatic transmission and Audi's "
                                       'Quattro permanent all-wheel drive system.'},
                           {'title': 'EQUIPMENT',
                            'content': 'A build sheet is provided in the photo gallery, and a partial list of notable '
                                       'equipment reported by the seller includes:\n'
                                       '  - Executive Package\n'
                                       '  - RS Design Package, Red\n'
                                       '  - Luxury Package\n'
                                       '  - Carbon Package\n'
                                       '  - Black Optic Package\n'
                                       '  - 23-inch 5-Y-spoke rotor wheels\n'
                                       '  - All-wheel steering\n'
                                       '  - Panoramic sunroof\n'
                                       '  - Heated and ventilated front seats\n'
                                       '  - Adaptive cruise assist\n'
                                       '  - Bang & Olufsen sound system'},
                           {'title': 'KNOWN FLAWS', 'content': "- Some creases on driver's seat bolster"},
                           {'title': 'RECENT SERVICE HISTORY',
                            'content': 'Some service history is detailed in the attachedCarfaxhistory report.'},
                           {'title': 'OTHER ITEMS INCLUDED IN SALE',
                            'content': "- 2 keys\n  - Owner's manual\n  - WeatherTech floor mats and cargo mat"},
                           {'title': 'OWNERSHIP HISTORY',
                            'content': 'The seller reportedly purchased this RS Q8 in December 2024.'}],
              'raw_description': 'HIGHLIGHTS\n'
                                 '\n'
                                 'THIS... is a 2024 Audi RS Q8, finished in Mythos Black Metallic with a black '
                                 'interior.\n'
                                 '  - This RS Q8 is a Canadian-spec SUV that was imported and declared to meet US '
                                 "highway safety specifications in September 2024. It's equipped with a digital "
                                 'instrument cluster that displays in both metric and imperial units.\n'
                                 '  - The attachedCarfaxhistory report lists no accidents or mileage discrepancies in '
                                 "this RS Q8's past.\n"
                                 '  - According to the build sheet provided in the gallery, notable factory equipment '
                                 'includes the Executive, RS Design, Luxury, Carbon, and Black Optic packages, 23-inch '
                                 '5-Y-spoke rotor wheels, heated and ventilated front seats, adaptive cruise assist, '
                                 'and a Bang & Olufsen sound system. The seller reports no notable modifications.\n'
                                 '  - The Audi RS Q8 was Audi\'s first foray into the "Super" SUV market, built to '
                                 'compete with other high-performance SUVs like the BMW X6M and the Mercedes-AMG GLE '
                                 '63. Manufactured on the same underpinnings as the Lamborghini Urus and utilizing the '
                                 'same (albeit slightly de-tuned) twin-turbocharged V8 engine, the RS Q8 can sprint to '
                                 '60 mph in under 3.8 seconds, a staggering figure considering its almost 5,500 lb. '
                                 'curb weight.\n'
                                 '  - Power comes from a 4.0-liter twin-turbocharged V8 and a 48-volt mild-hybrid '
                                 'system, rated at 591 horsepower and 590 lb-ft of torque. Output is sent to all four '
                                 "wheels via an 8-speed automatic transmission and Audi's Quattro permanent all-wheel "
                                 'drive system.\n'
                                 '\n'
                                 'EQUIPMENT\n'
                                 '\n'
                                 'A build sheet is provided in the photo gallery, and a partial list of notable '
                                 'equipment reported by the seller includes:\n'
                                 '  - Executive Package\n'
                                 '  - RS Design Package, Red\n'
                                 '  - Luxury Package\n'
                                 '  - Carbon Package\n'
                                 '  - Black Optic Package\n'
                                 '  - 23-inch 5-Y-spoke rotor wheels\n'
                                 '  - All-wheel steering\n'
                                 '  - Panoramic sunroof\n'
                                 '  - Heated and ventilated front seats\n'
                                 '  - Adaptive cruise assist\n'
                                 '  - Bang & Olufsen sound system\n'
                                 '\n'
                                 'KNOWN FLAWS\n'
                                 '\n'
                                 "  - Some creases on driver's seat bolster\n"
                                 '\n'
                                 'RECENT SERVICE HISTORY\n'
                                 '\n'
                                 'Some service history is detailed in the attachedCarfaxhistory report.\n'
                                 '\n'
                                 'OTHER ITEMS INCLUDED IN SALE\n'
                                 '\n'
                                 '  - 2 keys\n'
                                 "  - Owner's manual\n"
                                 '  - WeatherTech floor mats and cargo mat\n'
                                 '\n'
                                 'OWNERSHIP HISTORY\n'
                                 '\n'
                                 'The seller reportedly purchased this RS Q8 in December 2024.'},
  'featured': True,
  'financing_available': True,
  'warranty_available': True,
  'delivery_available': True},
 {'id': '2026-ram-1500-rho-crew-cab-4x4',
  'slug': '2026-ram-1500-rho-crew-cab-4x4',
  'title': '2026 Ram 1500 RHO Crew Cab 4x4',
  'make': 'Ram',
  'model': '1500 RHO',
  'trim': 'Crew Cab 4x4',
  'year': 2026,
  'status': 'Available',
  'stock_number': 'RUC63640',
  'vin': '1C6SRFUP8TN363640',
  'price': 49999,
  'mileage': 709,
  'body_type': 'Truck',
  'transmission': 'Automatic (8-Speed)',
  'drivetrain': '4WD/AWD',
  'engine': '3.0L Turbocharged I6',
  'exterior_color': 'Forged Blue Metallic',
  'interior_color': 'Black',
  'location': 'Commodore, PA',
  'short_description': '2026 Ram 1500 RHO Crew Cab 4x4 finished in Forged Blue Metallic with a Black interior, 709 '
                       'miles, and 3.0L Turbocharged I6.',
  'description': 'THIS… is a 2026 Ram 1500 RHO Crew Cab 4x4, finished in Forged Blue Metallic with a black interior.',
  'images': ['/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/01.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/02.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/03.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/04.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/05.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/06.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/07.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/08.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/09.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/10.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/11.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/12.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/13.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/14.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/15.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/16.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/17.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/18.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/19.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/20.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/21.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/22.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/23.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/24.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/25.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/26.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/27.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/28.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/29.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/30.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/31.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/32.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/33.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/34.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/35.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/36.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/37.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/38.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/39.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/40.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/41.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/42.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/43.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/44.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/45.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/46.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/47.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/48.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/49.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/50.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/51.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/52.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/53.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/54.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/55.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/56.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/57.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/58.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/59.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/60.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/61.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/62.jpg',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/63.png',
             '/media/vehicles/2026-ram-1500-rho-crew-cab-4x4/64.png'],
  'features': ['Customer Preferred Package 22Y',
               '18-inch aluminum wheels',
               'Locking rear differential',
               'Active-performance shock absorbers with adaptive damping',
               'High-performance brakes'],
  'specs': {},
  'details': {'info': [{'label': 'Title', 'value': '2026 Ram 1500 RHO Crew Cab 4x4'},
                       {'label': 'Make', 'value': 'Ram'},
                       {'label': 'Engine', 'value': '3.0L Turbocharged I6'},
                       {'label': 'Model', 'value': '1500Save'},
                       {'label': 'Drivetrain', 'value': '4WD/AWD'},
                       {'label': 'Mileage', 'value': '709'},
                       {'label': 'Transmission', 'value': 'Automatic (8-Speed)'},
                       {'label': 'VIN', 'value': '1C6SRFUP8TN363640'},
                       {'label': 'Body Style', 'value': 'Truck'},
                       {'label': 'Title Status', 'value': 'Clean (AR)'},
                       {'label': 'Exterior Color', 'value': 'Forged Blue Metallic'},
                       {'label': 'Location', 'value': 'Wynne, AR 72396'},
                       {'label': 'Interior Color', 'value': 'Black'},
                       {'label': 'Seller', 'value': 'CortesA2000'},
                       {'label': 'Seller Type', 'value': 'Private Party'}],
              'sections': [{'title': 'HIGHLIGHTS',
                            'content': 'THIS… is a 2026 Ram 1500 RHO Crew Cab 4x4, finished in Forged Blue Metallic '
                                       'with a black interior.\n'
                                       '  - The odometer on this Ram currently displays approximately 709 miles.\n'
                                       '  - The attachedCarfaxvehicle history report shows no accidents or mileage '
                                       'discrepancies in this trucks’s brief past.\n'
                                       '  - According to the window sticker provided in the gallery, notable factory '
                                       'equipment includes Customer Preferred Package 22Y, 18-inch aluminum wheels, '
                                       'Active-performance shock absorbers with adaptive damping, heated front seats, '
                                       'and adaptive cruise control with stop and go. The seller reports no notable '
                                       'modifications.\n'
                                       '  - The fifth-generation Ram truck was launched for the 2019 model year with a '
                                       'revised design, technological updates, and a range of capable engines. For '
                                       '2025, the Ram 1500 RHO replaced the then-discontinued TRX.\n'
                                       '  - Power comes from a twin-turbocharged 3.0-liter inline-six, rated at 540 '
                                       'horsepower and 521 lb-ft of torque. Output is sent to all four wheels via an '
                                       '8-speed automatic transmission and a 2-speed transfer case.'},
                           {'title': 'EQUIPMENT',
                            'content': 'A window sticker is provided in the photo gallery, and a partial list of '
                                       'notable equipment reported by the seller includes:\n'
                                       '  - Customer Preferred Package 22Y\n'
                                       '  - 18-inch aluminum wheels\n'
                                       '  - Locking rear differential\n'
                                       '  - Active-performance shock absorbers with adaptive damping\n'
                                       '  - High-performance brakes\n'
                                       '  - Heated front seats\n'
                                       '  - Adaptive cruise control with stop and go'},
                           {'title': 'RECENT SERVICE HISTORY',
                            'content': 'The seller states that this RHO has not required service due to its low '
                                       'mileage.'},
                           {'title': 'OTHER ITEMS INCLUDED IN SALE',
                            'content': "- 2 keys\n  - Owner's manual\n  - Window sticker"},
                           {'title': 'OWNERSHIP HISTORY',
                            'content': 'The seller reports that they purchased this Ram when new in May 2026.'},
                           {'title': 'SELLER NOTES',
                            'content': 'The seller reports that the windows have been tinted.'}],
              'raw_description': 'HIGHLIGHTS\n'
                                 '\n'
                                 'THIS… is a 2026 Ram 1500 RHO Crew Cab 4x4, finished in Forged Blue Metallic with a '
                                 'black interior.\n'
                                 '  - The odometer on this Ram currently displays approximately 709 miles.\n'
                                 '  - The attachedCarfaxvehicle history report shows no accidents or mileage '
                                 'discrepancies in this trucks’s brief past.\n'
                                 '  - According to the window sticker provided in the gallery, notable factory '
                                 'equipment includes Customer Preferred Package 22Y, 18-inch aluminum wheels, '
                                 'Active-performance shock absorbers with adaptive damping, heated front seats, and '
                                 'adaptive cruise control with stop and go. The seller reports no notable '
                                 'modifications.\n'
                                 '  - The fifth-generation Ram truck was launched for the 2019 model year with a '
                                 'revised design, technological updates, and a range of capable engines. For 2025, the '
                                 'Ram 1500 RHO replaced the then-discontinued TRX.\n'
                                 '  - Power comes from a twin-turbocharged 3.0-liter inline-six, rated at 540 '
                                 'horsepower and 521 lb-ft of torque. Output is sent to all four wheels via an 8-speed '
                                 'automatic transmission and a 2-speed transfer case.\n'
                                 '\n'
                                 'EQUIPMENT\n'
                                 '\n'
                                 'A window sticker is provided in the photo gallery, and a partial list of notable '
                                 'equipment reported by the seller includes:\n'
                                 '  - Customer Preferred Package 22Y\n'
                                 '  - 18-inch aluminum wheels\n'
                                 '  - Locking rear differential\n'
                                 '  - Active-performance shock absorbers with adaptive damping\n'
                                 '  - High-performance brakes\n'
                                 '  - Heated front seats\n'
                                 '  - Adaptive cruise control with stop and go\n'
                                 '\n'
                                 'RECENT SERVICE HISTORY\n'
                                 '\n'
                                 'The seller states that this RHO has not required service due to its low mileage.\n'
                                 '\n'
                                 'OTHER ITEMS INCLUDED IN SALE\n'
                                 '\n'
                                 '  - 2 keys\n'
                                 "  - Owner's manual\n"
                                 '  - Window sticker\n'
                                 '\n'
                                 'OWNERSHIP HISTORY\n'
                                 '\n'
                                 'The seller reports that they purchased this Ram when new in May 2026.\n'
                                 '\n'
                                 'SELLER NOTES\n'
                                 '\n'
                                 'The seller reports that the windows have been tinted.'},
  'featured': False,
  'financing_available': True,
  'warranty_available': True,
  'delivery_available': True}]


def vehicles_table() -> sa.Table:
    return sa.table(
        "vehicles",
        sa.column("id", sa.String),
        sa.column("slug", sa.String),
        sa.column("title", sa.String),
        sa.column("make", sa.String),
        sa.column("model", sa.String),
        sa.column("trim", sa.String),
        sa.column("year", sa.Integer),
        sa.column("status", sa.String),
        sa.column("stock_number", sa.String),
        sa.column("vin", sa.String),
        sa.column("price", sa.Integer),
        sa.column("mileage", sa.Integer),
        sa.column("body_type", sa.String),
        sa.column("transmission", sa.String),
        sa.column("drivetrain", sa.String),
        sa.column("engine", sa.String),
        sa.column("exterior_color", sa.String),
        sa.column("interior_color", sa.String),
        sa.column("location", sa.String),
        sa.column("short_description", sa.String),
        sa.column("description", sa.Text),
        sa.column("images", sa.JSON),
        sa.column("features", sa.JSON),
        sa.column("specs", sa.JSON),
        sa.column("details", sa.JSON),
        sa.column("featured", sa.Boolean),
        sa.column("financing_available", sa.Boolean),
        sa.column("warranty_available", sa.Boolean),
        sa.column("delivery_available", sa.Boolean),
        sa.column("created_at", sa.DateTime),
    )


def upgrade() -> None:
    vehicles = vehicles_table()
    connection = op.get_bind()

    for vehicle_id, price in PRICE_UPDATES.items():
        connection.execute(
            vehicles.update().where(vehicles.c.id == vehicle_id).values(price=price)
        )

    rows = [{**vehicle, "created_at": CREATED_AT} for vehicle in NEW_VEHICLES]
    op.bulk_insert(vehicles, rows)


def downgrade() -> None:
    vehicles = vehicles_table()
    connection = op.get_bind()
    new_ids = [vehicle["id"] for vehicle in NEW_VEHICLES]

    connection.execute(
        sa.text("UPDATE leads SET vehicle_id = NULL WHERE vehicle_id IN :ids").bindparams(sa.bindparam("ids", expanding=True)),
        {"ids": new_ids},
    )
    connection.execute(
        sa.text("DELETE FROM vehicles WHERE id IN :ids").bindparams(sa.bindparam("ids", expanding=True)),
        {"ids": new_ids},
    )

    for vehicle_id in PRICE_UPDATES:
        connection.execute(
            vehicles.update().where(vehicles.c.id == vehicle_id).values(price=0)
        )
