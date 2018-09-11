from urllib.parse import urlparse,urlencode,quote

#url = "http://www.baidu.com/index.html;user?id=6#comment"
url = "http://ehr.unisoc.com/SpreadTrum_HR/MyES/ESMain.aspx?model="
print(urlparse(url))

param = {
    "name":"brian.liu",
    "age":18,
}

url = url + urlencode(param)
print(url)

url = "https://www.baidu.com/s?wd=%E5%A4%A7%E7%86%8A%E7%8C%AB"

keyword = "大熊猫"
print(quote(keyword))

