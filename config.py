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
    "output": "csv"
}

METADATA = {
    "name": "METAKOZO#_ID_",
    "description": "MetaKozo sample description",
    "external_url": "https://metakozo-nft.xyz",
    "background_color": "FFFFFF",
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
    # {
    #     "id": 2,
    #     "name": "back_object",
    #     "directory": "2-back_object",
    #     "required": False,
    #     "rarity_weights": None,
    # },
    {
        "id": 3,
        "name": "body",
        "directory": "3-body",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 4,
        "name": "clothes",
        "directory": "4-clothes",
        "required": False,
        "rarity_weights": None,
    },
    {
        "id": 5,
        "name": "head",
        "directory": "5-head",
        "required": True,
        "rarity_weights": None,
        "link": {
            "body_brown.png": "head_brown.png",
            "body_white.png": "head_white.png",
            "body.png": "head.png",
        },
    },
    {
        "id": 6,
        "name": "eyes",
        "directory": "6-eyes",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 7,
        "name": "mouth",
        "directory": "7-mouth",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 8,
        "name": "nose",
        "directory": "8-nose",
        "required": True,
        "rarity_weights": None,
        "link": {
            "body_brown.png": "nose_brown.png",
            "body_white.png": "nose_white.png",
            "body.png": "nose.png",
        },
    },
    {
        "id": 9,
        "name": "hair",
        "directory": "9-hair",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 10,
        "name": "face_object",
        "directory": "10-face_object",
        "required": False,
        "rarity_weights": None,
        "remove": ['eyes'],
    },
    {
        "id": 11,
        "name": "ear",
        "directory": "11-ear",
        "required": True,
        "rarity_weights": None,
        "link": {
            "body_brown.png": "ear_brown.png",
            "body_white.png": "ear_white.png",
            "body.png": "ear.png",
        },
    },
    {
        "id": 12,
        "name": "head_object",
        "directory": "12-head_object",
        "required": False,
        "rarity_weights": None,
    },
    {
        "id": 13,
        "name": "hand_object",
        "directory": "13-hand_object",
        "required": False,
        "rarity_weights": None,
    },
    {
        "id": 14,
        "name": "object",
        "directory": "14-object",
        "required": False,
        "rarity_weights": None,
    },
    # {
    #     "id": 15,
    #     "name": "nose",
    #     "directory": "nose",
    #     "required": True,
    #     "rarity_weights": None,
    # },
    # {
    #     "id": 16,
    #     "name": "object",
    #     "directory": "object",
    #     "required": True,
    #     "rarity_weights": None,
    # },
]
