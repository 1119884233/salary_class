import pymysql
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from config import config
#设置链接
def connect_database():
    host, user, passwd, db = config.mysql_info()
    #连接数据库
    db = pymysql.connect(host=host,user=user,passwd=passwd,db=db)
    # 链接数据库
    db = connect_database()
    #  定义游标
    cursor = db.cursor()
    return cursor

def index(request):
    #获取前端数据
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username)
    print(password)
    return render(request,"index.html")

def register(request):
    #获取注册端的数据
    username = request.POST.get('username')
    email=request.POST.get('email')
    confirmPassword=request.POST.get('confirmPassword')
    password = request.POST.get('password')
    sql="insert into user values ('"+username+"',"+email+"','"+password+"''"+confirmPassword+"'')"

    cursor = connect_database()

    cursor.execute(sql)
    print(username,email,confirmPassword,password)
    return render(request, "register.html")
