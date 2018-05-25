import re
import requests
import bs4

URL = "https://www.qiushibaike.com"
HEADER = {
        'User-Agent':
        'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
PAGE_URL = "/8hr/page/"
#craw for qiushibaike,without the detail about cha kan quan wen
def get_qiushibaike(URL):

    data = requests.get(URL,headers=HEADER)
    data.encoding = "utf-8"
    soup = bs4.BeautifulSoup(data.content,"lxml")
    #get user name
    user_name = soup.find_all("h2")
    #get user content
    user_content =  soup.find_all(attrs={"class":"content"})
    #compare the user_name and user_content if they are equal to each other
    if(len(user_name) == len(user_content)):
        for i in range(len(user_name)):
    #loop the two list to print the text
            print(user_name[i].text)
            print(user_content[i].span.text)

#craw for qiushibaike,with detail content
def get_detail_qiushibaike(URL,PAGE):
    for page in range(PAGE):
        NOW_URL = URL + PAGE_URL + str(page)
        # List for save some informations about detail content
        List_article = []
        data = requests.get(NOW_URL, headers=HEADER)
        data.encoding = "utf-8"
        soup = bs4.BeautifulSoup(data.content, "lxml")
        # find all user
        user_name = soup.find_all("h2")
        # find all url of user_content
        user_content = soup.find_all(attrs={"class": "contentHerf"})
        # splicing url save to List_article
        for content in user_content:
            List_article.append(URL + str(content.get("href")))
        # do loop get every user name and access every url to contain content
        for i in range(len(List_article)):
            page_soup = bs4.BeautifulSoup(requests.get(List_article[i], headers=HEADER).content, "lxml")
            detail_content = page_soup.find(attrs={"class": "content"}).text
            print(user_name[i].text)
            print(detail_content)



get_detail_qiushibaike(URL,20)

