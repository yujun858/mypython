# 享元模式;
#　咖啡出售系统
class Coffee():
    name =''
    price=0
    def __init__(self,name):
        self.name =  name
        self.price = len(name)#假设咖啡价格咖啡名字
    def show(self):
        print('Coffee Name: %s Coffee Price %f'%(self.name,self.price))
class Customer():
    name =''
    coffeeFactory = ''
    def __init__(self,name,coffeeFactory):
        self.name = name
        self.coffeeFactory = coffeeFactory
    def order(self,coffee_name):
        print('Customer: %s ordered Coffee: %s'%(self.name,coffee_name))
        return self.coffeeFactory.getCoffee(coffee_name)

class CoffeeFactory():
    coffeeDict ={}
    def getCoffee(self,name):
        if self.coffeeDict.__contains__(name) == False:
            self.coffeeDict[name] = Coffee(name)
        return self.coffeeDict[name]
    def coffeeCount(self):
        print(self.coffeeDict)
        return len(self.coffeeDict)

if __name__ == '__main__':
    coffeeFactory = CoffeeFactory()
    c1 = Customer('YuJUn',coffeeFactory)
    co1 = c1.order('cappuccino')
    co1.show()
    co2 = c1.order('c2')
    co2.show()
    c2 = Customer('YJ',coffeeFactory)
    co3 = c2.order('c3')
    co4 = c2.order('c2')
    print(coffeeFactory.coffeeCount())
