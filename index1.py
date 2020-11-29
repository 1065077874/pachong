# -*- coding: utf-8 -*-
# 开发人：方路
# 开发时间：2020/11/4 15:57
# -*- coding: utf-8 -*-
# 开发人：方路
# 开发时间：2020/11/4 10:29


import requests
import re
from bs4 import BeautifulSoup
import os

def main():
    a = os.path.exists('D:\photo')
    if not a:
        os.makedirs('D:\photo')
        print('D:\photo' + ' 创建成功')
    else:
        print('D:\photo' + ' 已存在')
    findimg = re.compile(r'<a class="preview" href="(.*)" target="_blank"></a>')
    findimg1 = re.compile(r'id="wallpaper" src="(.*)"')
    a = input('请输入你要爬取多少页,注意必须为数字')
    mainurl = 'https://wallhaven.cc/search?q=DARKER%20THAN%20BLACK&page='
    for c in range(0,int(a)):
     url = mainurl + str(c)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58'}
    r = requests.get(url, headers=headers)
    r.encoding='utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    for item in soup.find_all(attrs={'class':'preview'}):
        a = re.findall(findimg, str(item))
        r1 = requests.get(a[0], headers=headers)
        r1.encoding='utf-8'
        soup1 = BeautifulSoup(r1.text, 'html.parser')
        for item1 in soup1.find_all(attrs={'class': 'scrollbox'}):
            a1 = re.findall(findimg1, str(item1))
            name = a1[0]
            r1 = requests.get(a1[0], headers=headers)
            with open(r'D:\photo\%s'% name[-10:], "wb")as f:
                 f.write(r1.content)

if __name__ == '__main__':
    main()
