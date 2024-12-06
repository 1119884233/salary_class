import requests
from config import config
import time
import re
from data_save import save_neo4j

# 获取招聘数据源码
def get_data(url,headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(response.status_code)

# 解析详细招聘数据
def parse_job_url(html):
    pattern = re.compile(r'"jobName":"(.*?)".*?"cityString":"(.*?)".*?"degreeString":"(.*?)".*?"fullCompanyName":"(.*?)".*?"jobDescribe":"(.*?)".*?"jobSalaryMax":"(.*?)".*?"jobSalaryMin":"(.*?)"', re.S)
    items = re.findall(pattern, html)
    return items

def main():
    #  链接neo4j数据库
    graph_neo4j = save_neo4j.connect_to_neo4j()

    for item in config.job_list:
        #  调用函数创建工作种类节点
        create_job_type_node = save_neo4j.create_job_type_node(item)
        graph_neo4j.run(create_job_type_node)

        #  开始抓取数据并保存在数据库中
        for page in range(20):
               time.sleep(2)
               print("正在抓取"+str(item)+"的第 "+str(page+1)+" 页")
               job_url = config.job_url(page,item)
               headers = config.job_headers
               html = get_data(job_url,headers)
               job_detail = parse_job_url(html)
               for job in job_detail:
                   if item in str(job[0]).lower():
                       print(job[0])
                       try:
                        # 调用Cypher语言创建节点
                        create_job_info_node, create_relationship = save_neo4j.create_node_and_relationship(item, job[0])
                        graph_neo4j.run(create_job_info_node)
                        graph_neo4j.run(create_relationship)
                       except:
                            print("数据存储异常")

if __name__ == '__main__':
    main()
