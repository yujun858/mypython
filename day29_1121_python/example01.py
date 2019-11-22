
# with open(r'./test01.txt','r') as f:
#     # 按行读取内容
#     strline = f.readline()
#     while strline:
#         print(strline)
#         strline = f.readline()

# with open(r'./test01.txt','r') as f:
#     l = list(f)
#     for line in l:
#         print(line)

# # read 按字符读取文件内容
# import time
# with open(r'./test01.txt','r') as f:
#     strChar = f.read(3)
#     while strChar:
#         time.sleep(1)
#         print(strChar)
#         strChar = f.read(3) # 按字符读取
# tell():文件读写指针当前位置
# write(str)：文件写入字符串
# writeline(str)
# os 模块
# pickle
# import pickle
# # pickle.dump
# # pickle.load
# age = 19
# with open(r'test01.txt','wb') as f:
#     pickle.dump(age,f)
# #  反序列化
# with open(r'test01.txt','rb') as f:
#     age = pickle.load(f)
    # print(age)
import pickle
a = [19,'liu','i love wang','beijing大学',[185,76]]
with open(r'test01.txt','wb') as f:
    pickle.dump(a,f)
with open(r'test01.txt','rb') as f:
    a = pickle.load(f)
    print(a)
