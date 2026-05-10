# 生成任务4专用练习PDF：无边框 + 合并单元格课表
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

pdf = canvas.Canvas(r"PDF办公\任务\data\timetable.pdf", pagesize=A4)

# 标题
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(200, 750, "Class Timetable")

# 绘制无边框、带合并单元格的文字
pdf.setFont("Helvetica", 12)

# 表头
pdf.drawString(50, 700, "Time\\Day")
pdf.drawString(150, 700, "Monday")
pdf.drawString(250, 700, "Tuesday")
pdf.drawString(350, 700, "Wednesday")

# 合并单元格：上午 8:00-10:00（跨两行）
pdf.drawString(50, 670, "8:00-10:00")
pdf.drawString(150, 670, "Math")
pdf.drawString(250, 670, "English")
pdf.drawString(350, 670, "PE")

# 合并单元格：下午 14:00-16:00
pdf.drawString(50, 640, "14:00-16:00")
pdf.drawString(150, 640, "History")
pdf.drawString(250, 640, "Art (merged)")  # 合并单元格
pdf.drawString(350, 640, "Physics")

# 合并单元格：全天（跨三列）
pdf.drawString(50, 610, "16:00-18:00")
pdf.drawString(150, 610, "Free Time")
pdf.drawString(250, 610, "(merged all day)")
pdf.drawString(350, 610, "(merged)")

pdf.save()
print("✅ 任务4练习PDF已生成：timetable.pdf")