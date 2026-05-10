# #创建类
# class Car:
#     pass
# #创建对象
# c1 = Car()
# #为对象动态添加属性
# c1.color = "red"
# c1.brand = "BWY"
# c1.name = "X5"
# c1.price = 50000

# print(c1.__dict__)#以字典的形式输出

#----------------------------------------------------------
class Car:
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name  = c_name
        self.price = c_price
    
    #定义实例方法
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中...")
    
    def total_cost(self,discount,rate):
        """
        total_cost 的 Docstring:
            计算提车的总费用
        :param discount: 折扣
        :param rate: 税率
        return :   车的价格*折扣+车的价格*税率
        """
        total_cost = self.price*discount+rate*self.price
        return f"提车总费用为 :{total_cost}"
    #魔法方法
    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"
    
    def __eq__(self, other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
       
    def __lt__(self,other) :
        return self.price < other.price

c1 = Car(c_color="红色",c_brand="BWM",c_name="X4",c_price=320000)
# #print(c1.__dict__)
# c1.running()
# total = c1.total_cost(0.8,0.1)
# print(total)
c2 = Car(c_color="红色",c_brand="BWM",c_name="Y5",c_price=3200000)

print(c1 < c2)
