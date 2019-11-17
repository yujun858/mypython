# print('hello world')
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]
z = zip(l1,l2)
print(type(z))
l3 = [i for i in z]
print(l3)
e = enumerate(l1,start=1)
l4 = [i for i in e]
print(l4) #[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
import collections
Point = collections.namedtuple('point',['x','y'])
p = Point(11,22)
print(p.x)
print(p[0])

