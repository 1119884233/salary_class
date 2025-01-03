# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 读取CSV文件
# df = pd.read_csv('data.csv',encoding="GBK")
#
# # 按地区统计评论数量
# region_count = df['地区'].value_counts()
#
# # 绘制柱状图
# plt.bar(region_count.index, region_count.values)
# plt.xlabel('地区')
# plt.ylabel('评论数量')
# plt.title('抖音评论数量按地区分布')
# plt.xticks(rotation=45)
# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 读取CSV文件
# df = pd.read_csv('data.csv',encoding="GBK")
#
# # 将日期列转换为日期时间类型
# df['日期'] = pd.to_datetime(df['日期'])
#
# # 按日期统计评论数量
# date_count = df['日期'].value_counts().sort_index()
#
# # 绘制折线图
# plt.plot(date_count.index, date_count.values)
# plt.xlabel('日期')
# plt.ylabel('评论数量')
# plt.title('抖音评论数量按日期分布')
# plt.xticks(rotation=45)
# plt.show()
import json
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Graph

# 读取抖音评论数据
df = pd.read_csv('data.csv',encoding="GBK")

# 提取评论者和地区信息
data = df[['评论', '地区']]

# 构建节点和链接数据
nodes = []
links = []
node_set = set()
node_index = {}
index = 0
for _, row in data.iterrows():
    commenter = row['评论']
    region = row['地区']
    if commenter not in node_set:
        node_set.add(commenter)
        nodes.append({"name": commenter, "category": region})
        node_index[commenter] = index
        index += 1
    for _, row2 in data.iterrows():
        commenter2 = row2['评论']
        region2 = row2['地区']
        if commenter!= commenter2 and region == region2:
            links.append({"source": node_index[commenter], "target": node_index[commenter2]})

categories = list(set([node['category'] for node in nodes]))
category_mapping = {category: index for index, category in enumerate(categories)}
for node in nodes:
    node['category'] = category_mapping[node['category']]

c = (
    Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
   .add(
        "",
        nodes=nodes,
        links=links,
        categories=[{"name": category} for category in categories],
        layout="circular",
        is_rotate_label=True,
        linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
        label_opts=opts.LabelOpts(position="right"),
    )
   .set_global_opts(
        title_opts=opts.TitleOpts(title="Graph - 抖音评论关系"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
    )
   .render("graph_douyin_commenters.html")
)