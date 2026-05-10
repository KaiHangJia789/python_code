from pypdf import PdfReader, PdfWriter
from pypdf.generic import  RectangleObject

reader = PdfReader('PDF办公/test_pdf/1.pdf')
writer = PdfWriter()

page = reader.get_page(0)


print(page.mediabox)# 获取页面的尺寸
print(page.mediabox.left)
print(page.mediabox.right)

# 修改页面的尺寸
for page in reader.pages:
    page.mediabox = RectangleObject([0, 0,595.276, 841.89])# 设置页面的尺寸
    writer.add_page(page)

with open(r"PDF办公/test_pdf/test.pdf", "wb") as f:
    writer.write(f)

#========================================================
print('-'   * 50)
reader = PdfReader('PDF办公/test_pdf/test.pdf')
writer = PdfWriter()

page = reader.get_page(0)


print(page.mediabox)# 获取页面的尺寸
print(page.mediabox.left)
print(page.mediabox.right)
