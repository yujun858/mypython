class A():
    name ='bbb'
    age = 18
    def __init__(self):
        self.name = 'aaa'
        self.age = 200
    def say(self):
        print(self.name)
        print(self.age)
class B():
    name ='ccc'
    age =19
a = A()
a.say()
print('------------')
A.say(a)
print('---------------')
A.say(A)
print('--------------')
A.say(B)
# 鸭子模型：
