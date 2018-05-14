import re
import urllib.request

count = 0
url_dic = {}
with open('G:\my\kuc\crawled.txt', 'r') as datafile:
    for i in range(600):
        try:
            link = datafile.readline()
            print(str(link))
            response = urllib.request.urlopen(str(link))
            html = response.read()
            fp = open(str(count) + ".htm", "w+b")  # 打开一个文本文件
            fp.write(html)  # 写入数据
            fp.close()
            url_dic[count] = str(link)
            count = count + 1
        except:
            continue
datafile.close()

