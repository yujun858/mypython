class Animal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print('----Animal----')

class Dog(Animal):
    # def __init__(self):
    #     print('----Dog----')
    def __init__(self):
        super().__init__('a','b')
d = Dog()
print(d.a)