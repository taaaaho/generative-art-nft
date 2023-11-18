# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder.
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random.
#       - array: An array of numbers where each number represents a weight.
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.

METACONFIG = {
    "output": "csv",
    "start_seq": 0,
    "assets_path": "assets/2nd/angel",
}

METADATA = {
    "name": "METAKOZO MONSETRS#_ID_",
    "description": "MetaKozo by MetaKoZoDao(MKD)\n\nThe first commerative collection published by MKD.\n\nHolders will receive the right of access to MKD's future projects and physical events.\nFor more information on MKD and MetaKozo, please visit https://www.metakozo-dao.xyz/",
    "external_url": "https://metakozo-dao.xyz/",
}

CONFIG = [
    {
        "id": 10,
        "name": "Background",
        "directory": "Background",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 15,
        "name": "Background_Item",
        "directory": "Background_Item",
        "required": False,
        "rarity_weights":None,
    },
    {
        "id": 20,
        "name": "Body",
        "directory": "Body",
        "required": True,
        "rarity_weights": None
    },
    {
        "id": 30,
        "name": "Clothes",
        "directory": "Clothes",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 40,
        "name": "Head",
        "directory": "Head",
        "required": True,
        "rarity_weights": None,
        "link": {
            "Angel_TypeA.png": "Angel_TypeA.png",
        },
    },
    {
        "id": 50,
        "name": "Eyes",
        "directory": "Eyes",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 60,
        "name": "Mouth",
        "directory": "Mouth",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 70,
        "name": "Nose",
        "directory": "Nose",
        "required": True,
        "rarity_weights": None,
        "link": {
            "Angel_TypeA.png": "Angel_TypeA.png",
        },
    },
    {
        "id": 80,
        "name": "Hair",
        "directory": "Hair",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 90,
        "name": "Face_Accessory",
        "directory": "Face_Accessory",
        "required": False,
        "rarity_weights": None,
        "remove": ['Eyes'],
    },
    {
        "id": 100,
        "name": "Ear",
        "directory": "Ear",
        "required": True,
        "rarity_weights": None,
        "link": {
            "Angel_TypeA.png": "Angel_TypeA.png",
        },
    },
    {
        "id": 110,
        "name": "Head_Accessory",
        "directory": "Head_Accessory",
        "required": False,
        "rarity_weights": None,
    },
    {
        "id": 120,
        "name": "Hand_Item",
        "directory": "Hand_Item",
        "required": False,
        "rarity_weights": None,
    },
    {
        "id": 130,
        "name": "Favorite_Things",
        "directory": "Favorite_Things",
        "required": False,
        "rarity_weights":None,
    },
    {
        "id": 133,
        "name": "Doji",
        "directory": "Doji",
        "required": False,
        "rarity_weights": None,
    },
    {
        "id": 134,
        "name": "Buddy",
        "directory": "Buddy",
        "required": False,
        "rarity_weights": None,
    },
    {
        "id": 140,
        "name": "Personality",
        "directory": "Personality",
        "required": True,
        "rarity_weights": None,
    },
]
