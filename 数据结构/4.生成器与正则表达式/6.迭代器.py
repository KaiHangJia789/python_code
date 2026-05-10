"""
数据结构.4.生成器与正则表达式.6.迭代器 的 Docstring

迭代器(Iterator)核心概念
    迭代器是 Python 中用于逐个访问数据集合元素的对象，它提供了一种统一的遍历方式，
    而无需关心数据结构的底层实现。
核心定义
    协议实现：
        迭代器必须实现 __iter__() 和 __next__() 两个特殊方法。
    __iter__()：返回迭代器对象本身，使迭代器可迭代。
    __next__()：返回集合中的下一个元素，当没有更多元素时，抛出 StopIteration 异常。
    示例:range() 就是一个典型的迭代器，它按需生成数字，而不是一次性创建所有元素。
主要特点
    手动管理：
        需要显式实现 __iter__() 和 __next__() 方法，不像可迭代对象那样可以直接使用 for 循环。
    状态管理：
        迭代器内部维护着迭代的状态（如当前位置），每次调用 next() 都会推进这个状态，
        且迭代器是一次性的，遍历完成后就无法再次使用。
    惰性计算：
        内存使用效率高，元素是在迭代过程中按需生成的，而不是一次性加载到内存中，
        这在处理大数据集时尤为重要。
"""

class MyIterator:
    def __init__(self,start,end):
        self.current_value = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_value >= self.end:
            raise StopIteration
        # current = self.current_value
        # self.current_value += 1
        # return current

        #简便写法
        self.current_value += 1
        return self.current_value - 1

    
for i in MyIterator(1,5):
    print(i)
print('-'*20)

my_itr = MyIterator(1,5)
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))
print(next(my_itr))


