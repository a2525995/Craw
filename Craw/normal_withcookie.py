import urllib.request
import urllib.parse
import http.cookiejar
URL = "http://bbs.chinaunix.net/member.php?mod=logging&loginsubmit=yes&loginhash=L768q"
URL2 = "http://bbs.chinaunix.net/"

POSTDATA = urllib.parse.urlencode({
    "username":"weisuen",
    "password":"aA123456"
}).encode('utf-8')
PATH = "/home/CORPUSERS/xp023799/PycharmProjects/Craw"
HEADER = {
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

req = urllib.request.Request(URL,POSTDATA,HEADER)
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read()
with open(PATH + "/7.html","wb") as f:
    f.write(data)
    f.close()
data2 = urllib.request.urlopen(URL2).read()
with open(PATH + "/8.html","wb") as f:
    f.write(data2)
    f.close()
