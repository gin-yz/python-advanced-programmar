import requests
import json
str_one = requests.get("https://www.baidu.com").__dict__
print(str_one['status_code'])
for key,values in str_one.items():
    print(key,values)
print(dir(requests.get("https://www.baidu.com")))


print([1]*10)