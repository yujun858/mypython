from threading import Thread
import time
#开启线程方式一：
def hello(name):
    time.sleep(2)
    print('say hello %s'%name)

# 开启线程方式二
class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        time.sleep(2)
        print('say hello %s'%self.name)

if __name__ == "__main__":
    t = Thread(target=hello,args=('nihao',))
    t.start()
    print('主线程')
    print('-----------------')
    t2 = MyThread('yJ')
    t2.start()
    print('主线程')    