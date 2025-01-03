# 导入自动化模块的安装：需要安装 pip install DrissionPage
from DrissionPage import ChromiumPage
# 导入时间转换模块
from datetime import datetime
# 导入csv模块，用于操作CSV文件
import csv
# 导入格式化输出模块
from pprint import pprint

# 使用with语句管理文件资源，自动关闭文件
with open('data.csv', mode='w', encoding='GBK', newline='') as f:
    # 创建字典写入对象，指定表头字段
    csv_writer = csv.DictWriter(f, fieldnames=['昵称', '地区', '日期', '评论'])
    # 写入表头
    csv_writer.writeheader()

    # 打开浏览器（实际浏览对象）
    dp = ChromiumPage()
    # 监听数据包
    dp.listen.start('comment/list/')
    # 访问网站
    dp.get('https://www.douyin.com/video/7444572344439541042')

    # 构建循坏翻页，从第1页到第20页（左闭右开区间，所以是1到21）
    for page in range(1, 28):
        print(f'正在采集{page}页的数据内容')

        # 等待数据包加载
        resp = dp.listen.wait()

        # 获取响应数据
        try:
            json_data = resp.response.body
            # 解析数据，获取评论信息所在的列表
            try:
                comments = json_data['comments']
            except KeyError as e:
                print(f"获取评论列表出现异常，异常信息：{e}")
                comments = []
            # 遍历评论列表，提取每条评论具体数据信息
            for index in comments:
                try:
                    create_time = index['create_time']
                    date = str(datetime.fromtimestamp(create_time))
                    # 尝试获取地区信息，先从ip_label获取，若不存在则尝试从client_info中获取省份信息
                    try:
                        region = index['ip_label']
                    except KeyError:
                        ip_client_info = index.get('client_info', {})
                        region = ip_client_info.get('province', '未知') if ip_client_info else '未知'
                except KeyError as e:
                    print(f"处理单个评论数据出现异常，异常信息：{e}，当前评论数据：{index}")
                    continue
                dit = {
                    '昵称': index['user']['nickname'],
                    '地区': region,
                    '日期': date,
                    '评论': index['text'],
                }
                try:
                    csv_writer.writerow(dit)
                    print(dit)
                except Exception as e:
                    print(f"写入CSV文件出现异常，异常信息：{e}，当前数据：{dit}")

                # 查找下一页元素，判断是否存在
                next_page = dp.ele('css:.Rcc71LyU')
                if next_page:
                    dp.scroll.to_see(next_page)
                else:
                    print("未找到下一页元素，可能已到达最后一页或者页面结构有变化")
        except Exception as e:
            print(f"整体页面数据处理出现异常，异常信息：{e}")