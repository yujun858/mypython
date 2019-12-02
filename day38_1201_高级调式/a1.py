list1 = [1,2,3,4,5,6,7,8,9]
list2 = ['a','b','c','d','e','f','g','h','i']
tuple1 = zip(list1,list2)
for i in tuple1:
    print(i,end=' ')

list3 =[11,22,33,44,55]
em = enumerate(list3,start=1)
l = [i for i in em]
print(l)

import collections
Point = collections.namedtuple('Point',['x','y'])
p = Point(1,2)
print(p)
print(p.x,p.y)
print(p[0],p[1])

Circle = collections.namedtuple('Circle',['x','y','r'])
c = Circle(100,150,50)
print(c)

# deque
# 插入与删除问题
from collections import deque
q = deque(['a','b','c'])
print(q)
q. append('d')
q.appendleft('0')
print(q)

##defaultdict

d1 ={'one':1,'two':2}
#print(d1['four']) #keyerror

from collections import defaultdict
f = lambda : '刘大拿'
d2 = defaultdict(f)
d2['one'] = 1
d2['two'] = 2
print(d2['four']) # 刘大拿

#Counter-- 统计字符串格式
from collections import Counter


