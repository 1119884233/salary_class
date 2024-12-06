import requests
from config import config1
import re
import os


from config.config import params


# 获取百度图片的html代码
def get_data(url,headers,params):
    response = requests.get(url, headers=headers,params=params)
    if response.status_code == 200:
        return response.text
    else:
        print(response.status_code)

# 从html代码中提取图片链接
def parse_img_url(html):
    # 写正则表达式
    pattern = re.compile('"thumbURL":"(.*?)"',re.S)
    items = re.findall(pattern, html)
    return items

# 获取图片的二进制流
def get_img_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        # 返回图片的二进制流
        return response.content
    else:
        print(response.status_code)

# 保存图片
def save_img(content,img_name):
    with open(img_name,"wb") as f:
        f.write(content)
        f.close()

#创建文件夹
def create_new_file(file_name):
    os.mkdir(config1.img_file+file_name)
def main():

   # 输入要抓取的图片名字
   pic_name = input("请输入要抓取的图片内容：")
   # 创建文件夹
   create_new_file(pic_name)
   # 初始化图片的名字
   pic_num = 0
   # 初始化图片页数
   pic_page = 0

   for i in range(10):
       print("************正在抓取第 "+str(i+1)+" 页的图片******************")
       # 引用加载头
       pic_page = pic_page + 1
       url,headers,params = config1.pic_params(str(pic_page*30),pic_name)
       print(url)
       # 获取图片源代码
       data = get_data(url,headers,params)
       # print(data)
       # 获取图片链接
       img_url = parse_img_url(data)
       # print(img_url)
       for img in img_url:
           pic_num = pic_num+1
           # print(pic_num)
           img_content = get_img_content(img)
           img_name = config1.img_file+pic_name+"/"+str(pic_num)+".jpg"
           save_img(img_content,img_name)

if __name__ == '__main__':
    main()