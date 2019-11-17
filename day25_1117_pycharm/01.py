class A:
    def show(self):
        print('A')
class B(A):
    #super(A,self).show()
    def show(self):
        super().show()
        print('B')
class Person():
    def __init__(self,name,gender,height,age,mobile,email):
        self.name = name
        self.gender = gender
        self.height = height
        self.age = age
        self.mobile = mobile
        self.email = email
    def run(self):
        print('跑步')

class Chinese(Person):
    def __init__(self,name,gender,height,age,mobile,email):
        Person.__init__(self,name,gender,height,age,mobile,email)
    def say(self):
        print('欢迎来到中国　')
if __name__ == '__main__':
    c = Chinese('aaa','a','b','c','e','f')
    c.say()
    c.run()