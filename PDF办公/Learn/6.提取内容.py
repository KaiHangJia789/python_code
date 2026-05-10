# from pypdf import PdfReader, PdfWriter

# reader = PdfReader(r'PDF办公/test_pdf/第一阶段2.pdf')

# writer = PdfWriter()


# for page in reader.pages:
#     text = page.extract_text()
#     print(text)


import pdfplumber

pdf = pdfplumber.open(r'PDF办公/test_pdf/第一阶段2.pdf')
for page in pdf.pages:
    #text = page.extract_text()
    text = page.extract_tables()
    print(text)
    print( )