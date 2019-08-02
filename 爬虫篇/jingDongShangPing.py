# jingDongShangPin.py

import requests

url = "https://item.jd.com/2967929.html"
try: # 如果对try-except不熟悉的同学，这里可以简单的把它理解成判断语句
    r = requests.get(url) # 获取指定URL链接的页面
    r.raise_for_status() # 如果不是200，产生requests.HTTPError
    r.encoding = r.apparent_encoding # r.apparent_encoding是根据网页内容“实实在在”地分析出来的编码方式，r.encoding为从HTTPheader中猜测的响应内容编码方式
    print(r.text[:1000]) # 获取文本中前1000个字符
except:
    print("爬取失败")