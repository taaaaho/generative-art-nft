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
    "output": "json",
    "start_seq": 0
}

METADATA = {
    "name": "METAKO#_ID_",
    "description": "Meta sample description",
    "external_url": "https://meta-nft.xyz",
    # "background_color": "FFFFFF",
    #    "youtube_url": ""
}

CONFIG = [
    {
        "id": 1,
        "name": "background",
        "directory": "1-background",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 2,
        "name": "body",
        "directory": "2-body",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 3,
        "name": "clothes",
        "directory": "3-clothes",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 4,
        "name": "head",
        "directory": "4-head",
        "required": True,
        "rarity_weights": None,
        "link": {
            "TypeA.png": "TypeA.png",
            "TypeB.png": "TypeB.png",
            "TypeC.png": "TypeC.png",
        },
    },
    {
        "id": 5,
        "name": "eyes",
        "directory": "5-eyes",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 6,
        "name": "mouth",
        "directory": "6-mouth",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 7,
        "name": "nose",
        "directory": "7-nose",
        "required": True,
        "rarity_weights": None,
        "link": {
            "TypeA.png": "TypeA.png",
            "TypeB.png": "TypeB.png",
            "TypeC.png": "TypeC.png",
        },
    },
    {
        "id": 8,
        "name": "hair",
        "directory": "8-hair",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 9,
        "name": "face_accessory",
        "directory": "9-face_accessory",
        "required": False,
        "rarity_weights": None,
        "remove": ['eyes'],
    },
    {
        "id": 10,
        "name": "ear",
        "directory": "10-ear",
        "required": True,
        "rarity_weights": None,
        "link": {
            "TypeA.png": "TypeA.png",
            "TypeB.png": "TypeB.png",
            "TypeC.png": "TypeC.png",
        },
    },
    {
        "id": 11,
        "name": "head_accessory",
        "directory": "11-head_accessory",
        "required": False,
        "rarity_weights": None,
    },
    {
        "id": 12,
        "name": "hand_item",
        "directory": "12-hand_item",
        "required": False,
        "rarity_weights": None,
    },
    {
        "id": 13,
        "name": "attached",
        "directory": "13-attached",
        "required": False,
        "rarity_weights": None,
    },
]
