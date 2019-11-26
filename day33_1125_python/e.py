import abc #abstract class
# 声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def smoking(self):
        pass

class A():
    pass
def say(self):
    print('saying')
A.say = say #函数名称当变量使用
a = A()
a.say()

#绑定对象
from types import MethodType
a = A()
a.say = MethodType(say,A)
a.say()

# 借助type实现组装类
def say(self):
    print('Saying......')
def talk(self):
    print('Talking......')
A = type('AName',(object,),{'class_say':say,'class_talk':talk})
a = A()
print(dir(a))

# 利用元类实现  MetaClass
class TulingMetaClass(type):
    def __new__(cls,name,bases,attrs):
        print('haha 元类')
        attrs['id'] = '0000000'
        attrs['addr'] = '北京海淀'
        return type.__new__(cls,name,bases,attrs)
class Teacher(object,metaclass=TulingMetaClass):
    pass
t = Teacher()
print(t.id,t.addr)