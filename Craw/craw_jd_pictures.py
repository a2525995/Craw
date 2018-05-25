# -*- coding:utf-8 -*-
"""Craw some pictures of JD shopping mall"""
import sys
import requests
from bs4 import BeautifulSoup
import os
import re
URL = "https://search.jd.com/search?keyword=手机&enc=utf-8&qrst=1&wq=shou&cid2=653&cid3=655&page="
HEADER = {
        'User-Agent':
        'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
HTTP = "https:"
DOWNLOAD_PATH = "/home/CORPUSERS/xp023799/Downloads"
list1 = []
def craw_jd(URL,PAGE):
    picture_name = 0
    PAGE+=1
    for count in range(1,PAGE):
        #Composition of URL
        URL = URL + str(count)
        #Get access link’s data
        data = requests.get(URL, headers=HEADER)
        data.encoding = 'utf-8'
        soup = BeautifulSoup(data.text, "lxml")
        #Filter
        imgList = soup.find_all(attrs={"class": "err-product",
                                       "data-img": "1",
                                       "width": "220",
                                       "height": "220",
                                       "data-lazy-img": re.compile("^//")
                                       }
                                )
        #Check the direct exist,if not create direct
        if not(os.path.isdir(DOWNLOAD_PATH + "/JD_pictures" + "/" + str(count))):
            os.makedirs(DOWNLOAD_PATH + "/JD_pictures" + "/" + str(count))
        #Change the workspace to the path
        os.chdir(DOWNLOAD_PATH + "/JD_pictures" + "/" + str(count))
        #Read the URL and download pictures one by one
        for img in imgList:
            picture_name+=1
            # composition of URL
            all_url = HTTP + str(img.get('data-lazy-img'))
            req = requests.get(all_url)
            # write in pictures
            with open(str(picture_name) + ".jpg", "wb") as f:
                f.write(req.content)


