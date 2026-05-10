import pdfplumber
import pandas as pd

dfs = []#存储每页的DataFrame
with pdfplumber.open("PDF办公\\任务\\data\\test1 (1).pdf") as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            df_page = pd.DataFrame(table[1:], columns=table[0])
            dfs.append(df_page)
#合并所有页的DataFrame
#参一:列表   ignore_index=True:表示重新索引，避免重复索引
final_pdf = pd.concat(dfs, ignore_index=True)
print(final_pdf.shape)#显示行列数
#显示所有数据
print(final_pdf)
