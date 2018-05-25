import  urllib.request
def Test_Debug():
    httphd = urllib.request.HTTPHandler(debuglevel=1)
    httpshd = urllib.request.HTTPSHandler(debuglevel=1)
    opener = urllib.request.build_opener(httphd, httpshd)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen("http://edu.51cto.com")
Test_Debug()
