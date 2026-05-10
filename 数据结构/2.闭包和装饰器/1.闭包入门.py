"""
数据结构.闭包.1.闭包入门 的 Docstring
闭包解释:
    内部函数 引用外部函数的变量 形成闭包
    格式：
    def 外部函数(参数):
        变量 = 参数

        def 内部函数():
            使用外部函数的变量
        return 内部函数
    条件:
        1.有嵌套
        2.有引用
        3.有返回
细节:1.函数名 和 函数名()是两个概念:前者:函数对象 后者:函数调用,获取返回值
"""

#1.:函数名->是对象
def get_sum(a,b):
    return a+b

print(get_sum)#<function get_sum at 0x0000020E0E0E0E80>,对象
print(get_sum(10,20))#30,调用函数，获取返回值

#变量名可以被赋值给变量
get_sum_1 = get_sum
print(get_sum_1)    #<function get_sum at 0x0000020E0E0E0E80>
print(get_sum_1(10,20))#30
print('*'*50)

#2.定以求和的闭包，外部函数有参数num1,内部函数有参数num2，求其之和
def fn_outer(num1):
    def fn_inner(num2):
        sum=num1+num2
        print(f"{num1}+{num2}={sum}")

    return fn_inner

#调用上述函数
fn_inner = fn_outer(10)
fn_inner(20)
print('*'*50)

fn_outer(10)(20)

