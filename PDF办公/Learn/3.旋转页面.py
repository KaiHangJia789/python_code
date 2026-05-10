from pypdf import PdfReader, PdfWriter

reader = PdfReader(r"PDF办公/test_pdf/1.pdf")# 创建PdfReader对象: 用于读取指定路径的PDF文件
writer = PdfWriter()# 创建PdfWriter对象: 用于处理PDF文件的写入操作

page = reader.get_page(0)# 获取页面: 获取PDF文件中的第1页

for i in range(reader.get_num_pages()):
    if i % 2 == 0:
        page = reader.get_page(i).rotate(90)# 旋转页面: 将当前页旋转90度
    else:
        page = reader.get_page(i).rotate(-90)# 旋转页面: 将当前页旋转-90度

    writer.add_page(page)# 添加页面: 将旋转后的页添加到PdfWriter对象中

with open(r"PDF办公/test_pdf/test.pdf", "wb") as f:

    writer.write(f)