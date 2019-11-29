# 例1： 计算一个数字×100. a_01.py
#     - 例2： 多个参数x,y,z ->100x+10y+z a_01.py
# 2. 高阶函数:把函数作为参数使用函数。
#     - 例3： 函数名称就是变量 b_01.py
#     - 例4： 写一个高阶函数   b_01.py
#     - 例5： 系统定义高阶函数map b_02.py
#     - 例6： 系统定义reduce减少例如list数据求和 b_03.py
from functools import reduce
def funA(n):
    return n*100
def funB(n,f):
    return f(n)*3
def add(a,b):
    return a+b
def mapF():
    l1 = [i for i in range(10)]
    r1 = map(funA,l1)
    l2 = [i for i in list(r1)]
    return l2
def reduceF():
    l1 = [i for i in range(10)]
    r2 = reduce(add , l1)
    return r2
if __name__ == "__main__":
    print(funB(10,funA))
    print(mapF())
    print(reduceF())