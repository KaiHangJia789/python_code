"""
2.继承入门 的 Docstring

class A(B):
    pass
    
    继承关系：
    A 是 B 的子类
    B 是 A 的父类
    
    好处:
        提高代码复用性
    弊端:
        耦合性增强了，父类不好的内容，子类想没有都不行

    扩展: 开发原则
    1. 高内聚，低耦合
    内聚:指类自己独立解决问题的能力
    耦合:指类之间相互依赖的能力
    即  : 自己能解决的事,不要麻烦别人
"""
#1 定义父类
class father():
    def __init__(self):
        self.gender = '男'
    
    def walk(self):
        print("走")

#定义子类
class son(father):
    pass


s = son()
print(f"性别:{s.gender}")
s.walk()
