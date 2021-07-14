#!/usr/bin/env python3

import os
from PIL import Image

img_dir = os.path.expanduser("~")+ "/supplier-data/images/"
new_size = (600, 400)

for image in os.listdir(img_dir):
  if ".tiff" in image and "." not in image[0]:
    img = Image.open(img_dir+image)
    img.resize(new_size).convert("RGB").save(img_dir+image.split(".")[0]+".jpeg", "jpeg")
    img.close()
