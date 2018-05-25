import  urllib.request
def Test_get():
    file = urllib.request.urlopen("http://www.baidu.com")
    header = {"User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"}
    data = file.read()
    print(file.getcode())
    dataline = file.readline()
    with open("/home/CORPUSERS/xp023799/PycharmProjects/Craw/1.html", "wb") as f:
        f.write(data)
Test_get()