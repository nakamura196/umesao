import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import json
import hashlib
import os
from PIL import Image
import glob
import requests

url = "http://nmearch.minpaku.ac.jp/umesao-archives/json/16_romaji_card.json"

headers = {"content-type": "application/json"}
r = requests.get(url, headers=headers)
data = r.json()

content = data["content"]

rows = []
rows.append(["ID", "title", "Thumbnail", "rights", "manifest", "Relation", "viewingDirection", "viewingHint", "attribution"])
rows.append(["http://purl.org/dc/terms/identifier", "http://purl.org/dc/terms/title", "http://xmlns.com/foaf/0.1/thumbnail", "http://purl.org/dc/terms/rights", "http://schema.org/url", "http://purl.org/dc/terms/relation", "http://iiif.io/api/presentation/2#viewingDirection", "http://iiif.io/api/presentation/2#viewingHint"])
rows.append(["Literal", "Literal", "Resource", "Resource", "Resource"])
rows.append([])

for row in content:
    obj = content[row]

    item = obj["item"]

    key = ""

    title_field = "見出し"
    id_field = "資料番号"

    if "link" in item[title_field]:
        link = item[title_field]["link"]

        tmp = link.split("?")[1].split("&")
        category = tmp[0].split("=")[1]
        sub = tmp[1].split("=")[1]

        key = category+"___"+sub

    rows.append(["16_romaji_card___"+item[id_field]["value"], item[title_field]["value"], "", "", "", "", "", "", "", key])

import csv

f = open('data/items.csv', 'w')

writer = csv.writer(f, lineterminator='\n')
writer.writerows(rows)

f.close()

            
