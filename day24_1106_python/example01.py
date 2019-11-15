# print('hello world')
import collections
l1 = [1, 2, 3, 4, 5]
l2 = [11, 22, 33, 44, 55]
z = zip(l1, l2)
print(type(z))
l3 = [i for i in z]
print(l3)
e = enumerate(l1, start=1)
l4 = [i for i in e]
print(l4)  # [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
Point = collections.namedtuple('point', ['x', 'y'])
p = Point(11, 22)
print(p.x)
print(p[0])
Circle = collections.namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(100, 150, 50)
q = collections.deque(['a', 'b', 'c'])
q.append('d')
q.appendleft('0')
print(q)
d = {'one': 1, 'two': 2}
# print('three')-->抛出异常
print(d['one'])
def func(): return '刘大拿'
d2 = collections.defaultdict(func)
print(d2['two'])
print(d2['one'])
c = collections.Counter('dfdgdgdfafrdsfdsfdjsfjdskjlfhdaoufjhvsaldalsfd')
print(c)