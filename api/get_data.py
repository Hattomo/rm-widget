# -*- coding: utf-8 -*-

import json
from selenium import webdriver

with open('config.json') as f:
    config = json.load(f)

driver = webdriver.Chrome('./chromedriver')
url = 'https://websearch.rakuten.co.jp/'  # 楽天ウェブ検索
driver.get(url)
