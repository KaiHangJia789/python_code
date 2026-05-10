import pdfplumber

with pdfplumber.open("PDF办公\\任务\\data\\test1_1.pdf") as pdf:
    first_page = pdf.pages[0]
    table = first_page.extract_tables()#提取表格
    table_1 = first_page.extract_text()#提取文本
    print(table)
    print('-----------------')
    print(table_1)