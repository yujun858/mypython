# __call__()对象当函数时候触发
# class A():
#     def __call__(self):
#         print('调用对象a')
# a = A()
# a()
# # __str__
# # __repr__

# class Person():
#     def __init__(self):
#         pass
#     def __setattr__(self,name,value):
#         print('设置属性{0}'.format(name))
#         # self.name = value
#         super().__setattr__(name,value)

# p = Person()
# print(p.__dict__)
# p.age = 18

class Person():
    def __init__(self,name,score):
        self._name = name 
        self._score = score
    def __gt__(self,obj):
        print('haha,{0} {1}大吗？'.format(self,obj))
        return self._score > obj._score
    def __str__(self):
        return Person.__name__
p1 =Person('p1',10)
p2 = Person('p2',20)
print(p1>p2)