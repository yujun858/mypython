from threading import Thread
import time
from  multiprocessing import Process

def work():
    print('线程运行程序')
if __name__ == "__main__":
    t = Thread(target= work)
    t.start()
    print('多线程主进程......')
    p =  Process(target=work)
    p.start()
    print('多进程')