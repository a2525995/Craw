import urllib.request
import urllib.parse
url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=L768q"
url2 = "http://bbs.chinaunix.net/"
path = "/home/CORPUSERS/xp023799/PycharmProjects/Craw"
postdata = urllib.parse.urlencode({
    "username":"weisuen",
    "password":"aA123456"
}).encode('utf-8')
req = urllib.request.Request(url,postdata)
req.add_header( 'User-Agent',
                'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
data = urllib.request.urlopen(req).read()
with open(path + "/5.html","wb") as f:
    f.write(data)
    f.close()
req2 =urllib.request.Request(url2,postdata)
req2.add_header('User-Agent',
                'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
data2 = urllib.request.urlopen(req2).read()
with open(path + "/6.html","wb") as f:
    f.write(data2)
    f.close()