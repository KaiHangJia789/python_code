"""
案例: 演示二分查找, 递归版.

二分查找:
    概述:
        属于查找类算法, 相对效率比较高, 时间复杂度为: O(log n)

    前提:
        列表必须是有序的.

    原理: 假设列表是 升序 的
        1. 比较 要查找的元素 和 列表的中值, 如果一样就返回True, 程序结束.
        2. 如果 要查找的元素 比 中值小, 去前半段(中值前) 查找.
        3. 如果 要查找的元素 比 中值大, 去后半段(中值后) 查找.
        4. 重复上述动作, 直至找完. 如果都找完了, 还找不到, 就返回 False
"""

def binary_search_recursion(my_list,target):
    n = len(my_list)

    if n == 0: return False

    mid = n//2

    if my_list[mid]==target: return True
    elif my_list[mid]>target:
        return binary_search_recursion(my_list[:mid],target)
    else:
        return binary_search_recursion(my_list[mid+1:],target)
    return False
if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,7,8,9,10]
    print(binary_search_recursion(my_list,11))
    
    