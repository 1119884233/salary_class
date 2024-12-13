#本程序主要用来描述matplotlib的具体使用
#导入相应的库
import numpy as np
from matplotlib import pyplot as plt
# 创建一个尺寸为(8,6)，分辨率为100dpi，背景色为青色的画布
fig1=plt.figure(figsize=(15,15))

x=[1.5,2.5,3.5,4.5,5]
y=[5,4,3,2,5]

x1=[1.5,2.5,3.5,4.5,5]
y1=[1,3,4,2,3]

x2=[1.5,2.5,3.5,4.5,5]
y2=[2,6,1,3,1]

x3=[1.5,2.5,3.5,4.5,5]
y3=[1,2,5,4,1]

x4=[1.5,2.5,3.5,4.5,5]
y4=[2,4,3,2,1]

plt.plot(x,y,linestyle='-',marker='o',markerfacecolor='r',markersize=10)
plt.plot(x1,y1,linestyle='-',marker='1',markerfacecolor='b',markersize=15)
plt.plot(x2,y2,linestyle='-',marker='2',markerfacecolor='m',markersize=15)
plt.plot(x3,y3,linestyle='-',marker='*',markerfacecolor='k',markersize=10)
plt.plot(x4,y4,linestyle='-',marker='4',markerfacecolor='y',markersize=10)

#正弦函数
fig2=plt.figure(figsize=(15,15))
x = np.linspace(0, 2 * np.pi, 200)
y1 = np.sin(x)
plt.plot(x, y1, linestyle='-', color='c', label='y=sin(x)')
# 该线标记为y=sin(x)
plt.title('y=sin(x)')
plt.xlabel('x', loc='right')
plt.ylabel('y', loc='top', rotation=0)
x_ticks = np.linspace(0, 2 * np.pi, 5)
x_ticks_labels = ['0', 'π/2', 'π', '3π/2', '2π']
y_ticks = np.linspace(-1, 1, 5)
plt.xticks(x_ticks, x_ticks_labels, c='g')
plt.yticks(y_ticks)
plt.legend(loc='best')
plt.grid(linestyle='--', axis='y', alpha=0.5)

#余弦函数
fig3=plt.figure(figsize=(15,15))
y2 = np.cos(x)
plt.plot(x, y2, linestyle='--', color='m', label='y=cos(x)')
# 该线标记为y=cos(x)
plt.title('y=cos(x)')
plt.xlabel('x', loc='right')
plt.ylabel('y', loc='top', rotation=0)
x_ticks_labels = ['0', 'π/2', 'π', '3π/2', '2π']
y_ticks = np.linspace(-1, 1, 5)
plt.xticks(x_ticks, x_ticks_labels, c='g')
plt.yticks(y_ticks)
plt.legend(loc='best')
plt.grid(linestyle='--', axis='y', alpha=0.5)






# 创建一个画布
# fig6, ax = plt.subplots(figsize=(10, 10))
# # 生成x轴的数据
# x = np.linspace(0, 2*np.pi, 200)
# # 定义五条不同的y轴数据
# y = np.sin(x)
# lines=[ ax.plot(x, y, label='sin(x)', color='k', linestyle='-', marker='o')[0]]
# # 设置图表的标题和坐标轴标签
# ax.set_title('sinx')
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# # 添加图例
# ax.legend()
# # 显示网格线
# ax.grid(True)

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
# fig = plt.figure(facecolor='lightblue')
#
# x1 = np.linspace(0, 2 * np.pi, 200)
# y1 = np.sin(x1)
# plt.subplot(2, 2, 1)  # 一共2×2个子图，此为第一个
# plt.plot(x1, y1, linestyle='-', color='b', label='y=sin(x)')
# plt.title('y=sin(x)')
# plt.xlabel('x', loc='right')
# plt.ylabel('y', loc='top')
# plt.grid(alpha=0.8)
# x_ticks = np.linspace(0, 2 * np.pi, 5)
# x_labels = ['0', 'π/2', 'π', '3π/2', '2π']
# plt.xticks(x_ticks, x_labels)
# plt.yticks(np.linspace(-1, 1, 5))
#
# x2 = np.linspace(0, 2 * np.pi, 200)
# y2 = np.cos(x2)
# plt.subplot(2, 2, 2)  # 一共2×2个子图，此为第二个
# plt.plot(x2, y2, linestyle='--', color='g', label='y=cos(x)')
# plt.title('y=cos(x)')
# plt.xlabel('x', loc='right')
# plt.ylabel('y', loc='top')
# plt.grid(axis='y', alpha=0.5)
# plt.xticks(x_ticks, x_labels)
# plt.yticks(np.linspace(-1, 1, 5))
#
# x3 = np.linspace(0, 10, 200)
# y3 = np.exp(x3)
# plt.subplot(2, 2, 3)  # 一共2×2个子图，此为第三个
# plt.plot(x3, y3, linestyle='-.', color='orange', alpha=0.7, label='y=e^x')
# plt.title('y=e^x')
# plt.xlabel('x', loc='right')
# plt.ylabel('y', loc='top')
#
# x4 = np.linspace(0.01, 10, 200)
# y4 = np.log10(x4)
# plt.subplot(2, 2, 4)  # 一共2×2个子图，此为第四个
# plt.plot(x4, y4, linestyle=':', color='r', alpha=0.6, label='y=lg(x)')
# plt.title('y=lg(x)')
# plt.xlabel('x', loc='right')
# plt.ylabel('y', loc='top')
#
# plt.tight_layout()  # 自动调整布局（紧凑布局）



plt.show()