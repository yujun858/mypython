#图形操作,
from tkinter import *
class Array():
    def __init__(self):
        self.list01 =[[1,2,3],[4,5,6],[7,8,9]]
    def print(self):
        for row in range(len(self.list01)):
            for col in range(len(self.list01[row])):
                print(self.list01[row][col],end='\t')
            print()# 换行
    def right_rotate(self):
        '''
        对集合进行顺时针旋转
        0,0 -> 2,0 0,1->1,0 0,2->0,0
        '''
        temp_list = []
        # temp_row_01 =[]
        # temp_row_01.append(self.list01[len(self.list01-1)][0])
        # temp_row_01.append(self.list01[len(self.list01-2)][0])
        # temp_row_01.append(self.list01[len(self.list01-3)][0])
        # temp_list.append(temp_row_01)
        for row in range(len(self.list01)):
            temp_row = []
            for col in range(len(self.list01[row])-1,-1,-1):
                temp_row.append(self.list01[col][row])
            temp_list.append(temp_row)
        self.list01 = temp_list
    def left_rotate(self):
        '''
        对集合进行逆时针旋转
        '''
        temp_list = []
        # temp_row_01 =[]
        # temp_row_01.append(self.list01[len(self.list01-1)][0])
        # temp_row_01.append(self.list01[len(self.list01-2)][0])
        # temp_row_01.append(self.list01[len(self.list01-3)][0])
        # temp_list.append(temp_row_01)
        for i in range(3):
            self.right_rotate()
        
class Canvas_Demo(Tk):
    def __init__(self):
        super().__init__()
        self.title ='canvas绘图'
        self.geometry('800x600+300+100')
        #准备画板
        cv = Canvas(self,bg='lightGray',width=700,height =500)
        cv.place(x=50,y=50)
        #画一根线
        cv.create_line(70,70,70,400,fill='red',dash=(3,3))

if __name__ == '__main__':
    # this_array = Array()
    # this_array.right_rotate()
    # this_array.print()
    # this_array.left_rotate()
    # this_array.print()
    window = Canvas_Demo()
    window.mainloop()