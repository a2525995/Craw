import re
import requests
import bs4
HEADER = {
        'User-Agent':
        'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
URL = "http://blog.csdn.net/"
#Craw for every href of csdn's index
def getlink(url):
    data = requests.get(url,headers=HEADER)
    data.encoding = "utf-8"
    soup = bs4.BeautifulSoup(data.content,"lxml")
    url_list = soup.find_all(attrs={"href":re.compile('^https?://')})
    for i in url_list:
        print(str(i.get('href')))

getlink(URL)