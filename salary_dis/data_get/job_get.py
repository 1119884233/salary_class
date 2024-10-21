import requests
from config import config
import time
import re

# 获取招聘数据源码
def get_data(url,headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(response.status_code)

# 提取详细招聘数据链接
def parse_job_url(html):
    pattern = re.compile(r'"jobHref":"(.*?)"', re.S)
    items = re.findall(pattern, html)
    for item in items:
        print(item)

def main():
    for item in config.job_list:
        for page in range(50):
           time.sleep(10)
           print("正在抓取"+item+"的第 "+str(page+1)+" 页")
           job_url = config.job_url(page,item)
           headers = config.job_headers
           html = get_data(job_url,headers)
           parse_job_url(html)

if __name__ == '__main__':
    main()
