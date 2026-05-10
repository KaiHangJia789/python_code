
import re

from pypdf  import PdfReader, PdfWriter# 导入PdfReader和PdfWriter类: 用于读取和写入PDF文件

reader = PdfReader(r"PDF办公/test_pdf/1.pdf")

# print(len(reader.pages))# 获取页数: 获取PDF文件中的页数

writer = PdfWriter()# 创建PdfWriter对象: 用于处理PDF文件的写入操作

# for page in reader.pages:# 遍历页面: 对PDF文件中的每一页进行操作
#     print(type(page))
#     writer.add_page(page)# 添加页面: 将当前页添加到PdfWriter对象中

writer.write(r"PDF办公/test_pdf/test.pdf")

pdf1 = open(r"PDF办公/test_pdf/1.pdf", "rb")# 打开文件: 以二进制读取模式打开一个名为"1.pdf"的文件
pdf2 = open(r"PDF办公/test_pdf/2.pdf", "rb")# 打开文件: 以二进制读取模式打开一个名为"2.pdf"的文件
pdf3 = open(r"PDF办公/test_pdf/3.pdf", "rb")# 打开文件: 以二进制读取模式打开一个名为"3.pdf"的文件

# 合并文件: 将多个PDF文件合并为一个新的PDF文件
writer.merge(0,pdf1,pages=[0,2])# 将pdf1的第1页和第3页合并到新的PDF文件的第1页位置
writer.merge(2,pdf2,pages=[0,1])# 将pdf2的第1页和第2页合并到新的PDF文件的第3页位置
writer.merge(4,pdf3,pages=[0,2])# 将pdf3的第1页和第3页合并到新的PDF文件的第5页位置

pdf1.close()# 关闭文件: 释放资源，关闭打开的pdf1文件
pdf2.close()
pdf3.close()

writer.write(r"PDF办公/test_pdf/test.pdf")
writer.close()
reader.close()