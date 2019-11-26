# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         self.setName(self.name)
#     def intro(self):
#         print('Hi,my name is {0}'.format(self.name))
#     def setName(self,name):
#         self.name = name.upper()


# s1 = Student('Liu Ying',19)
# s1.intro()
# hansh
#--------------------------------------------------------
# get 属性
# set 属性
# delete　属性
# 方法一：　 使用类实现描述器
# 使用属性修饰符
# 使用　property 函数：　property(fget,fset,fdel,doc)

class Person():
    '''
    Person 类
    '''
    def fget(self):
        return self._name*2
    def fset(self,name):
        self._name = name.upper()
    def fdel(self):
        self._name = 'NoName'
    name  = property(fget,fset,fdel,'')
p = Person()
p.name = 'Yujun'
print(p.name)
del p.name
print(p.name)
print(Person.__dict__)
print(Person.__bases__)
print(Person.__doc__)