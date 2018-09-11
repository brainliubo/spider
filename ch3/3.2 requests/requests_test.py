import  requests

r = requests.get("http://www.baidu.com/")
print(type(r))
print(r.cookies)
print(r.status_code)
print(r.content)
print((r.text))

