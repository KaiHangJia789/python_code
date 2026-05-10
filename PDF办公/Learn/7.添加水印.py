from  pypdf import PdfReader, PdfWriter

reader = PdfReader('PDF办公/test_pdf/1.pdf')
writer = PdfWriter()

reader2 = PdfReader('PDF办公/test_pdf/2.pdf')
wm_page = reader2.pages[0]

for page in reader.pages:
    page.merge_page(wm_page)#合并水印
    writer.add_page(page)

writer.write('PDF办公/test_pdf/test_watermark.pdf')