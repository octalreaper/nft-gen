from PIL import Image as PI
from PIL import ImageDraw
import os
import random
import json

TOTAL_IMAGES = 10

w, h = 220, 220

x_offset = 10
y_offset = 25

img_mode = "RGB"
block_size = (10, 10)
block_color = "Slategray"
face_color = "White"
body_color = "Powderblue"  # TEST

bg_colors = ["Coral", "Cyan", "Darkblue", "Firebrick", "Lime", "Orangered", "Pink", "Tomato", "White", "Orange"]
bgc_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

cat_colors = ["Dimgray", "Peachpuff", "Powderblue", "Peru"]
cc_weights = [25, 25, 25, 25]

eye_colors = ["Black", "Red", "Gold"]
ec_weights = [40, 40, 20]


# BODY
body_list = [
    [10, 10, 30, 20],
    [20, 20, 40, 30],
    [110, 10, 140, 20],
    [110, 20, 130, 30],
    [30, 30, 120, 110],
    [10, 60, 20, 100],
    [20, 50, 30, 110],
    [120, 50, 130, 110],
    [130, 60, 140, 100],
    [20, 110, 130, 160],
    [140, 130, 150, 140],
    [150, 90, 160, 130],
    [160, 80, 180, 90],
    [180, 90, 190, 100],
    [130, 140, 140, 150],
]

# OUTLINE
outline_list = [
    [10, 0, 30, 10],
    [0, 10, 10, 100],
    [10, 100, 20, 110],
    [20, 110, 30, 130],
    [30, 110, 40, 120],
    [10, 130, 20, 160],
    [30, 10, 40, 20],
    [40, 20, 110, 30],
    [100, 10, 110, 20],
    [110, 0, 140, 10],
    [140, 10, 150, 130],
    [130, 100, 140, 110],
    [130, 130, 140, 140],
    [120, 110, 130, 130],
    [110, 110, 120, 120],
    [140, 140, 150, 150],
    [130, 150, 140, 160],
    [20, 160, 130, 170],
    [50, 140, 60, 160],
    [90, 140, 100, 160],
    [150, 130, 160, 140],
    [150, 80, 160, 90],
    [160, 70, 180, 80],
    [180, 80, 190, 90],
    [160, 90, 180, 100],
    [190, 90, 200, 100],
    [160, 100, 170, 130],
    [180, 100, 190, 110],
]

# FACE
face_list = [
    [60, 80, 90, 90],
    [50, 90, 100, 100],
    [40, 100, 110, 110],
]

# NOSE
nose_list = [[70, 90, 80, 100], ]

# EYES
eyes_list = [
    [40, 70, 50, 90],
    [100, 70, 110, 90],
]

# EARS
ears_list = [
    [10, 20, 20, 60],
    [20, 30, 30, 50],
    [120, 30, 130, 50],
    [130, 20, 140, 60],
]

# COLLAR
collar_list = [[40, 110, 110, 120], ]

# SIGN
sign_list = [[70, 120, 80, 130], ]


def create_new_image():
    new_image = {"Background": random.choices(bg_colors, bgc_weights)[0],
                 "Body": random.choices(cat_colors, cc_weights)[0], "Eyes": random.choices(eye_colors, ec_weights)[0]}

    # For each trait category, select a random trait based on the weightings

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image


def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)


def fdraw(arr, col):
    xy = [0, 0, 0, 0]
    for i in arr:
        if len(i) == 4:
            xy[0] = i[0] + x_offset
            xy[1] = i[1] + y_offset
            xy[2] = i[2] + x_offset
            xy[3] = i[3] + y_offset
            draw.rectangle(xy, fill=col)

def ensure_dirs(dirs: list[str]) -> None:
    for d in dirs:
        os.makedirs(d, exist_ok=True)

if __name__ == '__main__':

    all_images = []

    ensure_dirs([
        "./content/images/",
        "./content/metadata/"
    ])

    for i in range(TOTAL_IMAGES):
        new_trait_image = create_new_image()

        all_images.append(new_trait_image)

    tid = 0
    for item in all_images:
        item["tokenId"] = tid
        tid = tid + 1

    if all_images_unique(all_images):
        for data in all_images:
            # print(data)
            print(data['Background'], data['Body'], data['Eyes'], data['tokenId'])
            im = PI.new(mode=img_mode, size=(w, h), color=data['Background'])
            draw = ImageDraw.Draw(im)
            fdraw(body_list, data['Body'])
            fdraw(outline_list, block_color)
            fdraw(face_list, face_color)
            fdraw(nose_list, "Black")
            fdraw(eyes_list, data['Eyes'])
            fdraw(ears_list, "Gray")
            fdraw(collar_list, "Blue")
            fdraw(sign_list, "Gold")
            im.save("content/images/" + str(data['tokenId']) + ".png")

    # GENERATE METADATA
    with open('content/metadata/metadata.json', 'w') as outfile:
        json.dump(all_images, outfile, indent=4)

