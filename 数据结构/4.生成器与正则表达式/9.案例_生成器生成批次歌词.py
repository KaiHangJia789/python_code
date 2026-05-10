"""
数据结构.4.生成器与正则表达式.9.案例_生成器生成批次歌词 的 Docstring

生成器与迭代器的核心区别
维度	
迭代器 (Iterator)	

    实现方式:	需要手动实现 __iter__() 和 __next__() 方法，手动管理迭代状态。	
    代码复杂度:	代码量通常更多，需要显式处理状态（如当前位置、结束条件）。
    性能与内存:	惰性计算，但性能和内存依赖于手动实现，可能存在优化空间。	
    使用场景:	需要高度控制迭代过程，或自定义复杂迭代逻辑时使用。	
生成器 (Generator)

    实现方式:   通过 yield 关键字或生成器表达式实现，自动管理迭代状态。
    代码复杂度: 代码更简洁,yield 自动处理暂停和恢复，可读性和可维护性更高
    性能与内存: 惰性计算,yield 自动优化内存和性能，适合大数据集或无限序列
    使用场景:   需要简洁生成序列数据，尤其是处理大数据、按需生成数据时，能显著节省内存。


    
    基于文件中，周杰伦的歌词，创建生成器，实现歌词的批量生成

"""
import math
#定义生成器，接受每批次的歌词，返回生成器
def batch_lyricf(batch_size):
    with open('data\zhoujielun','r',encoding='utf-8')as zj_f:
        lines = [line.strip() for  line in zj_f.readlines()]
        count = math.ceil(len(lines)/batch_size)
        for i in range(count):
            yield lines[i*batch_size:(i+1)*batch_size]

d1 = batch_lyricf(8)
print(next(d1))
print(next(d1))
for a in d1:
    print(a)