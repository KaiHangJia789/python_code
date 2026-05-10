from pypdf import PdfWriter# 导入PdfWriter类: 用于将多个PDF文件合并为一个文件
from pypdf import PdfReader# 导入PdfReader类: 用于读取PDF文件的内容

# writer = PdfWriter()# 创建PdfWriter对象: 用于处理PDF文件的写入操作

# writer.add_blank_page(595.276, 841.89)# 添加空白页: 在PDF文件中添加一页空白页，指定页面的宽度和高度

# writer.add_blank_page()# 添加空白页: 在PDF文件中添加一页空白页，使用默认的页面尺寸

# with open("PDF办公/test_pdf/test.pdf", "wb") as f:# 打开文件: 以二进制写入模式打开一个名为"test.pdf"的文件
#     writer.write(f)# 写入PDF文件: 将之前添加的空白页写入到打开的文件中


#======================================================
reader = PdfReader("PDF办公/test_pdf/test.pdf")# 创建PdfReader对象: 用于读取指定路径的PDF文件

print(len(reader.pages))# 获取页数: 获取PDF文件中的页数

reader.close()# 关闭PDF文件: 释放资源，关闭打开的PDF文件
