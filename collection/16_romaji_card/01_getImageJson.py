import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import json
import hashlib
import os
from PIL import Image
import requests

url = "http://nmearch.minpaku.ac.jp/umesao-archives/json/imageList.json"

headers = {"content-type": "application/json"}
r = requests.get(url, headers=headers)
image_list = r.json()



url = "http://nmearch.minpaku.ac.jp/umesao-archives/json/16_romaji_card.json"

headers = {"content-type": "application/json"}
r = requests.get(url, headers=headers)
data = r.json()

content = data["content"]

for row in content:
    obj = content[row]

    field = "見出し"

    if "link" in obj["item"][field]:
        link = obj["item"][field]["link"]
        print(link)

        tmp = link.split("?")[1].split("&")
        category = tmp[0].split("=")[1]
        sub = tmp[1].split("=")[1]


        images = image_list[category][sub]

        page = 1

        for id in images:

            key = category+"___"+sub

            original = "http://nmearch.minpaku.ac.jp/umesao-archives/swipeImage/"+urllib.parse.quote(category)+"/"+urllib.parse.quote(sub)+"/"+id
            thumbnail = "http://nmearch.minpaku.ac.jp/umesao-archives/swipeImage/"+urllib.parse.quote(category)+"/"+urllib.parse.quote(sub)+"/thu/"+id.replace(".jpg", "-thu.jpg")

            path  = "tmp/"+key+"_"+str(page).zfill(3)+".json"

            if not os.path.exists(path):

                src = original

                print(src)

                image = Image.open(urllib.request.urlopen(src))
                width, height = image.size

                thumb = thumbnail

                obj = {
                    "original": src,
                    "thumbnail": thumb,
                    "book": key,
                    "page": page,
                    "width": width,
                    "height": height
                }

                with open(path, 'w') as outfile:
                    json.dump(obj, outfile, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
                
                page += 1
