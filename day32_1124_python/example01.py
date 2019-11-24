class A():
    name  = 'dana'
    age = 18
    def say(self):
        self.name = 'aaaa'
        self.age = 200
        print('My age is {0}'.format(__class__.age))
    def speak():#绑定类的函数
        #访问类中成员
        print(__class__.name)
        print(__class__.age)

print(A.__dict__)
# 通过对象对类中成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，二不会修改类的成员。
s1 = A()
s2 = A()
s1.name = 'dana2'
print(s2.name)
yueyue = A()
print(yueyue.__dict__)
yueyue.say()
A.speak()
#yueyue.speak()


