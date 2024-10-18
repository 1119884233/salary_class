#导入相应的库
import requests

import config.config
from   config import *
import re
#1.获取图片源代码
def get_html(url,headers):
    response = requests.get(url,headers)
#更改编码方式
    response.encoding = "jbk"
    if response.status_code == 200:
        return response.text
    else:
        print("获取源代码错误")
#2.从html中提取图片链接
def parse_img_url(html):
#正则表达式
    pattern=re.compile('"thumbURL": "(.*?)"',re.S)
    items=re.findall(pattern,html)
    return items

def get_img_content(url):
    response = requests.get(url)
    # 更改编码方式
    response.encoding = "jbk"
    if response.status_code == 200:
#3.返回图片的二进制流
        return response.content
    else:
        print("获取源代码错误")

#4.保存图片
def save_img(content,img_name):
    with open(img_name,"wb") as f:
        f.write(content)
        f.close()

def main():
    #输入要抓取的图片名字
    pic_name=input("请输入要抓取的图片内容")
    #初始化图片的名字
    pic_num=0
    url = config.img_url
    headers = config.img_headers
    params=config.params(pic_page,pic_name)
    html = get_html(url,headers)
    img_url=parse_img_url(html)
    for img in img_url:
        pic_num=pic_num+1
        img_content=get_img_content(img)
        img_name=config.img_file+str(pic_num)+".jpg"
        save_img(img_content,img_name)

if __name__ == '__main__':
    main()


