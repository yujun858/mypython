#工厂方法模式
# 学校:　　抽象学校　---> 北京　上海   　　(工厂)
# 课程：   抽象课程 ---> Linux  Python　（产品）
# 学校　：属性：名称，地址，校长 　　方法：　info() enroll(学生注册课程，name,course)
# 课程：　属性：　名称,费用，时间周期，学习类型　方法：enroll_test()

#优点：　创建客户所需要的超，同时还向客户隐藏了哪种具体产品类将被实例化这一细节。
#缺点：　类个数增加，一定程度上增加系统复杂性；
# 针对同一个产品等级(cpu) ,产品族(AMD)
# 抽象工厂模式：
# AMD (主板，芯片组, cpu) 
# Intel(主板，芯片组，cpu)
#如果一个子系统需要一些产品，而这些超属于一个以上产品等级结构，消费产品一方不需要直接参与产品创建，只需要
#公用的工厂接口请求需要产品。
# 类：抽象工厂　：方法：　creatCpu() creatMainborard()
# 类：具体工厂: IntelFactory() AMDFactory()
# 类：产品：不同（Mainboard, Chip, CPU）,相同( 内存,硬盘)
# 起源：　
# 类 ComputerEngineer: 方法：　
class AbstractFactory():
    computer_name = ''
    def createCpu(self):
        pass
    def createMainboard(self):
        pass
class IntelFactory(AbstractFactory):
    computer_name ='Intel I7 series computer'
    def createCpu(self):
        return IntelCpu('I7-6500')
    def createMainboard(self):
        return IntelMainBoard('Intel-6000')
class AMDFactory(AbstractFactory):
    computer_name ='AMD 4 computer'
    def createCpu(self):
        return AMDCpu('I7-6500')
    def createMainboard(self):
        return AMDMainBoard('Intel-6000')
class Cpu():
    pass
class IntelCpu(Cpu):
    def __init__(self,name):
        self.name = name
class AMDCpu(Cpu):
    def __init__(self,name):
        self.name = name
class Mainboard():
    pass
class IntelMainBoard(Mainboard):
    def __init__(self,name):
        self.name = name
class AMDMainBoard(Mainboard):
    def __init__(self,name):
        self.name = name

class ComputerEngineer():
    def makeComputer(self,factory_obj):
        self.prepaerHardwars(factory_obj)
    def prepaerHardwars(self,factory_obj):
        self.computer_name =factory_obj.computer_name
        self.cup = factory_obj.createCpu()
        self.mainboard = factory_obj.createMainboard()
        return "\n--------------\ncomputer [%s] info:\ncpu:%s\nmainboard:%s\n----------------"%(self.computer_name,self.cup.name,self.mainboard.name)

if __name__ == "__main__":
    engineer  = ComputerEngineer()
    intel= IntelFactory()
    amd = AMDFactory()
    print(engineer.prepaerHardwars(intel))
    print(engineer.prepaerHardwars(amd))