
class Category(object):
    def __init__(self):

        self.GARBAGE = [
            'WASTE MANAGEMENT'
        ]
        self.STUDENT_LOANS = [
            'SALLIEMAEBANK',
            'FEDLOANSERVICING'
        ]
        self.TRANSPORTATION = [
            'WI DEPT OF TRANSPORT',
            'ADVANCE AUTO PARTS',
            'DOT EPAY DMV',
            'DMV',
            'Prestige Auto Corporati'
        ]
        self.EDUCATION = [
            'UDEMY ONLINE COURSES',
            'UDEMY.COM',
            'PLURALSIGHT',
            'COLLEGE TRANSCRIPT'
        ]
        self.HOTELS = [
            'PRICELINE*HOTEL ROOMS',
            'RIVER VALLEY INN',
            'SS CARD PACKAGE',
            'DELTA AIR'
        ]
        self.ATM = [
            'ATM'
        ]
        self.SUBSCRIPTIONS = [
            'AmazonPrime Membership',
            'PLANET FIT',
            'ITUNES',
            'NETFLIX',
            'Hulu'
        ]
        self.ENTERTAINMENT = [
            'CHEERS PABLO',
            'HUMBLEBUNDLE.COM',
            'NINTENDO',
            'Valve',
            'LAKE HALLIE VEND',
            'LAKE WISSOTA GOLF',
            'MICON CINEMAS',
            'OJIBWA GOLF',
            'FAMILY VIDEO',
            'CRYSTAL CAVE',
            'KNUCKLEHEADS',
            'BLIZZARD ENT',
            'AMELIAS GALENA GHO',
            'OAKWOOD 12',
            'STEAMGAMES.COM',
            'METROPOLIS',
            'DIRECTV'
        ]
        self.SHOPPING = [
            'KOHL',
            'TANGEN DRUG',
            'SCHEELS',
            'GREENER GRASS SYSTEMS',
            'BATH & BODY WORKS',
            'JOANN STORES',
            'YOUNKERS',
            'GOODWILL',
            'THE MENS WEARHOUSE',
            'B&H PHOTO',
            'MICHAELS STORES',
            'FAMILY DOLLAR',
            'SOL SISTER',
            'ETSY.COM',
            'WAL Wal-Mart',
            'WAL-MART',
            'VISTAPR',
            'WALMART.COM',
            'KATE SPADE',
            'HELZBERG DIAMONDS',
            'PERSONALIZATION MALL',
            'KIRKLAND\'S',
            'THE PAMPERED CHEF',
            'DOLLAR TREE',
            'DOLLAR GENERAL',
            'PIER 1',
            'WM SUPERCENTER',
            'OLD NAVY',
            'GORDMANS',
            'SHUTTERFLY',
            'AMAZON',
            'KITCHEN COLLECTION',
            'HOBBY-LOBBY',
            'FEDEXOFFICE',
            'SEARS',
            'SHOPKO',
            'SHOE DEPT ENCORE',
            'MASSDROP',
            'FARM & FLT',
            'MENARDS',
            'PAYLESS SHOES',
            'GAMES BY JAMES',
            'EVES ADDICTION'
        ]
        self.HOMEOWNERS_INSURANCE = [
          'Esurance',
          'ESURANCE'
        ]
        self.TAXES = [
          'TAX PRODUCTS',
          'WI DEPT REVENUE'
        ]
        self.GAS_STATIONS = [
            'CENEX EXPRESS',
            'MARATHON',
            'CENEX',
            'SPEEDWAY',
            'KWIK TRIP',
            'KWIK STAR',
            'HOLIDAY STNSTORE',
            'HOLIDAY STATION',
            'EXPRESS MART',
            'PHILLIPS 66'
        ]
        self.PHONE = [
            'ATT'
        ]
        self.LUNCHES = [
            'AVE C MKT'
        ]
        self.PAY_CHECKS = [
            'UNITED HEALTHCAR',
            'MASON COMPANIES'
        ]
        self.PET_SUPPLIES = [
            'PETSMART',
            'NO DOG LEFT BEHIND'
        ]
        self.MORTGAGES = [
            'WHEDA'
        ]
        self.ENERGY = [
            'XCEL ENERGY'
        ]
        self.CREDIT_CARDS = [
            'CHASE CREDIT',
            'WELLS FARGO CARD',
            'Synchrony Bank',
            'Transfer TO : XXXX2403',
            'Transfer TO : XXXX2692',
            'Transfer FROM: XXXX2692',
            'ASPEN DENTAL'
        ]
        self.CAR_PAYMENTS = [
            'BankoftheWest',
            'Transfer TO : XXXX0146',
            '0146'
        ]
        self.TRANSFERS = [
            'Transfer TO : XXXX3763',
            'Transfer TO : XXXX0108',
            'Transfer TO : XXXX0112',
            'Transfer FROM : XXXX0112',
            'Transfer FROM: XXXX0112',
            'Over Counter'
        ]
        self.UTILITIES = [
            'PSN*CITY OF CHIP',
            'PSN*CHIPPEWA'
        ]
        self.RESTAURANTS = [
            'NOODLES & COMPANY',
            'A & W',
            'TEXAS ROADHOUSE',
            'BYE THE WILLOW',
            'TACO JOHN',
            'THREE TWINS',
            'HNDISCOVER',
            'TIP TOP BAR',
            'SAKURA',
            'HU HOT MONGO',
            'RUMOR MILL',
            'CHINA MAX',
            'ERBERT AND GERBERTS',
            'CHINA WOK',
            'FOREIGN 5',
            'THE MACARONI CHEESE',
            'SUPER DUPER BURGER',
            'LUMBER JACKS',
            'BURGER KING',
            'SHEELEY HOUSE',
            'APPLEBEES',
            'CHIPPEWA FAMILY RESTAUR',
            'HC GAMING SUNRISE',
            'LUCY\'S DELI',
            'PANDA KING',
            'WENDYS',
            'DOMINO\'S',
            'ARBYS',
            'CHINA BUFFET',
            'LOOPYS SALOON & GRILL',
            'TOPPERS PIZZA',
            'SUBWAY',
            'CHIPOTLE',
            'MCDONALD\'S',
            'JADE GARDEN',
            'KFC',
            'RED LOBSTER',
            'DAIRY QUEEN',
            'NORSKE NOOK RESTAURANT',
            'PANERA BREAD',
            'JIMMY JOHNS',
            'CHARLEYS GRILLED SUBS',
            'STARBUCKS STORE',
            'RED ROBIN',
            'LITTLE CAESARS',
            'CHOPSTICKS ASIA TASTE',
            'PRETZEL MAKER',
            'OLIVE GARDEN',
            'CARIBOU COFFEE',
            'CHOCOLATERIE STAM',
            'DIAMOND JO',
            'CULVER\'S',
            'CULVERS',
            'TACO BELL',
            'FUJI SUSHI & STEAK HOUS',
            'HAPPY HOLLOW TAVERN'
        ]
        self.AUTO_INSURANCE = [
            'PROG UNIVERSAL'
        ]
        self.GROCERIES = [
            'GORDY\'S',
            'ECONOFOODS',
            'TARGET',
            'HY VEE',
            'B&G LIQUOR',
            'FESTIVAL FOODS'
        ]
        self.HAIR_CUTS = [
            'SPORT CLIPS',
            'SAXY SALON',
            'ALLWAYS HAIR',
            'GREAT CLIPS'
        ]
        self.INTERNET = [
            'CHARTER COMM'
        ]
        self.MISC = [
            'U-HAUL'
        ]
class_instance = Category()