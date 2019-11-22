#建造者模式：
#　复杂对象构建与表示分离，同样构建过程可以创建不同表示。
# 　抽象，重写具体建造者就可以了：
#  人类： -->（白人）（黑人）
# 　建造者（指挥者）

class PersonBuilder():
    def BuildHead(self):
        pass
    def BuildBody(self):
        pass
    def BuildArm(self):
        pass
class PersonFatBuild(PersonBuilder):
    xtype = '胖子　'
    def BuildArm(self):
        print('创建%s手臂'%self.xtype)
    def BuildBody(self):
        print('创建%s身体'%self.xtype)
    def BuildHead(self):
        print('创建%s头'%self.xtype)

class PersonThitBuild(PersonBuilder):
    xtype = '瘦子'
    def BuildArm(self):
        print('创建%s手臂'%self.xtype)
    def BuildBody(self):
        print('创建%s身体'%self.xtype)
    def BuildHead(self):
        print('创建%s头'%self.xtype)

class PersonDirector():
    pb = None
    def __init__(self,pb):
        self.pb = pb
    def CreatePerson(self):
        self.pb.BuildArm()
        self.pb.BuildBody()
        self.pb.BuildHead()
if __name__ == '__main__':
    pb = PersonFatBuild()
    pd = PersonDirector(pb)
    pd.CreatePerson()

