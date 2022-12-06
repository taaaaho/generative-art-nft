import os
import glob
import json
import random

all = ['background', 'background_item', 'body', 'clothes', 'eyes', 'mouth',  'hair',
       'face_accessory',  'head_accessory', 'hand_item', 'attached1', 'attached2', 'attached3', 'personality']

newAll = [
"Background",
"Background Item",
"Body",
"Clothes",
"Eyes",
"Mouth",
"Hair",
"hair",
"Face Accessory",
"Head Accessory",
"Hand Item",
"Favorite Things",
"Doji",
"Buddy", "Personality"]
personality = ['Adamant', 'Bashful', 'Docile', 'Gentle', 'Hardy',
               'Impish', 'Lonely', 'Mild', 'Modest', 'Relaxed', 'Serious', 'Geek']


def renameSpecificMetadata():
    print('Start rename metadatas')
    path = '/Users/takaho/Downloads/ruki_11182/metadata'
    metadatas = glob.glob(os.path.join(
        path, '*'))

    # 処理順番を合わせるためにソート
    for metadata in metadatas:
        with open(metadata) as f:
            print('meta', metadata)
            df = json.load(f)
            # Image rename
            # image = df['image'].split('/')  # ['https:', '', 'xxxxxxxxxx', '2']
            # image[3] = str(os.path.splitext(os.path.basename(metadata))[0])
            # df['image'] = '/'.join(image)

            # 1113 add data
            df['image'] = 'https://storage.googleapis.com/metakozo/images/' + str(os.path.splitext(os.path.basename(metadata))[0]) + '.png'
            # 1113 add data
            
            # Name rename
            # print(df['name'].split(
            #     '#')[0] + '#' + str(os.path.splitext(os.path.basename(metadata))[0]))
            df['name'] = df['name'].split(
                '#')[0] + '#' + str(os.path.splitext(os.path.basename(metadata))[0])

            with open(metadata, 'w') as wf:
                json.dump(df, wf, indent=4)
            wf.close()
        f.close()

def renameMetadata():
    print('Start rename metadatas')
    path = '/Users/takaho/src/github.com/taaaaho/nft-viewer/public/1124/metadata'
    metadatas = glob.glob(os.path.join(
        path, '*'))

    # 処理順番を合わせるためにソート
    for metadata in metadatas:
        with open(metadata) as f:
            print('meta', metadata)
            df = json.load(f)
            # Image rename
            # image = df['image'].split('/')  # ['https:', '', 'xxxxxxxxxx', '2']
            # image[3] = str(os.path.splitext(os.path.basename(metadata))[0])
            # df['image'] = '/'.join(image)

            # 1113 add data
            df['image'] = 'https://storage.googleapis.com/metakozo/images/' + str(os.path.splitext(os.path.basename(metadata))[0]) + '.png'
            # 1113 add data
            
            # Name rename
            df['name'] = df['name'].split(
                '#')[0] + '#' + str(os.path.splitext(os.path.basename(metadata))[0])

            with open(metadata, 'w') as wf:
                json.dump(df, wf, indent=4)
            wf.close()
        f.close()


def removeMeta():
    print('Start removeMeta')
    # metadatas = glob.glob(os.path.join(
    #     'output', 'edition_2222', 'metadata', '*'))
    path = '/Users/takaho/src/github.com/taaaaho/generative-art-nft/output/1122typeA2119/metadata'

    metadatas = glob.glob(os.path.join(
        path, '*'))

    for metadata in metadatas:
        print(metadata)
        with open(metadata) as f:
            df = json.load(f)
            # Image rename
            newAttributes = []
            attributes = df['attributes']

            # Delete Attributes Start
            for att in attributes:
                # Append include all list
                if att['trait_type'] in newAll:
                    newAttributes.append(att)
            df['attributes'] = newAttributes

            with open(metadata, 'w') as wf:
                json.dump(df, wf, indent=4)
            wf.close()
        f.close()

def adjustMetadata():
    print('Start Adjust Metadatas')
    # metadatas = glob.glob(os.path.join(
    #     'output', 'edition_2222', 'metadata', '*'))
    # path = '/Users/takaho/src/github.com/taaaaho/nft-viewer/public/edition_2222/new_metadata'
    path = '/Users/takaho/src/github.com/taaaaho/nft-viewer/public/add2/meta'

    metadatas = glob.glob(os.path.join(
        path, '*'))

    for metadata in metadatas:
        print(metadata)
        with open(metadata) as f:
            df = json.load(f)
            # Image rename
            newAttributes = []
            attributes = df['attributes']

            # Delete Attributes Start
            for att in attributes:
                # Append include all list
                if att['trait_type'] in all:
                    if att['trait_type'] == 'attached1':
                        newAttributes.append({
                            'trait_type': 'favorite_things',
                            'value': att['value']
                        })
                    elif att['trait_type'] == 'attached2':
                        newAttributes.append({
                            'trait_type': 'doji',
                            'value': att['value']
                        })
                    elif att['trait_type'] == 'attached3':
                        newAttributes.append({
                            'trait_type': 'buddy',
                            'value': att['value']
                        })
                    else:
                        newAttributes.append(att)

            # Add shortage attributes
            attributeArray = []
            for tempatt in attributes:
                attributeArray.append(tempatt['trait_type'])
            for allatt in all:
                if allatt not in attributeArray:
                    if allatt == 'personality':
                        newAttributes.append({
                            "trait_type": allatt,
                            "value": random.choice(personality)
                        })
                    else:
                        newAttributes.append({
                            "trait_type": allatt,
                            "value": "none"
                        })
            df['attributes'] = newAttributes

            with open(metadata, 'w') as wf:
                json.dump(df, wf, indent=4)
            wf.close()
        f.close()

def renameEyesNormaltoLucky():
    print('Start renameEyesNormaltoLucky')
    path = '/Users/takaho/src/github.com/taaaaho/nft-viewer/public/edition_2222/metadata'

    metadatas = glob.glob(os.path.join(
        path, '*'))

    for metadata in metadatas:
        with open(metadata) as f:
            df = json.load(f)

            attributes = df['attributes']
            for att in attributes:
                # Append include all list
                if att['trait_type'] == 'Eyes' and att['value'] == 'Normal':
                    att['value'] = 'Lucky'
                    df['attributes'] = attributes
                    with open(metadata, 'w') as wf:
                        json.dump(df, wf, indent=4)
                    wf.close()
        f.close()

def renameEyesNoneToNormal():
    count = 0
    print('Start renameEyesNormaltoLucky')
    path = '/Users/takaho/src/github.com/taaaaho/nft-viewer/public/edition_2222/metadata'

    metadatas = glob.glob(os.path.join(
        path, '*'))

    for metadata in metadatas:
        with open(metadata) as f:
            df = json.load(f)

            attributes = df['attributes']
            for att in attributes:
                # Append include all list
                if att['trait_type'] == 'Eyes' and att['value'] == 'None':
                    att['value'] = 'Normal'
                    df['attributes'] = attributes
                    print(metadata)
                    count = count + 1
                    with open(metadata, 'w') as wf:
                        json.dump(df, wf, indent=4)
                    wf.close()
        f.close()
    print(count)

def createMBAMetadata():
    count = 0
    print('Start renameEyesNormaltoLucky')
    path = '/Users/takaho/Documents/Work/MetaKozo/Souvenir/reveal.json'
    export_path = '/Users/takaho/Documents/Work/MetaKozo/Souvenir'

    metadatas = glob.glob(path)

    with open(metadatas[0]) as f:
        df = json.load(f)
        temp_name = df['name']
        for i in range(1000):
            df['name'] = temp_name + '#' + str(count)
            with open(os.path.join(export_path,str(count) + '.json'), 'w') as wf:
                json.dump(df, wf, indent=4)
            wf.close()     
            count = count + 1   
    f.close()

    # for metadata in metadatas:
    #     print(metadata)
    #     with open(metadata) as f:
    #         df = json.load(f)
    #         df['name'] = df['name'] + '#' + count
    #     f.close()
    # print(count)

def main():
    # Overwrite metadata files
    # adjustMetadata()
    # renameMetadata()
    # renameSpecificMetadata()
    # removeMeta()
    # renameEyesNormaltoLucky()
    # renameEyesNoneToNormal()
    createMBAMetadata()


main()
