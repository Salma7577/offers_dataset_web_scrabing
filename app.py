
from base64 import encode
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import pandas as pd

# link = "https://www.alsoouq.com/saudi-arabia-offers/panda-offers/page/"
# # print(result.content)

# weekly_offers_link = []
# for i in range(1, 3):
#     src = requests.get(link+str(i)).content
#     soup = BeautifulSoup(src, "lxml")
#     weekly_offers_link.extend(soup.select("a.more-link"))

# # print(weekly_offers_link[1].attrs["href"])

# for i in range(len(weekly_offers_link)):
#     weekly_offers_link[i] = weekly_offers_link[i].attrs["href"]


# print(weekly_offers_link)


# src = requests.get(weekly_offers_link[1]).content
# soup = BeautifulSoup(src, "lxml")
# page_images = soup.select("noscript")
# print(page_images[1].text)
# print([x.encode('utf-8') for x in soup.select("noscript")])


# result = requests.get(
#     "https://www.alsoouq.com/saudi-arabia-offers/panda-offers/page/1")
# src = result.content
# print(src)


# print(soup)
# weekly_offers_link = soup.find_all("a", {"class", "more-link"})
# print(weekly_offers_link)


# page_images = soup.find_all(
#     "div", {"style": "width: 100%; text-align: center;"})
# page_images = soup.find_all("noscript")


# print([x.encode('utf-8') for x in page_images])
d = pd.concat([pd.read_csv(r'data\danube\booklet_danube.csv'), pd.read_csv(r'data/othaim/booklet_othaim.csv'),
              pd.read_csv(r'data/pandah/booklet_pandah.csv'), pd.read_csv(r'data/tamimi/booklet_tamimi.csv')])
print(str(d.count()))
