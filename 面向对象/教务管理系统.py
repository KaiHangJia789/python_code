"""
需求说明
采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
1. 添加学生成绩
    根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
    1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
    1.2 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
    1.3 验证成绩范围(0-100 分）
    1.4 创建学生对象并添加到系统
2. 修改学生成绩
    根据输入的学生姓名，修改对应的学生成绩
    2.1 输入要修改的学生姓名
    2.2 根据姓名查找该学生，显示该生当前成绩信息
    2.3 输入新的语文、数学、英语成绩
    2.4 更新学生成绩数据
3. 删除学生成绩
    根据输入的学生姓名，删除对应的学生成绩
4. 查询指定学生成绩
    根据输入的学生姓名，查找对应的学生成绩，并输出
    4.1 输出格式为: 姓名: 张三 | 语文: 85 | 数学: 90 | 英语: 88 | 总分: 263
5. 展示全部学生成绩
    展示出系统中所有学生的成绩
"""

#学生类
class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    
    def __str__(self):
        return f"姓名: {self.name} | 语文: {self.chinese} | 数学: {self.math} | 英语: {self.english} | 总分: {self.chinese+self.math+self.english}"
    
    #修改学生成绩
    def update_score(self,chinese=None,math = None,english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english



#教务管理系统
class EduMangement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []  #   记录学生信息
    

    #添加学生成绩

    def add_student(self):
        name = input("请输入学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print("该学生已经存在,添加失败")
                return
        
        chinese = int(input("请输入学生语文成绩:"))
        math    = int(input("请输入学生数学成绩:"))
        english = int(input("请输入学生英语成绩:"))
        
        #判断分数是否在0~100之间
        if 0 <= chinese <=100 and  0 <= math <=100  and  0 <= english <=100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("学生信息添加成功")
        else:
            print("各科成绩必须在0~100之间!!!")


    #修改学生成绩
    def update_student(self):
        name = input("请输入要修改成绩的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩为: {s}")
                chinese = int(input("请输入修改后的学生语文成绩:"))
                math    = int(input("请输入修改后的学生数学成绩:"))
                english = int(input("请输入修改后的学生英语成绩:"))
                 #判断分数是否在0~100之间
                if 0 <= chinese <=100 and  0 <= math <=100  and  0 <= english <=100:
                    s.update_score(chinese,math,english)
                    print("成绩修改成功.")
                    print(f"修改后的学生成绩：{s}")
                    return
                else:
                    print("各科成绩必须在0~100之间!!!")
                    return    
        print("未找到该学生.")


    #删除学生成绩
    def delete_student(self):
        name = input("请输入要删除成绩的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功.")
                return
            print("未找到该学生，查询失败!!")


    #查询指定学生成绩
    def query_student(self):
        name = input("请输入要查询的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print(f"学生信息:{s}")
                return
            else:
                print("未找到该学生.")
    #展示全部学生成绩
    def list_student(self):
        for s in self.student_list:
            print(s)

    def run(self):
        print(f"欢迎使用教务管理系统 V{EduMangement.system_version}")

        while True:
            print("###################################################################")
            print("1.添加学生信息\n2.修改学生信息\n3.删除学生信息\n4.查询单个学生信息\n5.查询全部学生信息\n6.退出")
            print("###################################################################\n")
            
            choice = input("请选择要执行的操作,输入1-6:\n")
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.query_student()
                    case "5":
                        self.list_student()
                    case "6":
                        print("拜拜!")
                        break
                    case _:
                        print("输入错误,请输入1-6之间的数字.")
            except ValueError :
                print("你输入的值有问题，请重新输入~")
            except Exception:
                print("程序运行出现问题，请重新选择~")

if __name__ == '__main__':
    edu_management = EduMangement()
    edu_management.run()

