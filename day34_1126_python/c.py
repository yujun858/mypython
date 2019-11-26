# 自定义异常

class :
    pass


try:
    num = input('Plz input num:')
    result = 100/int(num)
    print('result {0}:'.format(result))
    raise ValueError
    print('还没有结束')
except ZeroDivisionError as e: #异常是类，实例化
    print(e)
except Exception as e:
    print('有异常')