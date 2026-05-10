from  pypdf import PdfReader, PdfWriter

reader = PdfReader('PDF办公/test_pdf/1.pdf')
writer = PdfWriter()

for page in reader.pages:
    page.mediabox.lower_left = (100, 0)
    page.mediabox.lower_right = (500, 100)
    page.mediabox.upper_right = (500, 400)
    page.mediabox.upper_left = (100, 400)
    writer.add_page(page)


with open('PDF办公/test_pdf/test_cut.pdf', 'wb') as f:
    writer.write(f)