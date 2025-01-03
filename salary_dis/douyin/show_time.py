import pandas as pd
import matplotlib.pyplot as plt


# 定义一个绘图函数
def plot_bar(data, title, xlabel, ylabel, top_n=None, color='skyblue', grid=True):
    plt.figure(figsize=(10, 6))
    if top_n:
        data = data.head(top_n)
    data.plot(kind='bar', color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    if grid:
        plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


# 读取 CSV 数据
try:
    df = pd.read_csv('data.csv')
except FileNotFoundError:
    print("CSV文件未找到，请检查文件路径。")
    exit()
except pd.errors.EmptyDataError:
    print("CSV文件为空，请检查文件内容。")
    exit()
except pd.errors.ParserError:
    print("CSV文件格式错误，请检查文件是否损坏。")
    exit()

# 检查数据结构
print(df.head())

# 1. 地区分布可视化
region_counts = df['地区'].value_counts()
plot_bar(region_counts, '各地区评论数量分布', '地区', '评论数量', grid=True)

# 2. 昵称分布可视化
nickname_counts = df['昵称'].value_counts()
# 这里可以考虑使用词云等其他可视化方式，但这里仍然使用条形图作为示例
plot_bar(nickname_counts, '评论最多的昵称', '昵称', '评论数量', top_n=20, color='lightgreen', grid=True)
