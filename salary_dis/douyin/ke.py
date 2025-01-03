from pyecharts import options as opts
from pyecharts.charts import Graph

# 节点数据
nodes = [
    {"name": "Mlle Gillenormand", "category": 0, "value": 20.457146},
    {"name": "Gavroche", "category": 1},
    {"name": "Eponine", "category": 2},
    {"name": "Cochepaille", "category": 3},
    {"name": "Chenildieu", "category": 4},
    {"name": "Brujon", "category": 5},
    {"name": "Mme Hucheloup", "category": 6},
    {"name": "Myriel", "category": 7},
    {"name": "Valjean", "category": 8},
    # 根据你的实际数据添加更多节点
]

# 连线数据
links = [
    {"source": "Mlle Gillenormand", "target": "Gavroche"},
    {"source": "Mlle Gillenormand", "target": "Eponine"},
    {"source": "Eponine", "target": "Cochepaille"},
    {"source": "Eponine", "target": "Chenildieu"},
    # 根据你的实际数据添加更多连线
]

# 类别数据
categories = [
    {"name": "类别0", "itemStyle": {"color": "blue"}},
    {"name": "类别1", "itemStyle": {"color": "green"}},
    {"name": "类别2", "itemStyle": {"color": "orange"}},
    {"name": "类别3", "itemStyle": {"color": "red"}},
    {"name": "类别4", "itemStyle": {"color": "cyan"}},
    {"name": "类别5", "itemStyle": {"color": "magenta"}},
    {"name": "类别6", "itemStyle": {"color": "yellow"}},
    {"name": "类别7", "itemStyle": {"color": "purple"}},
    {"name": "类别8", "itemStyle": {"color": "pink"}}
]

c = (
    Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
  .add(
        "",
        nodes=nodes,
        links=links,
        categories=categories,
        layout="circular",
        is_rotate_label=True,
        linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3),
        label_opts=opts.LabelOpts(position="right"),
    )
  .set_global_opts(
        title_opts=opts.TitleOpts(title="Graph Example"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="2%", pos_top="20%"),
    )
  .render("graph_example.html")
)