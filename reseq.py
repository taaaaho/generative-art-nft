import os
import glob
import json


def metadataMatchToImage(edition_name: str, rendered_size: int):
    print('Start delete metadatas')
    images = glob.glob(os.path.join(
        '/Users/takaho/Documents/Work/MetaKozo/ProductionNormal', 'images', '*'))
    zfill_count = 4

    # 処理順番を合わせるためにソート
    sortedFileName = []
    for image in sorted(images):
        sortedFileName.append(
            int(os.path.splitext(os.path.basename(image))[0]))

    # print("Rendering %i files / Removed %i files / Remain Total is %i " %
    #       (rendered_size, rendered_size - len(sortedFileName), len(sortedFileName)))
    metadata_path = os.path.join(
        '/Users/takaho/Documents/Work/MetaKozo/ProductionNormal', 'metadata')

    # 画像名称を正としてjsonファイルを削除
    for i in range(9000):
        if i not in sortedFileName:
            if (os.path.isfile(os.path.join(metadata_path, str(i).zfill(zfill_count) + ".json"))):
                os.remove(os.path.join(metadata_path, str(
                    i).zfill(zfill_count) + ".json"))


def renameFile(edition_name: str, rendered_size: int):
    print('Start rename files')
    images = glob.glob(os.path.join('output', edition_name, 'images', '*'))
    metadata_path = os.path.join('output', edition_name, 'metadata')
    print(os.path.join('output', edition_name, 'images', '*'))

    # ソート用0埋めしていたが0埋めなしのidxでリネームしていく
    image_path = os.path.join('output', edition_name, 'images')
    for idx, img in enumerate(sorted(images)):
        tmpIdx = idx + 0
        print(tmpIdx)

        print(os.path.join(metadata_path, str(
            os.path.splitext(os.path.basename(img))[0]) + ".json"))
        print(os.path.join(metadata_path, str(tmpIdx) + ".json"))
        print('----')

        os.rename(
            os.path.join(metadata_path, str(
                os.path.splitext(os.path.basename(img))[0]) + ".json"),
            os.path.join(metadata_path, str(tmpIdx) + ".json"),
        )
        print(img)
        print(os.path.join(image_path, str(tmpIdx) + ".png"))
        os.rename(
            img,
            os.path.join(image_path, str(tmpIdx) + ".png"),
        )
        print('----')


def renameMetadata(edition_name: str):
    print('Start rename metadatas')
    metadatas = glob.glob(os.path.join(
        'output', edition_name, 'metadata', '*'))

    # 処理順番を合わせるためにソート
    for metadata in metadatas:
        with open(metadata) as f:
            df = json.load(f)
            # Image rename
            image = df['image'].split('/')  # ['https:', '', 'xxxxxxxxxx', '2']
            image[3] = str(os.path.splitext(os.path.basename(metadata))[0])
            df['image'] = '/'.join(image)

            # Name rename
            df['name'] = df['name'].split(
                '#')[0] + '#' + str(os.path.splitext(os.path.basename(metadata))[0])

            with open(metadata, 'w') as wf:
                json.dump(df, wf, indent=4)
            wf.close()
        f.close()


def main():
    print('Start reseq')
    print("What would you like to call this edition?: ")
    edition_name = 'edition_' + input()

    print("Collection size?: ")
    rendered_size = int(input())

    print("Mode?: 1=Only Delete Metadata / 2=All Process")
    mode = int(input())

    # Remove metadata so that it is the same as the image file
    # metadataMatchToImage(edition_name, rendered_size)

    if mode == 1:
        return

    # Rename by reassigning the sequence from 0
    renameFile(edition_name, rendered_size)

    # Overwrite sequences in metadata files
    renameMetadata(edition_name)


main()
