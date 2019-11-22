#系统中已经存在类库
#简单工厂
class Shape():
    def draw(self):
        raise NotImplementedError
        #如果这个方法不被重构，就抛出错误
class Triangel(Shape):
    def draw(self):
        print('画三角形')
class Square(Shape):
    def draw(self):
        print('画正方形')
class Rectangle(Shape):
   def draw(self):
        print('画矩形')
class Circle(Shape):
    def draw(self):
        print('画圆')

# 普通调用　main: s1 = Triangel() ---> s1.draw()
# 1)假如图形很多，记住大量类图形接口；
# 2)子类决定实类化哪个类；
class ShapeFactory():
    def getShape(self,shape):
        if shape.lower() == 'circle':
            return Circle()
        elif shape.lower == "rectangle":
            return Rectangle()
        else:
            return Square()

class Factory():
    def ProduceShape(self):
        raise NotImplementedError
class CircelFactory(Factory):
    def ProduceShape(self):
        return Circle()
class RectangleFactory(Factory):
    def ProduceShape(self):
        return Rectangle()

if __name__ =='__main__':
#　不用设计模式调用：
    c = Circle()
    c.draw()
    print('----------------------')
# 简单工厂方法
    fac = ShapeFactory()
    shape1 = fac.getShape('circle')
    shape1.draw()
#　优点：
# 缺点：　增加功能需要修改ShapeFactory类；违反了开放封闭原则；
    print('------------------------')
#工厂方法：给每一类图形做一个工厂：多个工厂
    shape = CircelFactory().ProduceShape()
    shape.draw()
# 优点：　可以扩展不用修改已经存在的类