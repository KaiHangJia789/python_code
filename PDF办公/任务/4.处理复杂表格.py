import pdfplumber
import pandas as pd

# 任务4核心：自定义复杂表格策略
table_settings = {
    "vertical_strategy": "text",      # 无边框必须用 text
    "horizontal_strategy": "text",
    "snap_tolerance": 10,# 设置容差:合并单元格时允许的距离
    "join_tolerance": 10,# 设置容差:合并单元格时允许的距离
}

# 打开练习课表PDF
with pdfplumber.open(r"PDF办公\任务\data\timetable.pdf") as pdf:
    page = pdf.pages[0]

    # 任务4提示：查看识别的表格线
    print("\n正在打开表格调试视图...")
    page.debug_tablefinder()  # 会弹出图片！

    # 提取表格
    table = page.extract_table(table_settings)

# 转成DataFrame
df = pd.DataFrame(table)
print("\n✅ 提取结果：")
print(df)