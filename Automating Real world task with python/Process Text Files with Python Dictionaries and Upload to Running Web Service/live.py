
#! /usr/bin/env python3

import os
import requests
import json
url = r"http://35.238.253.23/feedback/" # do not forget to add the last slash
feedback_source = "/data/feedback"
feedback_source = os.path.abspath(feedback_source)

def get_files():
    files = []
    for file in os.listdir(feedback_source):
        print(os.path.abspath(file))
        filePath = os.path.join(os.getcwd(), "/data/feedback/", file)
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
    print("handling file.. ", file)
    feedback = open(file, "r")
    index = 0
    for line in feedback:
        if index == 0:
            dict["title"] = line.strip()
            #print("counted ", index, dict)
        elif index == 1:
            dict["name"] = line.strip()
            #print("counted ", index, dict)
        elif index == 2:
            dict["date"] = line.strip()
            #print("counted ", index, dict)
        else:
            dict["feedback"] =  line.strip()
            #print("counted ", index, dict)
        index += 1
    d = json.dumps(dict)
    print("dictionary", d)
    print("request url", url)
    res = requests.post(url, json=d, data=dict)
    print("res ", res.status_code)
    print("res body", res.json())
    print("body text", res.text)
    feedback.close()

# print(os.listdir(feedback_source))
