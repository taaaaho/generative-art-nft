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
    "name": "LAG#_ID_",
    "description": "The ‘Love Addicted Girls with BIGLOVE’ (LAG) Collection is a wave of 4,000 Japanese-inspired unique digital exclusive collectibles made with love by the Soudan NFT community on the Ethereum blockchain. Your LAG NFT is your exclusive access to Soudan Exclusive Members-only partnerships, benefits, and perks.",
    "external_url": "https://soudan-nft.xyz/",
    "background_color": "FFFFFF",
    #    "youtube_url": ""
}

CONFIG = [
    {
        "id": 1,
        "name": "Background",
        "directory": "background",
        "required": True,
        "rarity_weights": [
            26,  # Blue PinStripe
            3,  # Celestial Moon
            1,  # CryptoMaids
            1,  # Golden Hour
            3,  # Lovely Lantern
            1,  # Moogie
            1,  # Morning Sun
            26,  # Pink Stripe
            26,  # Violet Stripe
            1,  # [R] Blue Pinstripe2
            1,  # [R] Pink Pinstripe2
            1,  # [R] Violet Pinstripe2
        ],
    },
    {
        "id": 2,
        "name": "Backhair",
        "directory": "backhair",
        "required": True,
        "rarity_weights": [
            10,  # Black Pigtails
            10,  # Blue Pigtails
            10,  # Bun
            10,  # Cafe Girl
            10,  # Gal
            10,  # Straight
            10,  # Wavy
            3,  # [R]Black Pigtails
            2,  # [R]Black Pigtails2
            2,  # [R]Blue Pigtails
            3,  # [R]Blue Pigtails2
            3,  # [R]Bun
            3,  # [R]Bun2
            3,  # [R]Cafe Girl
            1,  # [R]Cafe Girl2
            3,  # [R]Gal
            1,  # [R]Gal2
            3,  # [R]Straight
            2,  # [R]Straight2
            3,  # [R]Wavy
            1,  # [R]Wavy2
        ],
    },
    {
        "id": 3,
        "name": "Body",
        "directory": "body",
        "required": True,
        "rarity_weights": [
            5,  # Autumn Kimono
            5,  # Black Bikini
            5,  # Black Maid
            5,  # Blue Lolita
            5,  # Casual Black
            5,  # Casual Brown
            5,  # Casual Cream
            5,  # Casual Pink
            5,  # Dealeer Black
            5,  # Dealeer Blue
            5,  # Dealeer Red
            5,  # Dealer White
            5,  # Festival Kimono
            2,  # Harness
            5,  # Pink Lolita
            5,  # Red Maid
            5,  # School Brown
            5,  # School Gray
            5,  # Studded Bikini
            1,  # Succubus
            3,  # [R]Black Maid
            1,  # [R]Blue Lolita
            2,  # [R]Card Dealder Black
            2,  # [R]Card Dealer White
            1,  # [R]Casual Brown
            1,  # [R]Casual Cream
            3,  # [R]Kimono rose
            3,  # [R]Kimono sakura
            3,  # [R]Kimono
            1,  # [R]Pink Lolita
            2,  # [R]Red Maid
            3,  # [R]School Brown
            3,  # [R]School Gray
            2,  # [R]Studded Bikini
        ],
    },
    {
        "id": 4,
        "name": "Face",
        "directory": "face",
        "required": True,
        "rarity_weights": [
            12,  # Cat
            12,  # Confident
            12,  # Coy
            12,  # Flirty
            3,  # Heterochromia
            3,  # Miss Secretary
            12,  # Pretty Please
            12,  # Purple Gal
            12,  # Wink
            3,  # [R]Coy
            1,  # [R]Heterochromia
        ],
    },
    {
        "id": 5,
        "name": "Fronthair",
        "directory": "fronthair",
        "required": True,
        "rarity_weights": None,
        "link": {
            "[R]Black Pigtails.png": "[R]Black Pigtails.png",
            "[R]Black Pigtails2.png": "[R]Black Pigtails2.png",
            "[R]Blue Pigtails.png": "[R]Blue Pigtails.png",
            "[R]Blue Pigtails2.png": "[R]Blue Pigtails2.png",
            "[R]Bun.png": "[R]Bun.png",
            "[R]Bun2.png": "[R]Bun2.png",
            "[R]Cafe Girl.png": "[R]Cafe Girl.png",
            "[R]Cafe Girl2.png": "[R]Cafe Girl2.png",
            "[R]Gal.png": "[R]Gal.png",
            "[R]Gal2.png": "[R]Gal2.png",
            "[R]Straight.png": "[R]Straight.png",
            "[R]Straight2.png": "[R]Straight2.png",
            "[R]Wavy.png": "[R]Wavy.png",
            "[R]Wavy2.png": "[R]Wavy2.png",
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
