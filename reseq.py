import os
import glob

print('Start reseq')
print("What would you like to call this edition?: ")
edition_name = 'edition_' + input()

print("Collection size?: ")
rendered_size = int(input())

images = glob.glob(os.path.join('output', edition_name, 'images', '*'))
zfill_count = len(str(rendered_size - 1))

# zfillImages = []
sortedFileName = []
for image in sorted(images):
    sortedFileName.append(int(os.path.splitext(os.path.basename(image))[0]))

print("Rendering %i files / Removed %i files / Remain Total is %i " %
      (rendered_size, rendered_size - len(sortedFileName), len(sortedFileName)))
metadata_path = os.path.join('output', edition_name, 'metadata')
for i in range(rendered_size):
    if i not in sortedFileName:
        if (os.path.isfile(os.path.join(metadata_path, str(i) + ".json"))):
            os.remove(os.path.join(metadata_path, str(i) + ".json"))

image_path = os.path.join('output', edition_name, 'images')
for idx, img in enumerate(sorted(images)):
    print(img)
    print(os.path.join(image_path, str(idx) + ".png"))
    os.rename(
        img,
        os.path.join(image_path, str(idx) + ".png"),
    )
    print('----')
    print(os.path.join(metadata_path, str(int(
        os.path.splitext(os.path.basename(img))[0])) + ".json"))
    print(os.path.join(metadata_path, str(idx) + ".json"))
    print('----')
    os.rename(
        os.path.join(metadata_path, str(int(
            os.path.splitext(os.path.basename(img))[0])) + ".json"),
        os.path.join(metadata_path, str(idx) + ".json"),
    )
