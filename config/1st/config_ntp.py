METACONFIG = {
    "output": "json",
    "start_seq": 0,
    "assets_path": "assets/10.NTP",
}

METADATA = {
    "name": "METAKOZO#_ID_",
    "description": "Hey, Let's hang out!",
    "external_url": "https://metakozo-dao.xyz/",
}

CONFIG = [
    {
        "id": 10,
        "name": "background",
        "directory": "10-background",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 20,
        "name": "body",
        "directory": "20-body",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 30,
        "name": "clothes",
        "directory": "30-clothes",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 40,
        "name": "head",
        "directory": "40-head",
        "required": True,
        "rarity_weights": None,
        "link": {
            "TypeA.png": "TypeA.png",
            "TypeB.png": "TypeB.png",
            "TypeC.png": "TypeC.png",
        },
    },
    {
        "id": 50,
        "name": "eyes",
        "directory": "50-eyes",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 60,
        "name": "mouth",
        "directory": "60-mouth",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 70,
        "name": "nose",
        "directory": "70-nose",
        "required": True,
        "rarity_weights": None,
        "link": {
            "TypeA.png": "TypeA.png",
            "TypeB.png": "TypeB.png",
            "TypeC.png": "TypeC.png",
        },
    },
    {
        "id": 80,
        "name": "hair",
        "directory": "80-hair",
        "required": True,
        "rarity_weights": None,
    },
    # {
    #     "id": 90,
    #     "name": "face_accessory",
    #     "directory": "90-face_accessory",
    #     "required": False,
    #     "rarity_weights": None,
    #     "remove": ['eyes'],
    # },
    {
        "id": 100,
        "name": "ear",
        "directory": "100-ear",
        "required": True,
        "rarity_weights": None,
        "link": {
            "TypeA.png": "TypeA.png",
            "TypeB.png": "TypeB.png",
            "TypeC.png": "TypeC.png",
        },
    },
    {
        "id": 110,
        "name": "head_accessory",
        "directory": "110-head_accessory",
        "required": True,
        "rarity_weights": None
    },
]
