import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import json
import hashlib
import os
from PIL import Image
import glob
import requests

url = "http://nmearch.minpaku.ac.jp/umesao-archives/json/11_Field_note.json"

headers = {"content-type": "application/json"}
r = requests.get(url, headers=headers)
data = r.json()

content = data["content"]





files = glob.glob("tmp/*.json")

rows = []
rows.append(["ID", "title", "Thumbnail", "rights", "manifest", "Relation", "viewingDirection", "viewingHint", "attribution"])
rows.append(["http://purl.org/dc/terms/identifier", "http://purl.org/dc/terms/title", "http://xmlns.com/foaf/0.1/thumbnail", "http://purl.org/dc/terms/rights", "http://schema.org/url", "http://purl.org/dc/terms/relation", "http://iiif.io/api/presentation/2#viewingDirection", "http://iiif.io/api/presentation/2#viewingHint"])
rows.append(["Literal", "Literal", "Resource", "Resource", "Resource"])

for row in content:
    obj = content[row]

    item = obj["item"]

    key = ""

    if "link" in item["資料名"]:
        link = item["資料名"]["link"]

        tmp = link.split("?")[1].split("&")
        category = tmp[0].split("=")[1]
        sub = tmp[1].split("=")[1]

        key = category+"___"+sub

    rows.append(["11_Field_note___"+item["資料番号"]["value"], item["山、調査、探検行名"]["value"], "", "", "", "", "", "", "", item["資料番号"]["value"], item["状況"]["value"], item["資料名"]["value"], item["年月日"]["value"], item["形態"]["value"], key])

import csv

f = open('data/items.csv', 'w')

writer = csv.writer(f, lineterminator='\n')
writer.writerows(rows)

f.close()

            
