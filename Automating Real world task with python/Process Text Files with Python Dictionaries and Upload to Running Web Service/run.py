#! /usr/bin/env python3

import os
# import request

url = ""
feedback_source = "./data"
feedback_source = os.path.abspath(feedback_source)

def get_files():
    files = []
    for file in os.listdir(feedback_source):
        print(os.path.abspath(file))
        filePath = os.path.join(os.getcwd(), "./data", file)
        files.append(filePath)
    return files
# print(get_files())
# dirs = os.listdir(feedback_source)


dict = {
    "name": "",
    "title": "",
    "date": "",
    "feedback": ""
}
for file in get_files():
    # file = "./data/"+file
    # keys = ["title", "name", "date", "feedback"]
    feedback = open(file, "r")
    index = 0
    for line in feedback:
        if index == 0:
            dict["title"] = line.strip()
            print("counted ", index, dict)
        elif index == 1:
            dict["name"] = line.strip()
            print("counted ", index, dict)
        elif index == 2:
            dict["date"] = line.strip()
            print("counted ", index, dict)
        else:
            dict["feedback"] = dict.get("feedback", "") + " " + line.strip()
            print("counted ", index, dict)
        index += 1
    print("dictionary", dict)
    # res = request.post(url, json=dict)
    # print("dict")

# print(os.listdir(feedback_source))