# Trackable items extracted from the NZ Van Life Packing Checklist.
# Excludes: Documents & Admin (can't buy online), Van Equipment (buy in Auckland).

ITEMS = [
    # ── CLOTHING ────────────────────────────────────────────────────────────
    {
        "id": "merino_tshirt",
        "name": "Merino wool t-shirt ×3",
        "note": "Icebreaker, Macpac, or Kathmandu",
        "priority": "critical", "category": "Clothing", "qty": 3,
        "retailers": {
            "decathlon": "merino t-shirt",
            "amazon":    "Icebreaker merino wool t-shirt",
            "wiggle":    "Icebreaker merino t-shirt",
            "zalando":   "Icebreaker merino shirt",
        },
    },
    {
        "id": "merino_longsleeve",
        "name": "Merino long-sleeve top ×2",
        "note": "Base layer + mid-layer",
        "priority": "critical", "category": "Clothing", "qty": 2,
        "retailers": {
            "decathlon": "merino long sleeve top",
            "amazon":    "Icebreaker merino long sleeve",
            "wiggle":    "merino long sleeve base layer",
            "zalando":   "Icebreaker long sleeve",
        },
    },
    {
        "id": "fleece_jacket",
        "name": "Fleece mid-layer jacket",
        "note": "Patagonia or Macpac",
        "priority": "critical", "category": "Clothing", "qty": 1,
        "retailers": {
            "decathlon": "fleece hiking jacket",
            "amazon":    "Patagonia fleece jacket",
            "wiggle":    "fleece jacket outdoor",
            "zalando":   "Patagonia fleece jacket",
        },
    },
    {
        "id": "rain_jacket",
        "name": "Waterproof rain jacket (hardshell)",
        "note": "Non-negotiable for NZ weather",
        "priority": "critical", "category": "Clothing", "qty": 1,
        "retailers": {
            "decathlon": "hardshell waterproof jacket",
            "amazon":    "hardshell waterproof jacket hiking",
            "wiggle":    "hardshell jacket waterproof",
            "zalando":   "hardshell rain jacket",
        },
    },
    {
        "id": "hiking_trousers",
        "name": "Quick-dry hiking trousers ×2",
        "note": "Synthetic — no jeans",
        "priority": "critical", "category": "Clothing", "qty": 2,
        "retailers": {
            "decathlon": "hiking trousers quick dry",
            "amazon":    "quick dry hiking trousers",
            "wiggle":    "hiking trousers quick dry",
        },
    },
    {
        "id": "casual_trousers",
        "name": "Casual trousers / jeans",
        "note": "For town days",
        "priority": "high", "category": "Clothing", "qty": 1,
        "retailers": {
            "amazon":  "men chino trousers casual",
            "zalando": "slim fit chinos men",
        },
    },
    {
        "id": "merino_underwear",
        "name": "Merino underwear ×10",
        "note": "Merino if possible",
        "priority": "critical", "category": "Clothing", "qty": 10,
        "retailers": {
            "decathlon": "merino underwear",
            "amazon":    "merino wool underwear",
            "wiggle":    "merino underwear",
        },
    },
    {
        "id": "merino_socks",
        "name": "Merino hiking socks ×10 pairs",
        "note": "SmartWool or Darn Tough",
        "priority": "critical", "category": "Clothing", "qty": 10,
        "retailers": {
            "decathlon": "merino hiking socks",
            "amazon":    "SmartWool hiking socks",
            "wiggle":    "SmartWool hiking socks",
            "zalando":   "SmartWool socks",
        },
    },
    {
        "id": "thermal_base",
        "name": "Thermal base layer set (top + bottom)",
        "note": "Essential for South Island winter",
        "priority": "critical", "category": "Clothing", "qty": 1,
        "retailers": {
            "decathlon": "thermal base layer set",
            "amazon":    "thermal base layer set men",
            "wiggle":    "thermal base layer set",
        },
    },
    {
        "id": "beanie",
        "name": "Warm beanie",
        "note": "Merino ideal",
        "priority": "high", "category": "Clothing", "qty": 1,
        "retailers": {
            "decathlon": "merino wool beanie",
            "amazon":    "merino wool beanie hat",
            "zalando":   "merino beanie",
        },
    },
    {
        "id": "liner_gloves",
        "name": "Lightweight merino liner gloves",
        "priority": "high", "category": "Clothing", "qty": 1,
        "retailers": {
            "decathlon": "liner gloves merino",
            "amazon":    "merino liner gloves",
            "wiggle":    "merino liner gloves",
        },
    },
    {
        "id": "swimwear",
        "name": "Swimwear ×2",
        "note": "You'll swim almost every day",
        "priority": "critical", "category": "Clothing", "qty": 2,
        "retailers": {
            "decathlon": "swimwear swimming shorts",
            "amazon":    "quick dry swimwear",
            "zalando":   "swimwear",
        },
    },
    {
        "id": "flip_flops",
        "name": "Flip flops / sandals",
        "note": "Campsite showers and beach",
        "priority": "high", "category": "Clothing", "qty": 1,
        "retailers": {
            "decathlon": "flip flops",
            "amazon":    "flip flops sandals",
            "zalando":   "flip flops",
        },
    },
    {
        "id": "down_jacket",
        "name": "Light packable down jacket",
        "note": "Compact — for cold mornings",
        "priority": "high", "category": "Clothing", "qty": 1,
        "retailers": {
            "decathlon": "packable down jacket",
            "amazon":    "packable down jacket lightweight",
            "wiggle":    "packable down jacket",
            "zalando":   "packable down jacket",
        },
    },
    # ── FOOTWEAR ────────────────────────────────────────────────────────────
    {
        "id": "hiking_boots",
        "name": "Waterproof hiking boots",
        "note": "Salomon, Scarpa, or Merrell — break in before trip",
        "priority": "critical", "category": "Footwear", "qty": 1,
        "retailers": {
            "decathlon": "waterproof hiking boots",
            "amazon":    "Salomon waterproof hiking boots",
            "wiggle":    "waterproof hiking boots Salomon",
            "zalando":   "Salomon hiking boots waterproof",
        },
    },
    {
        "id": "trail_runners",
        "name": "Trail running shoes",
        "note": "Salomon or Merrell",
        "priority": "high", "category": "Footwear", "qty": 1,
        "retailers": {
            "decathlon": "trail running shoes",
            "amazon":    "Salomon trail running shoes",
            "wiggle":    "trail running shoes Salomon",
            "zalando":   "Salomon trail shoes",
        },
    },
    {
        "id": "camp_sandals",
        "name": "Camp sandals (Teva or Birkenstock)",
        "note": "After-hike comfort",
        "priority": "high", "category": "Footwear", "qty": 1,
        "retailers": {
            "amazon":  "Teva sandals",
            "zalando": "Teva sandals",
        },
    },
    # ── HIKING & OUTDOORS ───────────────────────────────────────────────────
    {
        "id": "daypack",
        "name": "Daypack 20–30L",
        "note": "Separate from main luggage bag",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "decathlon": "daypack 25L hiking",
            "amazon":    "daypack 25L hiking backpack",
            "wiggle":    "daypack 25L",
        },
    },
    {
        "id": "trekking_poles",
        "name": "Trekking poles (collapsible)",
        "note": "Essential for steep NZ descents",
        "priority": "high", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "decathlon": "collapsible trekking poles",
            "amazon":    "collapsible trekking poles hiking",
            "wiggle":    "trekking poles collapsible",
        },
    },
    {
        "id": "headlamp",
        "name": "Headlamp (USB rechargeable)",
        "note": "Night hikes and 3am toilet trips",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "decathlon": "USB rechargeable headlamp",
            "amazon":    "USB rechargeable headlamp hiking",
            "wiggle":    "rechargeable headlamp",
        },
    },
    {
        "id": "emergency_bivvy",
        "name": "Emergency bivvy bag (foil)",
        "note": "Mandatory for NZ alpine tracks",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "decathlon": "emergency bivvy bag survival",
            "amazon":    "emergency bivvy bag foil survival",
            "wiggle":    "emergency bivvy",
        },
    },
    {
        "id": "first_aid_kit",
        "name": "First aid kit (comprehensive hiking)",
        "note": "Blister kit, antiseptic, bandages",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "decathlon": "hiking first aid kit",
            "amazon":    "hiking first aid kit comprehensive",
        },
    },
    {
        "id": "sunscreen",
        "name": "Sunscreen SPF 50+ ×2",
        "note": "NZ has one of the world's highest UV indices",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 2,
        "retailers": {
            "amazon": "sunscreen SPF 50 sport water resistant",
            "bol":    "sunscreen SPF 50 sport",
        },
    },
    {
        "id": "sunglasses",
        "name": "Sunglasses UV400 polarised",
        "note": "Glacier and snow reflection",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "decathlon": "polarised sunglasses UV400 hiking",
            "amazon":    "polarised sunglasses UV400",
            "zalando":   "polarised sunglasses",
        },
    },
    {
        "id": "buff",
        "name": "Buff / neck gaiter",
        "note": "Sun protection and warmth",
        "priority": "high", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "decathlon": "buff neck gaiter",
            "amazon":    "Buff neck gaiter multifunctional",
            "wiggle":    "Buff neck gaiter",
        },
    },
    {
        "id": "water_bottle",
        "name": "Nalgene 1L wide-mouth water bottle",
        "note": "Also works as emergency hot-water bottle",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "decathlon": "1L wide mouth water bottle",
            "amazon":    "Nalgene 1L wide mouth",
            "wiggle":    "Nalgene wide mouth 1L",
        },
    },
    {
        "id": "water_filter",
        "name": "Water filter (Sawyer Squeeze or LifeStraw)",
        "note": "Drink from any NZ stream safely",
        "priority": "high", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "amazon": "Sawyer Squeeze water filter",
            "wiggle": "Sawyer Squeeze water filter",
        },
    },
    {
        "id": "dry_bags",
        "name": "Dry bags set (3 sizes)",
        "note": "Waterproof bags for electronics and clothes",
        "priority": "high", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "decathlon": "dry bag set waterproof",
            "amazon":    "waterproof dry bags set 3 sizes",
            "wiggle":    "dry bag set",
        },
    },
    {
        "id": "rain_trousers",
        "name": "Lightweight packable rain trousers",
        "note": "For exposed mountain tracks",
        "priority": "high", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "decathlon": "packable waterproof trousers hiking",
            "amazon":    "packable waterproof rain trousers",
            "wiggle":    "waterproof trousers hiking packable",
        },
    },
    {
        "id": "gaiters",
        "name": "Gaiters (low / trail)",
        "note": "For muddy NZ tracks",
        "priority": "normal", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "decathlon": "trail gaiters low",
            "amazon":    "trail gaiters low hiking",
            "wiggle":    "trail gaiters",
        },
    },
    {
        "id": "insect_repellent",
        "name": "Insect repellent DEET/Picaridin ×2",
        "note": "West Coast sandflies are vicious — non-negotiable",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 2,
        "retailers": {
            "amazon": "DEET insect repellent 50%",
            "bol":    "DEET insect repellent",
        },
    },
    # ── ELECTRONICS ─────────────────────────────────────────────────────────
    {
        "id": "power_bank",
        "name": "Power bank 20,000 mAh USB-C",
        "note": "Keep fully charged always",
        "priority": "critical", "category": "Electronics", "qty": 1,
        "retailers": {
            "amazon": "20000mAh power bank USB-C fast charge",
            "bol":    "20000mAh powerbank USB-C",
        },
    },
    {
        "id": "car_charger",
        "name": "12V USB car charger adaptor",
        "note": "Charges devices while driving",
        "priority": "critical", "category": "Electronics", "qty": 1,
        "retailers": {
            "amazon": "12V USB-C car charger fast charge",
            "bol":    "12V USB car charger USB-C",
        },
    },
    {
        "id": "travel_adaptor",
        "name": "Universal power adaptor Type I (NZ/AU)",
        "note": "NZ uses Type I plugs — 230V",
        "priority": "critical", "category": "Electronics", "qty": 1,
        "retailers": {
            "amazon": "universal travel adaptor Australia New Zealand Type I",
            "bol":    "universal travel adaptor Type I",
        },
    },
    {
        "id": "solar_panel",
        "name": "Portable solar panel 100W foldable",
        "note": "For van leisure battery",
        "priority": "high", "category": "Electronics", "qty": 1,
        "retailers": {
            "amazon": "portable solar panel 100W foldable",
            "bol":    "portable solar panel 100W foldable",
        },
    },
    {
        "id": "bluetooth_speaker",
        "name": "Waterproof Bluetooth speaker (JBL Flip)",
        "note": "JBL Flip or similar",
        "priority": "high", "category": "Electronics", "qty": 1,
        "retailers": {
            "amazon": "JBL Flip 6 waterproof Bluetooth speaker",
            "bol":    "JBL Flip Bluetooth speaker",
        },
    },
    {
        "id": "kindle",
        "name": "Kindle Paperwhite e-reader",
        "note": "Rain days and hut evenings",
        "priority": "high", "category": "Electronics", "qty": 1,
        "retailers": {
            "amazon": "Kindle Paperwhite e-reader",
            "bol":    "Kindle Paperwhite",
        },
    },
    {
        "id": "garmin_inreach",
        "name": "Garmin inReach Mini 2",
        "note": "Two-way messaging when off-grid — Great Walks",
        "priority": "normal", "category": "Electronics", "qty": 1,
        "retailers": {
            "amazon": "Garmin inReach Mini 2 satellite communicator",
            "wiggle": "Garmin inReach Mini",
        },
    },
    {
        "id": "headphones",
        "name": "Noise-cancelling headphones",
        "note": "Long drives and hostel nights",
        "priority": "high", "category": "Electronics", "qty": 1,
        "retailers": {
            "amazon":  "noise cancelling headphones wireless",
            "bol":     "noise cancelling headphones wireless",
            "zalando": "noise cancelling headphones",
        },
    },
    # ── TOILETRIES & HEALTH ─────────────────────────────────────────────────
    {
        "id": "microfibre_towel",
        "name": "Microfibre travel towel large ×2",
        "note": "Dries in 20 min",
        "priority": "critical", "category": "Toiletries & Health", "qty": 2,
        "retailers": {
            "decathlon": "microfibre travel towel large",
            "amazon":    "microfibre travel towel XL",
            "wiggle":    "microfibre travel towel",
        },
    },
    {
        "id": "castile_soap",
        "name": "Dr. Bronner's Castile soap 500ml ×2",
        "note": "Body wash + shampoo + laundry + dishes",
        "priority": "critical", "category": "Toiletries & Health", "qty": 2,
        "retailers": {
            "amazon": "Dr Bronner castile soap 500ml",
            "bol":    "Dr Bronner castile soap",
        },
    },
    {
        "id": "biodegradable_soap",
        "name": "Biodegradable soap Ecover ×2",
        "note": "Required for DOC campsites",
        "priority": "critical", "category": "Toiletries & Health", "qty": 2,
        "retailers": {
            "amazon": "Ecover biodegradable washing up liquid",
            "bol":    "Ecover biodegradable soap",
        },
    },
    {
        "id": "spf_moisturiser",
        "name": "SPF 50 daily face moisturiser ×2",
        "note": "NZ UV intense even on cloudy days",
        "priority": "critical", "category": "Toiletries & Health", "qty": 2,
        "retailers": {
            "amazon": "SPF 50 daily face moisturiser",
            "bol":    "face moisturiser SPF 50",
        },
    },
    {
        "id": "earplugs",
        "name": "Foam earplugs box of 50 pairs",
        "note": "Wind, campsite noise, snoring neighbours",
        "priority": "high", "category": "Toiletries & Health", "qty": 1,
        "retailers": {
            "amazon": "foam earplugs box 50 pairs NRR",
            "bol":    "foam earplugs 50 pairs",
        },
    },
    {
        "id": "eye_mask",
        "name": "Sleep eye mask",
        "note": "NZ summer evenings still bright at 9:30pm",
        "priority": "high", "category": "Toiletries & Health", "qty": 1,
        "retailers": {
            "amazon": "sleep eye mask contoured",
            "bol":    "sleep eye mask",
        },
    },
    {
        "id": "hydrocortisone",
        "name": "Hydrocortisone cream ×2",
        "note": "West Coast sandfly bites are intense",
        "priority": "high", "category": "Toiletries & Health", "qty": 2,
        "retailers": {
            "amazon": "hydrocortisone cream 1%",
            "bol":    "hydrocortisone cream bite relief",
        },
    },
    # ── MISCELLANEOUS ───────────────────────────────────────────────────────
    {
        "id": "padlock",
        "name": "TSA combination padlock ×2",
        "note": "Van security and hostel lockers",
        "priority": "high", "category": "Miscellaneous", "qty": 2,
        "retailers": {
            "amazon": "TSA combination padlock",
            "bol":    "TSA padlock combination",
        },
    },
    {
        "id": "laundry_bags",
        "name": "Mesh laundry bags ×2",
        "note": "Keep dirty and clean separated",
        "priority": "high", "category": "Miscellaneous", "qty": 2,
        "retailers": {
            "amazon": "mesh laundry bag set",
            "bol":    "mesh laundry bag",
        },
    },
    {
        "id": "sewing_kit",
        "name": "Travel sewing kit",
        "note": "Field repairs on gear",
        "priority": "normal", "category": "Miscellaneous", "qty": 1,
        "retailers": {
            "amazon": "travel sewing kit compact",
            "bol":    "travel sewing kit",
        },
    },
    {
        "id": "packable_tote",
        "name": "Packable tote bag",
        "note": "Supermarket shopping and farmers markets",
        "priority": "normal", "category": "Miscellaneous", "qty": 1,
        "retailers": {
            "amazon": "packable tote bag foldable",
            "bol":    "packable tote bag",
        },
    },
]

RETAILER_NAMES = {
    "decathlon": "Decathlon.be",
    "amazon":    "Amazon.de",
    "wiggle":    "Wiggle.com",
    "zalando":   "Zalando.be",
    "bol":       "Bol.com",
}
