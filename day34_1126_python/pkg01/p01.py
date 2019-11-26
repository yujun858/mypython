class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Info(self):
        print('name:{0},age:{1}'.format(self.name,self.age))