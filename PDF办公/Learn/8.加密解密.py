from pypdf import PdfReader, PdfWriter

# reader = PdfReader('PDF办公/test_pdf/1.pdf')
# writer = PdfWriter()

# for page in reader.pages:
    
#     writer.add_page(page)

#加密
# writer.encrypt('123')

# writer.write('PDF办公/test_pdf/test.pdf')


reader = PdfReader('PDF办公/test_pdf/test.pdf')

#解密
if reader.is_encrypted:
    reader.decrypt('123')


for page in reader.pages:
    print(page.extract_text())
