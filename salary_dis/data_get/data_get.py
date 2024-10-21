import requests

# 1.获取html代码
def get_data(url,headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(response.status_code)

#2.获取二进制流
def get_content(url,headers):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        # 返回图片的二进制流
        return response.content
    else:
        print(response.status_code)

#3.获取二进制流,不需要头部的信息
def get_content_no_headers(url):
    response = requests.get(url)
    if response.status_code == 200:
        # 返回图片的二进制流
        return response.content
    else:
        print(response.status_code)