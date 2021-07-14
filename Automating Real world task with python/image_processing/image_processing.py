#!/usr/bin/env python3
import os
from PIL  import Image
print('srat----------------------------------------')
for dirpath, dirnames, files in os.walk('./images'):
    for index, filename in enumerate(files):
        print(filename, index)
        if filename.startswith(".D"):
             print("found dotte start", filename)
             continue
        file_path = os.path.join("images", filename)

        with Image.open(file_path).convert("RGB") as im:

            print("image data", im.size, im.format, im.mode)
    #         Rotate the image
            direction = Image.ROTATE_90
            print('direction ', direction)
            im = im.transpose(direction)
    #         Resize image
            req_size = (128,128)
            im = im.resize(req_size)
            print('new zsize', im.size)

    #         Save in new format
            fn = os.path.join("/opt/icons", str(index))
            im = im.save(fn, "jpeg")
