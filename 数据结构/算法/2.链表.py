"""         
自定义代码模拟链表，思路分析：
自定义 SingleNode 类，
    表示节点类。
    属性：
        item 数值域 (元素域)
        next 地址域 (链接域)

自定义 SingleLinkedList 类，
    表示：链表
    属性：
        head 表示头结点，指向第 1 个节点。
    行为：
        isEmpty ()                  判断链表是否为空
        length ()                   获取链表长度的
        travel ()                   遍历链表
        is_empty (self)             链表是否为空
        length (self)               链表长度
        travel (self)               遍历整个链表
        add (self, item)            链表头部添加元素
        append (self, item)         链表尾部添加元素
        insert (self, pos, item)    指定位置添加元素
        remove (self, item)         删除节点
        search (self, item)         查找节点是否存在

"""

# 自定义 SingleNode 类  
class SingleNode():
    def __init__(self,item):
        self.item = item
        self.next = None
    
    def __str__(self):
        return str(self.item)

# 自定义 SingleLinkedList 类
class SingleLinkedList():
    def __init__(self,node = None):
        self.head = node

      
    def __str__(self):
        return str(self.head)
    
    #     isEmpty ()                  判断链表是否为空
    def is_empty(self):

        # #写法一:
        # if self.head is None:
        #     return True
        # else:
        #     return False

        # #写法二:  三元表达式
        # return True if self.head is None else False

        # #写法三:  布尔值
        return self.head is None    #本质是返回一个布尔值
    

    #     length ()                   获取链表长度的
    def length(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    #     travel ()                   遍历链表
    def travel(self):
        cur = self.head
        while cur is not None:
            print(cur)
            cur = cur.next
    
    #     add (self, item)            链表头部添加元素
    def add(self ,item):
        new_node = SingleNode(item)
        new_node.next = self.head
        self.head = new_node

    #     append (self, item)         链表尾部添加元素
    def append(self,item):
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
    #     insert (self, pos, item)    指定位置添加元素
    def insert(self, pos, item):
        #如果pos<=0，则添加到链表头部
        if pos <=0:
            self.add(item)
        #如果pos>=0，则添加到指定位置
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.head
            count = 0   #记录节点的位置
            while count < pos-1:
                count += 1
                cur = cur.next
            
            new_node = SingleNode(item)
            new_node.next = cur.next
            cur.next = new_node
    #     remove (self, item)         删除节点
    def remove(self,item):
        cur = self.head
        per = None
        while cur is not None:
            if cur.item == item:
                if cur == self.head:
                    self.head = cur.next
                else:
                    per.next = cur.next
                return
            else:
                per = cur
                cur = cur.next

    #     search (self, item)         查找节点是否存在
    def search(self,item):
        cur = self.head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False
        

if __name__ == '__main__':
    node = SingleNode("苏铭")
    linked_list = SingleLinkedList(node)
    # print(linked_list)
    # print(f"链表头节点的数值域为:{linked_list.head.item}")
    # print(f"链表头节点的地址域为:{linked_list.head.next}")
    print('-'*50)

    # 添加(往头部)数据
    linked_list.add("王大锤")
    linked_list.add("王小锤")
    print('-'*50)

    # 添加(往尾部)数据
    linked_list.append("木婉清")
    linked_list.append("李桐崖")
    print('-'*50)

    # 添加(指定位置)数据
    linked_list.insert(6,"张三丰")
    print('-'*50)

    # 删除数据
    linked_list.remove("王小锤")
    linked_list.remove("木婉清")
    print('-'*50)

    # 查找数据
    print(f"链表中是否存在(张三丰): {linked_list.search('张三丰')}")
    print(f"链表中是否存在(木婉清): {linked_list.search('木婉清')}")
    print('-'*50)

    # 判断链表是否为空
    print(f"链表是否为空: {linked_list.is_empty()}")
    print('-'*50)

    # 获取链表长度
    print(f"链表长度为: {linked_list.length()}")
    print('-'*50)

    # 遍历链表
    linked_list.travel()
    print('-'*50)
