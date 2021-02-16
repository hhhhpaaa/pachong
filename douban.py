import requests
from fake_useragent import UserAgent
import re

pingfens = []
names = []
jianjiais = []
times = []
urls = []

url_base = 'https://movie.douban.com/top250?start={}&filter='
for i in range(10):
    urls.append(url_base.format(i*25))

def paqu(url,pingfens,names,jianjiais,times):
    print('正在爬取'+url)
    header = {'User-Agent': UserAgent().chrome,
              'Referer': 'https://movie.douban.com/',
              'Connection': 'keep-alive'
              }
    response = requests.get(url, headers=header)
    response.encoding = 'utf-8'
    info = response.text
    pingfen = re.findall(r'<span class="rating_num" property="v:average">(\S*)</span>', info)
    pingfens.extend(pingfen)
    name =  re.findall(r'<a.*>\s*<span class="title">(.*)</span>',info)
    names.extend(name)
    jianjiai =  re.findall('<span class="inq">(.*)</span>',info)
    jianjiais.extend(jianjiai)
    time = re.findall(r'<br>\s*([0-9]*)',info)
    times.extend(time)
    print('爬取成功')

for url in urls:
    paqu(url,pingfens,names,jianjiais,times)

with open('doubanpaqu.txt','w',encoding='utf-8') as f:
    for name,time,pingfen,jianjiai in zip(names,times,pingfens,jianjiais):
        f.write(name)
        f.write("  ")

        f.write(time)
        f.write("  ")

        f.write(pingfen)
        f.write("  ")

        f.write(jianjiai)
        f.write('\n')

print('写入数据完成')