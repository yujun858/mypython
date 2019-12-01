import time
def printTime(f):
    def wrapper(*args,**kwargs):
        print("Time:",time.ctime())
        return f(*args,**kwargs)
    return wrapper

@printTime
def hello():
    print('hello world')

@printTime
def hello2():
    print('还可以自由选择')

def hello3():
    print('我是手动执行的')

if __name__ == '__main__':
    hello() #对扩展开放，对修改封闭；
    hello2()
    hello3 = printTime(hello3)
    hello3()
