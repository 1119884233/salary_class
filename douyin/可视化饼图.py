#导入数据处理模块
import pandas as pd
#导入可视化的配置项
from pyecharts import options as opts
#导入可视化饼图
from pyecharts.charts import Pie
#导入可视化数据(随时生成)
from pyecharts.faker import Faker
#读取csv文件
df = pd.read_csv('data.csv')
x = df['地区'].value_counts().index.to_list()
y = df['地区'].value_counts().to_list()


#可视化配置内容
c = (
    Pie()
    .add(
        "",
        [
            list(z)
            for z in zip(
                x,
                y,
            )
        ],
        center=["40%", "50%"],
    )
    #设置可视化标题
    .set_global_opts(
        title_opts=opts.TitleOpts(title="某视频评论地区分布情况"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    #导出可视化效果保存html文件
    .render("抖音评论地区分布情况.html")
)

