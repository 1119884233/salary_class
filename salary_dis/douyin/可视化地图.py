# 导入数据处理模块
import pandas as pd
# 导入可视化的配置项
from pyecharts import options as opts
# 导入可视化地图
from pyecharts.charts import Map
# 导入可视化数据(随时生成)
from pyecharts.faker import Faker

# 读取csv文件
df = pd.read_csv('data.csv', encoding='gbk')
# 获取省份（或地区）列表
provinces = df['地区'].to_list()
# 这里假设你想要统计每个地区出现的次数作为数值
values = df['地区'].value_counts().to_list()

# 可视化配置内容
c = (
    Map()
 .add(
        "",
        [list(z) for z in zip(provinces, values)],
        "china"
    )
    # 设置可视化标题
 .set_global_opts(
        title_opts=opts.TitleOpts(title="地区分布情况"),
        legend_opts=opts.LegendOpts(type_="scroll", pos_left="80%", orient="vertical")
    )
 .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    # 导出可视化效果保存html文件
 .render("地区分布图.html")
)
print(provinces)
print(values)