# git day01
## zip :
- 把两个可迭代内容生成一个可迭代tuple元素类型组成的内容
　[1,2,3,4,5]
  [5,4,3,2,1] -->[(1,5),(2,4),(3,3),(4,2),(5,1)]
- enumerate 
    - 跟zip功能比较像
    - 对可迭代对象里每一个元素，配上一个索引，然后索引内容构成tuple类型;
## collections模块
- namedtuple
    - tuple : 可以命名tuple
- dequeue
    - 比较方便解决频繁删除插入带来的效率问题

- defaultdict
    - 当直接读取dict不存在属性时候，直接返回默认值
- Counter
    - 统计字符串的个数
    