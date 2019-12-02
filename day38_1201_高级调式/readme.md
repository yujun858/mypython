- 两个list zip --> tuple
- enumerate  索引与数组 组成 tuple
- collections模块
    - namedtuple 扩展tuple
    - deque
- 文件：
- 常用操作： 打开关闭，文件名称路径， 打开方式 r 只读 w 写  x 创建模式 文件已存在，报错； a append写入
- b 二进制方式写入 t 文本方式打开 + 可读写
- with context  management protocal
```
with open(r'trext01.txt','r) as f:
    pass
    #下面语句块开始对f进行操作
```
```
f.readline()
list(f) #能打开文件作为参数，把文件内的每一行内容作为参数
```
```
read() 按字符读取；指定字符长度
seek(offset,from) from 0 从文件头开始， 1 从文件当前位置 2 文件末尾
移动单位字节：(byte)
tell() 用来显示读写指针的当前位置
f.write(str)
f.wrilines(str,[str1,str2,...,str3])
```
```
pickle
pickle.dump序列化
pickle.load反序列化
age = 19
with open(r'test01.txt','wb') as f:
    pickle.dump(age,f)
```
```
with open(r'test01.txt,'rb') as f:
    age = pickle.load(f)
```
```
持久化
shelve: 用kv保存数据，存取方式跟字典类似
shv = shelve.open(r'shv.db'，flag='r',writeback=True)
shv['one'] = 1
shv['two'] = 2
shv.close()
shelev不支持多个应用并行写入；
写回问题：强制协会writeback = True

```