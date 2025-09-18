from PIL import Image as PI
from PIL import ImageDraw
import os
import random
import json

TOTAL_IMAGES = 10

all_images = []

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
