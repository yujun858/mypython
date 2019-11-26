class Person():
    def eat(self):
        print(self)
        print('Eating......')
    @classmethod
    def play(cls):
        print(cls)
        print('Playing.....')
    @staticmethod
    def say():
        print('Saying......')
yueyue = Person()
yueyue.eat()
yueyue.play()
yueyue.say()