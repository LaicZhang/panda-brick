# keywordSubmit.py
# 因为百度和360搜索的代码类似，故只给出百度搜索关键词提交代码
# 小提示：此代码只需修改两个地方即可变为360搜索代码，请开始你的表演
import requests

keyword = "python"
try:
    kv = {'wd':keyword}
    r = requests.get('http://www.baidu.com/s', params= kv) # params为字典或字节序列，作为参数增加到url中
    print(r.request.url) # 输出结果页面的URL链接
    r.raise_for_status()
    print(len(r.text)) # 输出结果文本长度，len()函数返回对象（字符、列表、元组等）长度或项目个数。
except:
    print("爬取失败")
