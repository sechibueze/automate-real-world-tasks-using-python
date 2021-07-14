#! /usr/bin/env python3

import os
import requests

SUPPLIER_TEXT_DIR = os.path.expanduser('~') + '/supplier-data/descriptions/'
text_files = os.listdir(SUPPLIER_TEXT_DIR)

SUPPLIER_IMAGE_DIR = os.path.expanduser('~') + '/supplier-data/images/'
IMAGES = os.listdir(SUPPLIER_IMAGE_DIR)
jpeg_images = [image_name for image_name in IMAGES if '.jpeg' in image_name]

list = []
# Process the text files and images
for text_file in text_files:
    with open(SUPPLIER_TEXT_DIR + text_file, 'r') as f:
        data = {"name": f.readline().rstrip("\n"),
                "weight": int(f.readline().rstrip("\n").split(' ')[0]),
                "description": f.readline().rstrip("\n")}

        for image_file in jpeg_images:
            if image_file.split('.')[0] in text_file.split('.')[0]:
                data['image_name'] = image_file
        print("Data dict : ", data)
        list.append(data)

# Send the data to the API endpont
for item in list:
    resp = requests.post('http://127.0.0.1:80/fruits/', json=item)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created feedback ID: {}'.format(resp.json()["id"]))