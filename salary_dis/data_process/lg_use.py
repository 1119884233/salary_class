#调用scipy中的larange函数，进行拉格朗日插值法的应用
from scipy.interpolate import lagrange


#构建拉格朗日函数，使其对缺失值进行处理
def ployinterp_column(s,n,k=1):
    y=s.reindex(list(range(n-k,n))+list(range(n+1,n+1+k)))
    y=y[y.notnull()]
    return int(abs(lagrange(y.index,list(y))(n)))
