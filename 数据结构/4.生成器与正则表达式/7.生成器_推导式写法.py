"""
数据结构.4.生成器与正则表达式.7.生成器_推导式写法 的 Docstring

生成器(Generator)核心概念
    生成器是一种特殊的迭代器，它基于数据规则，在迭代过程中按需生成元素，
    而不是一次性将所有元素加载到内存中，从而实现高效的内存使用。
核心目的
    节省内存：
        特别适合处理大数据集或无限序列，避免一次性占用大量内存。
    惰性计算：
        只有在迭代时才计算并返回下一个值，计算是 “懒加载” 的。
主要实现方式
    1. 生成器表达式（推导式写法）
        语法与列表推导式类似，只是将方括号 [] 换成圆括号 ()。

2. yield 关键字
    在函数中使用 yield 替代 return,函数就变成了生成器函数。每次调用 next() 或迭代时，
    函数执行到 yield 处暂停，并返回当前值；下次迭代时从暂停处继续执行。

生成器与迭代器的关系
    生成器是迭代器的子类，它自动实现了 __iter__() 和 __next__() 方法，
    因此可以直接用 for 循环或 next() 函数遍历。
    与手动实现的迭代器相比，生成器的代码更简洁，且自动管理了迭代状态。

"""
import sys#系统模块
#1.生成器  推导式写法
my_generator = (i for i in range(1,11))
print(my_generator)
print(type(my_generator))
print('-'*50)

#生成1~10之间的偶数
mygt2 = (i for i in range(1,11) if i % 2 ==0)
print(mygt2)
print('-'*50  )


#如何从生成器中获取数据
print(next(mygt2))#2
print(next(mygt2))#4
print('-'*50)
for i in mygt2:
    print(i)#6 8 10
print('-'*50)


my_list = [i for i in range(1000000)]
my_gt3 = (i for i in range(1000000))
print(type(my_list  ),type(my_gt3))

#查看my_list和my_gt3占用内存大小
print(f"my_list的内存:      {sys.getsizeof(my_list)}")
print(f"my_gt3的内存占用:   {sys.getsizeof(my_gt3)}")