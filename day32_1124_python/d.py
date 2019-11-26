class A():
    name = 18
    def modify(self,name):
        self.name = name
class B(A):
    pass
print(B.__mro__)#查清
# 静态、类方法

# Mixin设计模式：
# 多继承方式对类功能进行扩展。
#　单一功能　
# 可以在不对类进行任何修改情况下，扩充功能

print(A.name)
a = A()
a.modify(19)
print(a.name)
print(A.name)