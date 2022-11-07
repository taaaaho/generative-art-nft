import os
import glob
import json


def zfillFiles():
    print('Start Zfill metadatas')
    path = '/Users/takaho/Documents/Work/MetaKozo/ProductionNormal/metadata'
    images = glob.glob(os.path.join(
        path, '*'))
    zfill_count = 4

    # 処理順番を合わせるためにソート
    sortedFileName = []
    for image in sorted(images):
        sortedFileName.append(
            os.path.splitext(os.path.basename(image))[0])

    # print(sortedFileName)
    # 画像名称を正としてjsonファイルを削除
    count = 0
    for i in sortedFileName:
        if len(i) < 4:
            print(i)
            print(os.path.join(path, i + ".json"))
            print(os.path.join(path, i.zfill(zfill_count) + ".json"))
            os.rename(
                os.path.join(path, i + ".json"),
                os.path.join(path, i.zfill(zfill_count) + ".json"),
            )
            count = count + 1
    print(count)


def unZfillFiles():
    print('Start UnZFill metadatas')
    path = '/Users/takaho/src/github.com/taaaaho/nft-viewer/public/edition_2222/new_metadata'
    images = glob.glob(os.path.join(
        path, '*'))

    zfill_count = 4

    # 処理順番を合わせるためにソート
    sortedFileName = []
    for image in sorted(images):
        sortedFileName.append(
            os.path.splitext(os.path.basename(image))[0])

    print(sortedFileName)
    # 画像名称を正としてjsonファイルを削除
    count = 0
    for i in sortedFileName:
        # if len(i) < 4:
        print(i)
        print(os.path.join(path, i + ".json"))
        os.rename(
            os.path.join(path, i + ".json"),
            os.path.join(path, str(int(i)) + ".json"),
        )
        count = count + 1
    print(count)


# def renameFile(edition_name: str, rendered_size: int):
#     print('Start rename files')
#     images = glob.glob(os.path.join('output', edition_name, 'images', '*'))
#     metadata_path = os.path.join('output', edition_name, 'metadata')

#     # ソート用0埋めしていたが0埋めなしのidxでリネームしていく
#     image_path = os.path.join('output', edition_name, 'images')
#     for idx, img in enumerate(sorted(images)):
#         # print(os.path.join(metadata_path, str(
#         #     os.path.splitext(os.path.basename(img))[0]) + ".json"))
#         # print(os.path.join(metadata_path, str(idx) + ".json"))
#         # print('----')
#         os.rename(
#             os.path.join(metadata_path, str(
#                 os.path.splitext(os.path.basename(img))[0]) + ".json"),
#             os.path.join(metadata_path, str(idx) + ".json"),
#         )
#         # print(img)
#         # print(os.path.join(image_path, str(idx) + ".png"))
#         os.rename(
#             img,
#             os.path.join(image_path, str(idx) + ".png"),
#         )
#         # print('----')


# def renameMetadata(edition_name: str):
#     print('Start rename metadatas')
#     metadatas = glob.glob(os.path.join(
#         'output', edition_name, 'metadata', '*'))

#     # 処理順番を合わせるためにソート
#     for metadata in metadatas:
#         with open(metadata) as f:
#             df = json.load(f)
#             # Image rename
#             image = df['image'].split('/')  # ['https:', '', 'xxxxxxxxxx', '2']
#             image[3] = str(os.path.splitext(os.path.basename(metadata))[0])
#             df['image'] = '/'.join(image)

#             # Name rename
#             df['name'] = df['name'].split(
#                 '#')[0] + '#' + str(os.path.splitext(os.path.basename(metadata))[0])

#             with open(metadata, 'w') as wf:
#                 json.dump(df, wf, indent=4)
#             wf.close()
#         f.close()


def main():
    # Remove metadata so that it is the same as the image file
    # zfillFiles()
    unZfillFiles()


main()
