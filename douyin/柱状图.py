import pyecharts.options as opts
from pyecharts.charts import Bar
import pandas as pd

# 读取csv文件
df = pd.read_csv('data.csv')
x = df['地区'].value_counts().index.to_list()
y = df['地区'].value_counts().to_list()

c = (
    Bar()
   .add_xaxis(x)
   .add_yaxis("地区", y)
   .set_global_opts(title_opts=opts.TitleOpts(title="抖音评论地区分布"))
   .render("某视频评论地区分布情况.html")
)