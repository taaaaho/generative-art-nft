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

METADATA = {
    "name": "Love Addicted Girl #_ID_",
    "description": "2000 Generative NFT collection",
    "external_url": "https://soudan-nft.xyz/",
    "background_color": "000000",
    #    "youtube_url": ""
}

CONFIG = [
    {
        "id": 1,
        "name": "Background",
        "directory": "background",
        "required": True,
        "rarity_weights": [300,  # Blue
                           30,  # Celestial Moon
                           30,  # Maids
                           5,  # Golden Hour
                           30,  # Lovely Lantern
                           5,  # Morning Sun
                           300,  # Pink Stripe
                           300  # Violet Stripe
                           ],
    },
    {
        "id": 2,
        "name": "Backhair",
        "directory": "backhair",
        "required": True,
        "rarity_weights": None,
    },
    {
        "id": 3,
        "name": "Body",
        "directory": "body",
        "required": True,
        "rarity_weights": [
            8,  # Autumn Kimono
            8,  # Black Bikini
            8,  # Black Maid
            8,  # Blue Lolita
            8,  # Casual Brown
            8,  # Casual Black
            8,  # Dealder Black
            8,  # Dealer White
            8,  # Festival Kimono
            8,  # Pink Lolita
            8,  # Red Maid
            8,  # Studded Bikini
            3,  # Succubus
            1  # Wedding doress
        ],
    },
    {
        "id": 4,
        "name": "Face",
        "directory": "face",
        "required": True,
        "rarity_weights": [5,  # Confident
                           5,  # Coy
                           5,  # Flirty
                           5,  # Gal
                           1,  # Heterochromia
                           5,  # Pretty Please
                           5  # Wink
                           ],
    },
    {
        "id": 5,
        "name": "Fronthair",
        "directory": "hair",
        "required": True,
        "rarity_weights": None,
        "link": {
            "Black Pigtails.png": "Black Pigtails.png",
            "Blue Pigtails.png": "Blue Pigtails.png",
            "Bun.png": "Bun.png",
            "Cafe Girl.png": "Cafe Girl.png",
            "Gal.png": "Gal.png",
            "Straight.png": "Straight.png",
            "Wavy.png": "Wavy.png",
        },
    },
]
