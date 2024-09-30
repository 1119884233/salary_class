#导入相应的库
import requests

import config.config
from   config import *

#获取源代码
def get_html(url,headers):
    response = requests.get(url,headers)
#更改编码方式
    response.encoding = "jbk"
    if response.status_code == 200:
        return response.text
    else:
        print("获取源代码错误")

def main():
    url = config.url_html
    headers = config.headers
    html = get_html(url,headers)
    print(html)

if __name__ == '__main__':
    main()

