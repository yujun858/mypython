#　GUI 继承
from tkinter import *
from tkinter.ttk import *

# 创建　GUI　基类
class GUIBase():
    def __init__(self):
        self.frame = Tk()
        self.frame.geometry('800x600+600+100')
        self.frame.resizable(0,0)
        self.frame['bg'] = 'lightgray'
        #关闭按钮
        self.Button_close = Button(self.frame,text='关闭',width =10,command = self.close)
        self.Button_close.place(x=480,y=550)
    def show(self):
        self.frame.mainloop()
    def close(self):
        self.frame.destroy()
if __name__ == '__main__':
    this = GUIBase()
    this.show()

