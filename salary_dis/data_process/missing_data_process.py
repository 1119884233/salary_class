#python实现使用拉格朗日插值法，对已经进行异常值过滤的文件进行插值
#导入相应的包
import pandas as pd
import warnings
from config import config
from lg_use import ployinterp_column
warnings.filterwarnings("ignore")

#定义文件列表
tables_list = config.job_name
#构建循坏,依次遍历各个文件
for file in tables_list:
    #指定要输入的文件名字
    file_name = "../job_data/{}.xls".format(file)

    #指定插完值后的文件存储路径
    output_file = "../data_result/{}.xls".format(file)
    print(output_file)

    #提取每个表中的数据
    data = pd.read_excel(file_name)

    #依次遍历Excel表中的每一行数据
    for i in data.columns:
        for j in range(len(data)):
            #进行检测看是否有空值，有空值就进行插值
            if (data[i].isnull())[j]:
                data[i][j] = ployinterp_column(data[i],j)

    #再讲插值的结果储存到文件中
    data.to_excel(output_file)

