import  requests

# r = requests.get("http://www.baidu.com/")
# print(type(r))
# print(r.cookies)
# print(r.status_code)
# print(r.content)
# print((r.text))

data = {
    "name":"brain.liu",
    "age": 33
}
r = requests.get("https://www.12306.cn",verify = True)
print(r.status_code)
print((r.cookies.items()))
print(r.cookies)

# r = requests.get("https://github.com/favicon.ico")
# with open("github_ico.ico","wb") as f:
#     f.write(r.content)

