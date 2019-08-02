# webPictures.py
# 这份代码的with…as….语句中的f.close()可以不用加上，该语句会进行相关的文件关闭的处理的。
# 涉及到的OS标准库在pythonMOOC中会讲到，不了解的同学可以查询python官方文档或者菜鸟教程，不在此处赘述，

import requests
import os

url = "http://www.nationalgeographic.com.cn/photography/photo_of_the_day/3921.html"
root = "D://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件以及存在")
except:
    print("爬取成功")
