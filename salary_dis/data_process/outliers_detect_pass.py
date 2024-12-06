#导入相应的库
import pandas as pd
import matplotlib.pyplot as plt
#用来设置坐标轴的刻度
from matplotlib.pyplot import MultipleLocator
from config import config

#获取工作列表
job_name = config.job_name

#设置图像显示中文和负号
plt.rcParams['font.sans-serif']=['FangSong']
plt.rcParams['axes.unicode_minus']=False
#遍历所有的文件并找出异常值
for job_file in job_name:
        #读取excel表格数据
        file_name = "../job_data/"+job_file+".xls"
        vars()[file_name] = pd.read_excel(file_name,index_col="max_salary")

        #打印工作类型的统计数据
        print(vars()[file_name].describe())
        print("***************")
        #创建画布,主要用来绘制箱型图，检测异常值
        figure=plt.figure(num="{}".format(job_file))
        #给图像设置一个小标题
        plt.title("{}".format(job_file),fontsize=14,color="blue")

        #设置x轴和y轴的刻度
        y_major_locator=MultipleLocator(20000)
        ax = plt.gca()
        ax.yaxis.set_major_locator(y_major_locator)
        plt.ylim([-2,400000])

        #画箱型图,这里采用DataFrame的方法
        p1 =vars()[file_name].boxplot(return_type="dict",sym="r")
        #为异常值打一个标签
        x = p1['fliers'][0].get_xdata()
        y = p1['fliers'][0].get_ydata()
        #对y的值进行排序
        y.sort()

        #给x轴和y轴各起一个标题
        plt.ylabel("工资分布",fontsize=14,color="blue")
        plt.xlabel("{}异常值检测".format(job_file),fontsize=14,color="blue")

        #对所有点进行添加注释
        for i in range(len(x)):
            if i>0:
                plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.5-0.8/(y[i]-y[i-1]+1),y[i]))
            else:
                plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))

        #打印出了所有的异常值检测
plt.show()


