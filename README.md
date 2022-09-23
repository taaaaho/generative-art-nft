# Generative NFT Art

## Introduction

The `generative-art-nft` repository is a library for creating generative art. It was developed for the purpose of creating NFT avatar & collectible projects. This library was used to generate the artwork for the [Love Addicted Girls](https://www.soudannft.xyz) project.

## Features

### Generate over a million distinct images with less than 60 traits

The library allows you to generate images every distinct possible combination of your traits. For context, if you had trait art for a project like [Bored Apes](https://boredapeyachtclub.com/#/home), the library could generate upwards of 1.2 billion distinct apes.

### Add rarity weights

The library also allows you to configure the image generation process in such a way that you have complete control over how rare each and every trait is.

### Generate compliant JSON metadata for your NFTs

There is now an added functionality to generate JSON metadata for your NFTs that are in compliance with OpenSea metadata requirements (and by extension, the general NFT metadata standard).

### Fuzzy friendly

You can use this library even if you do not know how to program (in Python or otherwise). Do check out the [Tutorial](https://medium.com/scrappy-squirrels/tutorial-create-generative-nft-art-with-rarities-8ee6ce843133) for more details on how to use (non-technical) and extend (technical) the library.

## Installation

**Clone this repository**

`git clone https://github.com/gurujowa/generative-art-nft.git`

**Install required packages**

`pip install Pillow pandas progressbar2`

Upload your input assets in the `assets` folder, fill up the `config.py` file, and then run `python nft.py`.

## Usage

This project is forked from Scrappy Squirrels. Scrappy Squirrels have good Document. Check it out [here](https://medium.com/scrappy-squirrels/tutorial-create-generative-nft-art-with-rarities-8ee6ce843133)

The following features have been added to this program.

- The output metadata is now compatible with [ThirdWeb](https://thirdweb.com/).
- Added support for one-to-one parts, such as front hair and back hair.
- Added DockerFile, .gitignore, etc.

## If you using IPFS like Pinata

You can change metadata output for IPFS.

Please set METACONFIG output to json.

(If you use ThirdWeb then set to csv.)

```json
METACONFIG = {
    "output": "json",
    "start_seq": 0
}
```

You need upload to Pinata then bellow article is useful.

https://note.com/hayattiq/n/n752d51d07cda

The following is a note of the commands I used to manipulate files using GCP's Compute Engine.

```bash
$ sudo apt-get update
$ sudo apt-get install -y wget unzip
$ wget https://dist.ipfs.tech/kubo/v0.15.0/kubo_v0.15.0_linux-amd64.tar.gz
$ tar -xvzf kubo_v0.15.0_linux-amd64.tar.gz
$ cd kudo
$ ipfs init
$ ipfs daemon
```

Transfer your local images.

```bash
$ gcloud compute scp --recurse ./images.zip [your gce name]:~ --zone "your zone"  --project "your project"
```

Add the folder to IPFS in another terminal without changing the terminal where the above command was executed.

```bash
$ ipfs add --recursive --progress ./images/
```

The above command will output the following information at the end.

This is the folder CID, so copy and upload to Pinata using this.

```
added QmZpGa8RnH7QDhiz1hN9MdqBFyqULrEdMRWetW5hdEivjs images
```
