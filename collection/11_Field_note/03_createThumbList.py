import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import json
import hashlib
import os
from PIL import Image
import glob

files = glob.glob("tmp/*.json")

rows = []
rows.append(["ID", "Thubmnail"])

for file in sorted(files):

    filename = file.split("/")[-1]

    print(filename)

    # jsonファイルを読み込む
    f = open(file)
    # jsonデータを読み込んだファイルオブジェクトからPythonデータを作成
    data = json.load(f)
    # ファイルを閉じる
    f.close()

    id = filename.replace(".json", "")
    id = id[0: len(id) - 4] 
    rows.append([id, data["thumbnail"]])

import csv

f = open('data/thumbnail.csv', 'w')

writer = csv.writer(f, lineterminator='\n')
writer.writerows(rows)

f.close()




       
