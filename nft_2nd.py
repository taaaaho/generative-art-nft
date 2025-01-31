#!/usr/bin/env python
# coding: utf-8

# Import required libraries
import json
from typing import Type
# from config.config_zombie import CONFIG, METADATA, METACONFIG
from config.config_hero import CONFIG, METADATA, METACONFIG
from PIL import Image
import pandas as pd
import numpy as np
import time
import os
import random
from pandas.core.base import DataError
from pandas.core.frame import DataFrame
from progressbar import progressbar
import math

import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)


# Import configuration file

# Parse the configuration file and make sure it's valid
image_extention = '.png'


def parse_config():

    # Input traits must be placed in the assets folder. Change this value if you want to name it something else.
    assets_path = METACONFIG['assets_path']

    # Loop through all layers defined in CONFIG
    for layer in CONFIG:

        # Go into assets/ to look for layer folders
        layer_path = os.path.join(assets_path, layer["directory"])
        # Get trait array in sorted order
        traits = sorted(
            [trait for trait in os.listdir(layer_path) if trait[0] != "."])
        print(traits)

        # Generate final rarity weights
        if layer["rarity_weights"] is None:
            rarities = [1 for x in traits]
        elif layer["rarity_weights"] == "random":
            rarities = [random.random() for x in traits]
        elif type(layer["rarity_weights"] == "list"):
            assert len(traits) == len(
                layer["rarity_weights"]
            ), "Make sure you have the current number of rarity weights"
            rarities = layer["rarity_weights"]
        else:
            raise ValueError("Rarity weights is invalid")

        rarities = get_weighted_rarities(rarities)
        print('rarities')
        print(rarities)

        # Re-assign final values to main CONFIG
        layer["rarity_weights"] = rarities
        layer["cum_rarity_weights"] = np.cumsum(rarities)
        layer["traits"] = traits


# Weight rarities and return a numpy array that sums up to 1
def get_weighted_rarities(arr):
    return np.array(arr) / sum(arr)


# Generate a single image given an array of filepaths representing layers
def generate_single_image(filepaths, output_filename=None):
    assets_path = METACONFIG['assets_path']

    # Treat the first layer as the background
    bg = Image.open(os.path.join(assets_path, filepaths[0]))

    # Loop through layers 1 to n and stack them on top of another
    for filepath in filepaths[1:]:
        if filepath.endswith(".png"):
            img = Image.open(os.path.join(assets_path, filepath))
            bg.paste(img, (0, 0), img)

    # Save the final image into desired location
    if output_filename is not None:
        if image_extention != '.png':
            rgb_im = bg.convert('RGB')
            rgb_im.save(output_filename)
        else:
            rgb_im = bg.convert('RGB')
            rgb_im.save(output_filename)
    else:
        # If output filename is not specified, use timestamp to name the image and save it in output/single_images
        if not os.path.exists(os.path.join("output", "single_images")):
            os.makedirs(os.path.join("output", "single_images"))
        bg.save(os.path.join("output", "single_images",
                str(int(time.time())) + ".png"))


# Get total number of distinct possible combinations
def get_total_combinations() -> int:

    total = 1
    for layer in CONFIG:
        total = total * len(layer["traits"])
    return total


# Select an index based on rarity weights
def select_index(cum_rarities, rand):

    cum_rarities = [0] + list(cum_rarities)
    for i in range(len(cum_rarities) - 1):
        if rand >= cum_rarities[i] and rand <= cum_rarities[i + 1]:
            return i

    # Should not reach here if everything works okay
    return None


def get_link_value(linklist, trait_set):
    for link in linklist.keys():
        if link in trait_set:
            return linklist[link]
    print(linklist)
    print(trait_set)
    raise Exception("linklist don't find in trait_set")


# Generate a set of traits given rarities
def generate_trait_set_from_config():

    trait_set = []
    trait_paths = []

    for layer in CONFIG:
        # Extract list of traits and cumulative rarity weights
        traits, cum_rarities = layer["traits"], layer["cum_rarity_weights"]

        # Generate a random number
        rand_num = random.random()

        # Select an element index based on random number and cumulative rarity weights
        idx = select_index(cum_rarities, rand_num)
        try:
            if layer["link"]:
                trait_value = get_link_value(layer["link"], trait_set)
                trait_set.append(trait_value)
                trait_path = os.path.join(layer["directory"], trait_value)
                trait_paths.append(trait_path)
        except KeyError:
            # Add selected trait to trait set
            trait_set.append(traits[idx])

            # Add trait path to trait paths if the trait has been selected
            if traits[idx] is not None:
                trait_path = os.path.join(layer["directory"], traits[idx])
                trait_paths.append(trait_path)
        # try:
        #     if idx != 0 and layer["remove"] and traits[idx] != 'None.png':
        #         for l in layer["remove"]:
        #             trait_set = [i if not (trait_set[5] in i)
        #                          else 'Normal' for i in trait_set]
        #             trait_paths = [i if not (trait_paths[5] in i)
        #                            else 'Normal' for i in trait_paths]
        # except KeyError:
        #     pass
        # except TypeError:
        #     pass

    return trait_set, trait_paths


def generate_images(edition: str, count: int) -> DataFrame:
    """Generate Images from rarity table"""
    # Initialize an empty rarity table
    rarity_table = {}
    for layer in CONFIG:
        rarity_table[layer["name"]] = []

    # Define output path to output/edition {edition_num}
    op_path = os.path.join("output", "edition_" + str(edition), "images")

    # Will require this to name final images as 000, 001,...
    zfill_count = len(str(count - 1))

    # Create output directory if it doesn't exist
    if not os.path.exists(op_path):
        os.makedirs(op_path)

    # Create the images
    for n in progressbar(range(count)):

        # Set image name
        # image_name = str(n).zfill(zfill_count) + image_extention
        image_name = str(n + METACONFIG["start_seq"]
                         ).zfill(zfill_count) + image_extention

        # Get a random set of valid traits based on rarity weights
        trait_sets, trait_paths = generate_trait_set_from_config()

        # Generate the actual image
        generate_single_image(trait_paths, os.path.join(op_path, image_name))

        # Populate the rarity table with metadata of newly created image
        for idx, trait in enumerate(trait_sets):
            if trait is not None:
                rarity_table[CONFIG[idx]["name"]].append(
                    trait[: -1 * len(image_extention)]
                    # .replace('_', ' ')
                    )
            else:
                rarity_table[CONFIG[idx]["name"]].append("None")

    # Create the final rarity table by removing duplicate creat
    rarity_table = pd.DataFrame(rarity_table).drop_duplicates()
    print("Generated %i images, %i are distinct" %
          (count, rarity_table.shape[0]))

    img_tb_removed = sorted(list(set(range(count)) - set(rarity_table.index)))
    print(img_tb_removed)

    # Remove duplicate images
    print("Removing %i images..." % (len(img_tb_removed)))

    # op_path = os.path.join('output', 'edition ' + str(edition))
    # for i in img_tb_removed:
    #     os.remove(os.path.join(op_path, str(
    #         i).zfill(zfill_count) + image_extention))

    print(sorted(os.listdir(op_path)))
    # Rename images such that it is sequentialluy numbered
    # for idx, img in enumerate(sorted(os.listdir(op_path))):
    #     print(img)
    #     os.rename(
    #         os.path.join(op_path, img),
    #         os.path.join(op_path, str(
    #             idx + METACONFIG["start_seq"]).zfill(zfill_count) + image_extention),
    #     )

    # Modify rarity table to reflect removals
    rarity_table = rarity_table.reset_index()
    rarity_table = rarity_table.drop("index", axis=1)
    return rarity_table


def generate_metadata_csv(rarity_table: DataFrame, edition_name: str, count: int):
    """Generate Metadata CSV from rarity data csv."""

    meta_list = []
    meta_index = []

    meta_column = list(METADATA.keys())
    rarity_column = rarity_table.keys().tolist()
    meta_column.extend(rarity_column)

    for index, row in rarity_table.iterrows():
        meta_index.append(str(index))

        listvalue = []
        for metavalue in METADATA.values():
            listvalue.append(metavalue.replace("_ID_", str(index)))

        listvalue.extend(row.to_list())
        meta_list.append(listvalue)

    meta_dataframe = pd.DataFrame(
        data=meta_list, index=meta_index, columns=meta_column)

    meta_dataframe.to_csv(
        os.path.join("output", "edition_" +
                     str(edition_name), "metadata.csv"),
        index=False,
    )


def generate_metadata_json(rarity_table: DataFrame, edition_name: str, count: int):
    """Generate Metadata CSV from rarity data csv."""

    meta_list = []
    meta_index = []

    meta_column = list(METADATA.keys())
    rarity_column = rarity_table.keys().tolist()
    meta_column.append('image')
    meta_column.append('attributes')

    zfill_count = len(str(count - 1))

    for index, row in rarity_table.iterrows():
        tmp_index = index + METACONFIG["start_seq"]
        meta_index.append(str(tmp_index))

        listvalue = []
        for metavalue in METADATA.values():
            listvalue.append(metavalue.replace("_ID_", str(tmp_index)))

        # for image url
        listvalue.append('https://xxxxxxxxxx/' + str(tmp_index))

        ralityvalue = []
        for (rarity, value) in zip(rarity_column, row):
            ralityvalue.append({
                "trait_type": rarity,
                "value": 'None' if value == '' else value
            })
        listvalue.append(ralityvalue)
        meta_list.append(listvalue)

    meta_dataframe = pd.DataFrame(
        data=meta_list, index=meta_index, columns=meta_column)

    if METACONFIG["output"] == "csv":
        meta_dataframe.to_csv(
            os.path.join("output", "edition_" +
                         str(edition_name), "metadata.csv"),
            index=False,
        )
    elif METACONFIG["output"] == "json":
        jsonArray = meta_dataframe.to_json(
            orient="records",
        )
        metadataDirName = os.path.join("output", "edition_" +
                                       str(edition_name), "metadata")
        if not(os.path.exists(metadataDirName)):
            os.makedirs(metadataDirName)
        for index, item in enumerate(json.loads(jsonArray)):
            with open(os.path.join(os.getcwd(), "output", "edition_" +
                                   str(edition_name), "metadata", str(index + METACONFIG["start_seq"]
                                                                      ) + ".json"), "w") as f:
                json.dump(item, f, indent=4)


# Main function. Point of entry
def main():

    print("Checking assets...")
    parse_config()
    print("Assets look great! We are good to go!\n")

    tot_comb = get_total_combinations()
    print("You can create a total of %i distinct avatars \n" % (tot_comb))

    print("How many avatars would you like to create? Enter a number greater than 0: ")
    while True:
        num_avatars = int(input())
        if num_avatars > 0:
            break

    print("What would you like to call this edition?: ")
    edition_name = input()

    print("Starting task...")
    rt = generate_images(edition_name, num_avatars)
    if METACONFIG["output"] == "csv":
        generate_metadata_csv(rt, edition_name, num_avatars)
    elif METACONFIG["output"] == "json":
        generate_metadata_json(rt, edition_name, num_avatars)

    print("Saving metadata...")

    print("Task complete!")


# Run the main function
main()
