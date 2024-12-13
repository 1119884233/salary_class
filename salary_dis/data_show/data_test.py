#本程序主要用来描述matplotlib的具体使用
#导入相应的库
import numpy as np
from matplotlib import pyplot as plt
# 创建一个尺寸为(8,6)，分辨率为100dpi，背景色为青色的画布
# fig=plt.figure(figsize=(8,6),dpi=100,facecolor='m')
# plt.show()



# # 全部用默认值
# fig=plt.figure()
# x=[1,2,3,4,5]
# y=[2,1,3,5,4]
# plt.plot(x,y,color='#A7D676',linestyle='--',marker='*',markerfacecolor='b',markersize=15)
# plt.show() # 每次调用plt.show()方法后，会将所有绘图元素释放出来，所以对元素的修改应该在该方法之前
# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)
# plt.plot(x, y, linestyle='-', color='c')
# plt.title('Line Plot of Sine Function', fontsize=18)
# plt.xlabel('x (radians)')  # 移除loc参数
# plt.ylabel('sin(x)')  # 移除loc参数和不必要的rotation参数（如果设置为0的话）
# plt.grid(axis='y', linestyle='--', color='k', alpha=0.5)
# plt.show()



# x=np.linspace(0,2*np.pi,200)
# y1=np.sin(x)
# y2=np.cos(x)
# fig=plt.figure()
# plt.plot(x,y1,linestyle='-',color='c',label='y=sin(x)') # 该线标记为y=sin(x)
# plt.plot(x,y2,linestyle='--',color='m',label='y=cos(x)') # 该线标记为y=cos(x)
# plt.title('y=sin(x) and y=cos(x)')
# plt.xlabel('x',loc='right')
# plt.ylabel('y',loc='top',rotation=0)
# x_ticks=np.linspace(0,2*np.pi,5)
# x_ticks_labels=['0','π/2','π','3π/2','2π']
# y_ticks=np.linspace(-1,1,5)
# plt.xticks(x_ticks,x_ticks_labels,c='g')
# plt.yticks(y_ticks)
# plt.legend(loc='best')
# plt.grid(linestyle='--',axis='y',alpha=0.5)
# plt.show()



# x = np.linspace(0, 2 * np.pi, 200)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x, y1, linestyle='-', color='c', label='y=sin(x)')  # 绘制正弦曲线
# plt.plot(x, y2, linestyle='--', color='m', label='y=cos(x)')  # 绘制余弦曲线
# plt.title('y=sin(x) and y=cos(x)')  # 设置标题
# plt.xlabel('x')  # 设置x轴标签，移除loc参数
# plt.ylabel('y')  # 设置y轴标签，移除loc参数和rotation参数（因为默认就是0度）
# x = np.linspace(0, 2 * np.pi, 200)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x, y1, linestyle='-', color='c', label='y=sin(x)')
# plt.plot(x, y2, linestyle='--', color='m', label='y=cos(x)')
# plt.title('y=sin(x) and y=cos(x)')
# plt.xlabel('x')  # 正确的调用
# plt.ylabel('y')  # 正确的调用



# x1=np.linspace(0,10,200)
# y1=np.exp(x1)
# x2=np.linspace(0.001,10,200)
# y2=np.log(x2)
# fig=plt.figure()
# ax1=fig.add_subplot()
# ax1.plot(x1,y1,linestyle='-.',color='b',alpha=0.8,label='y=e^x')
# ax1.tick_params(axis='y',labelcolor='b') # 将对应的y轴刻度标签改为对应颜色
# ax2=ax1.twinx()
# ax2.plot(x2,y2,linestyle=':',color='g',alpha=0.8,label='y=ln(x)')
# ax2.tick_params(axis='y',labelcolor='g')  # 将对应的y轴刻度标签改为对应颜色
# plt.title('y=e^x and y=ln(x)')
# plt.show()


# import numpy as np
# # import matplotlib.pyplot as plt
# #
# # fig = plt.figure(facecolor='lightblue')
# #
# # x1 = np.linspace(0, 2 * np.pi, 200)
# # y1 = np.sin(x1)
# # plt.subplot(2, 2, 1)
# # plt.plot(x1, y1, linestyle='-', color='b', label='y=sin(x)')
# # plt.title('y=sin(x)')
# # plt.xlabel('x')  # 移除了 loc 参数
# # plt.ylabel('y')  # 移除了 loc 参数
# # plt.grid(alpha=0.8)
# # x_ticks = np.linspace(0, 2 * np.pi, 5)
# # x_labels = ['0', 'π/2', 'π', '3π/2', '2π']
# # plt.xticks(x_ticks, x_labels)
# # plt.yticks(np.linspace(-1, 1, 5))
# #
# # x2 = np.linspace(0, 2 * np.pi, 200)
# # y2 = np.cos(x2)
# # plt.subplot(2, 2, 2)
# # plt.plot(x2, y2, linestyle='--', color='g', label='y=cos(x)')
# # plt.title('y=cos(x)')
# # plt.xlabel('x')  # 移除了 loc 参数
# # plt.ylabel('y')  # 移除了 loc 参数
# # plt.grid(axis='y', alpha=0.5)
# # plt.xticks(x_ticks, x_labels)
# # plt.yticks(np.linspace(-1, 1, 5))
# #
# # x3 = np.linspace(0, 10, 200)
# # y3 = np.exp(x3)
# # plt.subplot(2, 2, 3)
# # plt.plot(x3, y3, linestyle='-.', color='orange', alpha=0.7, label='y=e^x')
# # plt.title('y=e^x')
# # plt.xlabel('x')  # 移除了 loc 参数
# # plt.ylabel('y')  # 移除了 loc 参数
# #
# # x4 = np.linspace(0.01, 10, 200)
# # y4 = np.log10(x4)
# # plt.subplot(2, 2, 4)
# # plt.plot(x4, y4, linestyle=':', color='r', alpha=0.6, label='y=lg(x)')
# # plt.title('y=lg(x)')
# # plt.xlabel('x')  # 移除了 loc 参数
# # plt.ylabel('y')  # 移除了 loc 参数
# #
# # plt.tight_layout()
# # plt.show()



# fig, ax = plt.subplots(2, 2)  # 这种创建方式会返回fig、ax两个对象，其中ax是一个轴域列表，形状与子图的形状一致
# ax1, ax2, ax3, ax4 = ax.flatten()  # 可以将列表展平后逐个取出
#
# x1 = np.linspace(0, 2 * np.pi, 200)
# y1 = np.sin(x1)
# ax1.plot(x1, y1, label='y=sin(x)')
# ax1.set_title('y=sin(x)')
#
# x2 = np.linspace(0, 2 * np.pi, 200)
# y2 = np.cos(x2)
# ax2.plot(x2, y2, label='y=cos(x)')
# ax2.set_title('y=cos(x)')
#
# x3 = np.linspace(0, 10, 200)
# y3 = np.exp(x3)
# ax3.plot(x3, y3, label='y=e^x')
# ax3.set_title('y=e^x')
#
# x4 = np.linspace(-5, 5, 200)
# y4 = np.power(x4, 2)
# ax4.plot(x4, y4, label='y=x^2')
# ax4.set_title('y=x^2')
#
# plt.tight_layout()
# plt.show()


# fig=plt.figure()
# x1=np.linspace(0,2*np.pi,200)
# y1=np.sin(x1)
# plt.plot(x1,y1)
# plt.title('y=sin(x)')
# x2=np.linspace(0,2*np.pi,200)
# y2=np.cos(x2)
# ax2=fig.add_axes([0.58,0.55,0.25,0.25])
# ax2.set_title('y=cos(x)') # 用轴域绘图时设置标签等方法一般在前面加set
# ax2.plot(x2,y2)           # 如ax.set_xticks()、ax.set_title()等
# plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(1, 6)
# y = np.random.randint(60, 100, 5)
# fig = plt.figure()
# plt.bar(x, y, color=['c', 'm', 'r', 'g', 'b'], width=0.5, alpha=0.5)
# plt.title('Revenue-Month Plot')
# plt.xlabel('month')  # 移除了 loc 参数
# plt.ylabel('revenue')  # 移除了 loc 参数
# plt.show()


#3.8 簇状条形图
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(1, 6)
# x_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
# data_Tom = np.random.randint(60, 100, size=5)
# data_Jack = np.random.randint(60, 100, size=5)
# data_Wilson = np.random.randint(60, 100, size=5)
#
# fig = plt.figure()
# width = 0.3
#
# # 绘制分组条形图
# plt.bar(x - width, data_Tom, color='#D98481', width=width, label='Tom')
# plt.bar(x, data_Jack, color='#91B5A9', width=width, label='Jack')
# plt.bar(x + width, data_Wilson, color='#EDCA7F', width=width, label='Wilson')
#
# # 设置标题和坐标轴标签（移除了 loc 参数）
# plt.title('Revenue-Month Plot')
# plt.xlabel('Month')
# plt.ylabel('Revenue')
#
# # 设置 x 轴刻度标签
# plt.xticks(x, x_labels)
#
# # 添加图例
# plt.legend(loc='best')
#
# # 显示图形
# plt.show()


#3.9堆叠图
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(4)
# x_labels = ['Tom', 'Jack', 'Mike', 'John']
# data_Jan = np.random.randint(60, 100, size=4)
# data_Feb = np.random.randint(60, 100, size=4)
# data_Mar = np.random.randint(60, 100, size=4)
#
# fig = plt.figure()
#
# # 绘制堆叠条形图
# plt.bar(x, data_Jan, color='#D98481', label='Jan')
# plt.bar(x, data_Feb, color='#91B5A9', bottom=data_Jan, label='Feb')
# plt.bar(x, data_Mar, color='#EDCA7F', bottom=np.array(data_Jan) + np.array(data_Feb), label='Mar')
#
# # 设置标题和坐标轴标签（移除了 loc 参数）
# plt.title('Revenue-Staff Plot')
# plt.xlabel('Staff')
# plt.ylabel('Revenue')
#
# # 设置 x 轴刻度标签
# plt.xticks(x, x_labels)
#
# # 添加图例
# plt.legend(loc='best')
#
# # 显示图形
# plt.show()

#3.10横向条形图
x=np.arange(5)
y=np.random.randint(50,100,size=5)
fig=plt.figure()
plt.barh(x,y,color=['b','g','r','c','m'],alpha=0.5)
plt.title('Horizontal Bar Plot')
plt.xlabel('y',loc='right')
plt.ylabel('x',loc='top')
plt.show()