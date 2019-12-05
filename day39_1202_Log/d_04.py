import time
import threading

def loop1():
    print('Start loop 1 at: ',time.ctime())
    time.sleep(4)
    print('End loop 1 at:',time.ctime())

def loop2():
    print('Start loop 2 at: ',time.ctime())
    time.sleep(2)
    print('End loop 2 at: ',time.ctime())

def loop3():
    print('Start loop 3 at:',time.ctime())
    time.sleep(5)
    print('End loop 3 at: ', time.ctime())

def main():
    print('Starting at : ',time.ctime())
    t1 = threading.Thread(target=loop1,args=())
    t1.setName('THR_1')
    t1.start()

    t2 = threading.Thread(target=loop2,args=())
    t2.setName('THR_2')
    t2.start()

    t3 = threading.Thread(target=loop3,args=())
    t3.setName('THR_3')
    t3.start()

    time.sleep(3)

    for thr in threading.enumerate():
        print('正在运行线程:{0}'.format(thr.getName()))
    print('正在运行子线程数量: {0}'.format(threading.activeCount()))
    
    print('All done at: {0}'.format(time.ctime()))

if __name__ =='__main__':
    main()