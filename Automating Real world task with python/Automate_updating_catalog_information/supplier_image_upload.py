#!/usr/bin/env python3
import requests
import os
# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
img_dir=os.path.expanduser("~")+"/supplier-data/images/"
images = os.listdir(img_dir)
jpeg_images = [image for image in images if ".jpeg" in  image ]

for i in jpeg_images:
  with open(img_dir+i, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
