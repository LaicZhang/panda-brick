# AmazonShangPin.py
# 未注释部分可以参考例1
# 此例的调试方法可以参考：可输出r.request.headers查看headers

import requests

url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers = kv) # 假装我是个好人，修改headers以让程序模拟浏览器获取数据。
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")