import urllib.request
import ssl
import requests
Proxy = '180.121.134.81:808'
URL = 'http://www.baidu.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

def use_proxy(proxy_addr,url):
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data1 = urllib.request.Request(url,headers=headers)
    data = urllib.request.urlopen(data1).read().decode('utf-8')
    return data

data = use_proxy(Proxy,URL)
print(data)