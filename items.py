# Trackable items extracted from the NZ Van Life Packing Checklist.
# Excludes: Documents & Admin (can't buy online), Van Equipment (buy in Auckland).
#
# Retailers:
#   idealo   → Idealo.be  (aggregates Decathlon, Bol, Amazon.de, Zalando, etc.)
#   amazon   → Amazon.de  (direct fallback for branded electronics)

ITEMS = [
    # ── CLOTHING ────────────────────────────────────────────────────────────
    {
        "id": "merino_tshirt",
        "name": "Merino wool t-shirt ×3",
        "note": "Icebreaker, Macpac, or Kathmandu",
        "priority": "critical", "category": "Clothing", "qty": 3,
        "retailers": {
            "idealo":   "Icebreaker merino t-shirt",
            "amazon":   "Icebreaker merino wool t-shirt men",
        },
    },
    {
        "id": "merino_longsleeve",
        "name": "Merino long-sleeve top ×2",
        "note": "Base layer + mid-layer",
        "priority": "critical", "category": "Clothing", "qty": 2,
        "retailers": {
            "idealo":   "Icebreaker merino long sleeve top",
            "amazon":   "Icebreaker merino long sleeve base layer",
        },
    },
    {
        "id": "fleece_jacket",
        "name": "Fleece mid-layer jacket",
        "note": "Patagonia or Macpac",
        "priority": "critical", "category": "Clothing", "qty": 1,
        "retailers": {
            "idealo":   "Patagonia fleece jacket",
            "amazon":   "Patagonia fleece jacket men",
        },
    },
    {
        "id": "rain_jacket",
        "name": "Waterproof rain jacket (hardshell)",
        "note": "Non-negotiable for NZ weather",
        "priority": "critical", "category": "Clothing", "qty": 1,
        "retailers": {
            "idealo":   "hardshell waterproof rain jacket hiking",
            "amazon":   "hardshell waterproof jacket hiking men",
        },
    },
    {
        "id": "hiking_trousers",
        "name": "Quick-dry hiking trousers ×2",
        "note": "Synthetic — no jeans",
        "priority": "critical", "category": "Clothing", "qty": 2,
        "retailers": {
            "idealo":   "quick dry hiking trousers",
            "amazon":   "quick dry hiking trousers men",
        },
    },
    {
        "id": "casual_trousers",
        "name": "Casual trousers / jeans",
        "note": "For town days",
        "priority": "high", "category": "Clothing", "qty": 1,
        "retailers": {
            "idealo":   "slim fit chino trousers men",
        },
    },
    {
        "id": "merino_underwear",
        "name": "Merino underwear ×10",
        "note": "Merino if possible",
        "priority": "critical", "category": "Clothing", "qty": 10,
        "retailers": {
            "idealo":   "Icebreaker merino underwear",
            "amazon":   "merino wool underwear men",
        },
    },
    {
        "id": "merino_socks",
        "name": "Merino hiking socks ×10 pairs",
        "note": "SmartWool or Darn Tough",
        "priority": "critical", "category": "Clothing", "qty": 10,
        "retailers": {
            "idealo":   "SmartWool hiking socks merino",
            "amazon":   "SmartWool hiking socks",
        },
    },
    {
        "id": "thermal_base",
        "name": "Thermal base layer set (top + bottom)",
        "note": "Essential for South Island winter",
        "priority": "critical", "category": "Clothing", "qty": 1,
        "retailers": {
            "idealo":   "thermal base layer set top bottom",
            "amazon":   "thermal base layer set men",
        },
    },
    {
        "id": "beanie",
        "name": "Warm beanie",
        "note": "Merino ideal",
        "priority": "high", "category": "Clothing", "qty": 1,
        "retailers": {
            "idealo":   "merino wool beanie hat",
            "amazon":   "merino wool beanie",
        },
    },
    {
        "id": "liner_gloves",
        "name": "Lightweight merino liner gloves",
        "priority": "high", "category": "Clothing", "qty": 1,
        "retailers": {
            "idealo":   "merino liner gloves thin",
            "amazon":   "merino liner gloves",
        },
    },
    {
        "id": "swimwear",
        "name": "Swimwear ×2",
        "note": "You'll swim almost every day",
        "priority": "critical", "category": "Clothing", "qty": 2,
        "retailers": {
            "idealo":   "quick dry swim shorts",
        },
    },
    {
        "id": "flip_flops",
        "name": "Flip flops / sandals",
        "note": "Campsite showers and beach",
        "priority": "high", "category": "Clothing", "qty": 1,
        "retailers": {
            "idealo":   "flip flops sandals men",
        },
    },
    {
        "id": "down_jacket",
        "name": "Light packable down jacket",
        "note": "Compact — for cold mornings",
        "priority": "high", "category": "Clothing", "qty": 1,
        "retailers": {
            "idealo":   "packable down jacket lightweight",
            "amazon":   "packable down jacket men",
        },
    },
    # ── FOOTWEAR ────────────────────────────────────────────────────────────
    {
        "id": "hiking_boots",
        "name": "Waterproof hiking boots",
        "note": "Salomon, Scarpa, or Merrell — break in before trip",
        "priority": "critical", "category": "Footwear", "qty": 1,
        "retailers": {
            "idealo":   "Salomon waterproof hiking boots",
            "amazon":   "Salomon waterproof hiking boots men",
        },
    },
    {
        "id": "trail_runners",
        "name": "Trail running shoes",
        "note": "Salomon or Merrell",
        "priority": "high", "category": "Footwear", "qty": 1,
        "retailers": {
            "idealo":   "Salomon trail running shoes",
            "amazon":   "Salomon trail running shoes men",
        },
    },
    {
        "id": "camp_sandals",
        "name": "Camp sandals (Teva or Birkenstock)",
        "note": "After-hike comfort",
        "priority": "high", "category": "Footwear", "qty": 1,
        "retailers": {
            "idealo":   "Teva sandals",
            "amazon":   "Teva sandals men",
        },
    },
    # ── HIKING & OUTDOORS ───────────────────────────────────────────────────
    {
        "id": "daypack",
        "name": "Daypack 20–30L",
        "note": "Separate from main luggage bag",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "daypack 25L hiking backpack",
            "amazon":   "daypack 25L hiking backpack",
        },
    },
    {
        "id": "trekking_poles",
        "name": "Trekking poles (collapsible)",
        "note": "Essential for steep NZ descents",
        "priority": "high", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "collapsible trekking poles aluminium",
            "amazon":   "collapsible trekking poles hiking",
        },
    },
    {
        "id": "headlamp",
        "name": "Headlamp (USB rechargeable)",
        "note": "Night hikes and 3am toilet trips",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "USB rechargeable headlamp hiking",
            "amazon":   "USB rechargeable headlamp",
        },
    },
    {
        "id": "emergency_bivvy",
        "name": "Emergency bivvy bag (foil)",
        "note": "Mandatory for NZ alpine tracks",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "emergency bivvy bag foil survival",
            "amazon":   "emergency bivvy bag survival foil",
        },
    },
    {
        "id": "first_aid_kit",
        "name": "First aid kit (comprehensive hiking)",
        "note": "Blister kit, antiseptic, bandages",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "hiking first aid kit comprehensive",
            "amazon":   "hiking first aid kit",
        },
    },
    {
        "id": "sunscreen",
        "name": "Sunscreen SPF 50+ ×2",
        "note": "NZ has one of the world's highest UV indices",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 2,
        "retailers": {
            "idealo":   "sunscreen SPF 50 sport water resistant",
            "amazon":   "sunscreen SPF 50 sport",
        },
    },
    {
        "id": "sunglasses",
        "name": "Sunglasses UV400 polarised",
        "note": "Glacier and snow reflection",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "polarised sunglasses UV400 hiking",
            "amazon":   "polarised sunglasses UV400",
        },
    },
    {
        "id": "buff",
        "name": "Buff / neck gaiter",
        "note": "Sun protection and warmth",
        "priority": "high", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "Buff neck gaiter multifunctional",
            "amazon":   "Buff neck gaiter",
        },
    },
    {
        "id": "water_bottle",
        "name": "Nalgene 1L wide-mouth water bottle",
        "note": "Also works as emergency hot-water bottle",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "Nalgene 1L wide mouth water bottle",
            "amazon":   "Nalgene 1L wide mouth",
        },
    },
    {
        "id": "water_filter",
        "name": "Water filter (Sawyer Squeeze or LifeStraw)",
        "note": "Drink from any NZ stream safely",
        "priority": "high", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "Sawyer Squeeze water filter",
            "amazon":   "Sawyer Squeeze water filter",
        },
    },
    {
        "id": "dry_bags",
        "name": "Dry bags set (3 sizes)",
        "note": "Waterproof bags for electronics and clothes",
        "priority": "high", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "waterproof dry bags set",
            "amazon":   "waterproof dry bags set 3 sizes",
        },
    },
    {
        "id": "rain_trousers",
        "name": "Lightweight packable rain trousers",
        "note": "For exposed mountain tracks",
        "priority": "high", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "packable waterproof rain trousers hiking",
            "amazon":   "packable waterproof rain trousers",
        },
    },
    {
        "id": "gaiters",
        "name": "Gaiters (low / trail)",
        "note": "For muddy NZ tracks",
        "priority": "normal", "category": "Hiking & Outdoors", "qty": 1,
        "retailers": {
            "idealo":   "trail gaiters low hiking",
            "amazon":   "low trail gaiters",
        },
    },
    {
        "id": "insect_repellent",
        "name": "Insect repellent DEET/Picaridin ×2",
        "note": "West Coast sandflies are vicious — non-negotiable",
        "priority": "critical", "category": "Hiking & Outdoors", "qty": 2,
        "retailers": {
            "idealo":   "DEET insect repellent 50%",
            "amazon":   "DEET insect repellent 50%",
        },
    },
    # ── ELECTRONICS ─────────────────────────────────────────────────────────
    {
        "id": "power_bank",
        "name": "Power bank 20,000 mAh USB-C",
        "note": "Keep fully charged always",
        "priority": "critical", "category": "Electronics", "qty": 1,
        "retailers": {
            "idealo":   "20000mAh power bank USB-C",
            "amazon":   "20000mAh power bank USB-C fast charge",
        },
    },
    {
        "id": "car_charger",
        "name": "12V USB car charger adaptor",
        "note": "Charges devices while driving",
        "priority": "critical", "category": "Electronics", "qty": 1,
        "retailers": {
            "idealo":   "12V USB-C car charger",
            "amazon":   "12V USB-C car charger fast charge",
        },
    },
    {
        "id": "travel_adaptor",
        "name": "Universal power adaptor Type I (NZ/AU)",
        "note": "NZ uses Type I plugs — 230V",
        "priority": "critical", "category": "Electronics", "qty": 1,
        "retailers": {
            "idealo":   "universal travel adaptor Australia New Zealand",
            "amazon":   "universal travel adaptor Type I Australia",
        },
    },
    {
        "id": "solar_panel",
        "name": "Portable solar panel 100W foldable",
        "note": "For van leisure battery",
        "priority": "high", "category": "Electronics", "qty": 1,
        "retailers": {
            "idealo":   "portable foldable solar panel 100W",
            "amazon":   "portable solar panel 100W foldable",
        },
    },
    {
        "id": "bluetooth_speaker",
        "name": "Waterproof Bluetooth speaker (JBL Flip)",
        "note": "JBL Flip or similar",
        "priority": "high", "category": "Electronics", "qty": 1,
        "retailers": {
            "idealo":   "JBL Flip 6 waterproof Bluetooth speaker",
            "amazon":   "JBL Flip 6 Bluetooth speaker",
        },
    },
    {
        "id": "kindle",
        "name": "Kindle Paperwhite e-reader",
        "note": "Rain days and hut evenings",
        "priority": "high", "category": "Electronics", "qty": 1,
        "retailers": {
            "idealo":   "Kindle Paperwhite",
            "amazon":   "Kindle Paperwhite",
        },
    },
    {
        "id": "garmin_inreach",
        "name": "Garmin inReach Mini 2",
        "note": "Two-way messaging when off-grid — Great Walks",
        "priority": "normal", "category": "Electronics", "qty": 1,
        "retailers": {
            "idealo":   "Garmin inReach Mini 2",
            "amazon":   "Garmin inReach Mini 2 satellite communicator",
        },
    },
    {
        "id": "headphones",
        "name": "Noise-cancelling headphones",
        "note": "Long drives and hostel nights",
        "priority": "high", "category": "Electronics", "qty": 1,
        "retailers": {
            "idealo":   "noise cancelling headphones wireless",
            "amazon":   "noise cancelling headphones wireless",
        },
    },
    # ── TOILETRIES & HEALTH ─────────────────────────────────────────────────
    {
        "id": "microfibre_towel",
        "name": "Microfibre travel towel large ×2",
        "note": "Dries in 20 min",
        "priority": "critical", "category": "Toiletries & Health", "qty": 2,
        "retailers": {
            "idealo":   "microfibre travel towel large XL",
            "amazon":   "microfibre travel towel XL",
        },
    },
    {
        "id": "castile_soap",
        "name": "Dr. Bronner's Castile soap 500ml ×2",
        "note": "Body wash + shampoo + laundry + dishes",
        "priority": "critical", "category": "Toiletries & Health", "qty": 2,
        "retailers": {
            "idealo":   "Dr Bronner castile soap 500ml",
            "amazon":   "Dr Bronner castile soap 500ml",
        },
    },
    {
        "id": "biodegradable_soap",
        "name": "Biodegradable soap Ecover ×2",
        "note": "Required for DOC campsites",
        "priority": "critical", "category": "Toiletries & Health", "qty": 2,
        "retailers": {
            "idealo":   "Ecover biodegradable washing up liquid",
            "amazon":   "Ecover biodegradable soap",
        },
    },
    {
        "id": "spf_moisturiser",
        "name": "SPF 50 daily face moisturiser ×2",
        "note": "NZ UV intense even on cloudy days",
        "priority": "critical", "category": "Toiletries & Health", "qty": 2,
        "retailers": {
            "idealo":   "face moisturiser SPF 50 daily",
            "amazon":   "SPF 50 daily face moisturiser",
        },
    },
    {
        "id": "earplugs",
        "name": "Foam earplugs box of 50 pairs",
        "note": "Wind, campsite noise, snoring neighbours",
        "priority": "high", "category": "Toiletries & Health", "qty": 1,
        "retailers": {
            "idealo":   "foam earplugs box 50 pairs",
            "amazon":   "foam earplugs box 50 pairs NRR",
        },
    },
    {
        "id": "eye_mask",
        "name": "Sleep eye mask",
        "note": "NZ summer evenings still bright at 9:30pm",
        "priority": "high", "category": "Toiletries & Health", "qty": 1,
        "retailers": {
            "idealo":   "sleep eye mask contoured",
            "amazon":   "sleep eye mask",
        },
    },
    {
        "id": "hydrocortisone",
        "name": "Hydrocortisone cream ×2",
        "note": "West Coast sandfly bites are intense",
        "priority": "high", "category": "Toiletries & Health", "qty": 2,
        "retailers": {
            "idealo":   "hydrocortisone cream 1% bite relief",
            "amazon":   "hydrocortisone cream 1%",
        },
    },
    # ── MISCELLANEOUS ───────────────────────────────────────────────────────
    {
        "id": "padlock",
        "name": "TSA combination padlock ×2",
        "note": "Van security and hostel lockers",
        "priority": "high", "category": "Miscellaneous", "qty": 2,
        "retailers": {
            "idealo":   "TSA combination padlock",
            "amazon":   "TSA combination padlock",
        },
    },
    {
        "id": "laundry_bags",
        "name": "Mesh laundry bags ×2",
        "note": "Keep dirty and clean separated",
        "priority": "high", "category": "Miscellaneous", "qty": 2,
        "retailers": {
            "idealo":   "mesh laundry bag set",
            "amazon":   "mesh laundry bag",
        },
    },
    {
        "id": "sewing_kit",
        "name": "Travel sewing kit",
        "note": "Field repairs on gear",
        "priority": "normal", "category": "Miscellaneous", "qty": 1,
        "retailers": {
            "idealo":   "travel sewing kit compact",
            "amazon":   "travel sewing kit",
        },
    },
    {
        "id": "packable_tote",
        "name": "Packable tote bag",
        "note": "Supermarket shopping and farmers markets",
        "priority": "normal", "category": "Miscellaneous", "qty": 1,
        "retailers": {
            "idealo":   "packable foldable tote bag",
            "amazon":   "packable tote bag foldable",
        },
    },
]

RETAILER_NAMES = {
    "idealo": "Idealo.be",
    "amazon": "Amazon.de",
}
