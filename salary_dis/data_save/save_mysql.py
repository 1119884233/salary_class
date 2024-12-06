#导入相应的库

import pymysql
from config import config

#定义函数连接数据库
def connect_database():
    host, user, passwd, db = config.mysql_info()
    #连接数据库
    db = pymysql.connect(host=host,user=user,passwd=passwd,db=db)
    return db

#创建数据表
# def create_table(job_name):
#     #链接数据库
#     db=connect_database()
#     #  定义游标
#     cursor = db.cursor()
#     #编写sql语言创建数据表
#     sql_create_table = "create table "+job_name+"(job_name varchar(200) NULL,job_address varchar(200) NULL,degree varchar(200) NULL,company_name varchar(200) NULL,job_requirement varchar(5000) NULL,min_salary int(10) NULL,max_salary int(10) NULL,salary int(10) NULL);"
#     #执行sql语句
#     cursor.execute(sql_create_table)

#执行sql语句
def insert_data(job_list,job_info):
    #  连接数据库
    db = connect_database()
    #  定义游标
    cursor = db.cursor()
    #  定义创建数据表的sql语言
    sql_insert = "insert into "+job_list+"(job_name,job_address,degree,company_name,job_requirement,max_salary,min_salary) values ('"+job_info[0]+"','"+job_info[1]+"','"+job_info[2]+"','"+job_info[3]+"','"+job_info[4]+"','"+job_info[5]+"','"+job_info[6]+"');"
    print(sql_insert)
    #  执行sql语言
    cursor.execute(sql_insert)
    #执行推送结果
    db.commit()





