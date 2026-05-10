import pandas as pd
import pdfplumber

with pdfplumber.open("PDF办公\\任务\\data\\test1_1.pdf") as pdf:
    table = pdf.pages[0].extract_table()#提取表格
    df = pd.DataFrame(table[1:], columns=table[0])#转为DataFrame
    print(df.head())