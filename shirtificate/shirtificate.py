from fpdf import FPDF

pdf = FPDF()
pdf = FPDF(orientation="portrait", format="A4")
pdf.set_page_background('shirtificate.png')
pdf.add_page(format=(210 , 297))
pdf.set_font("Times", size=20)
pdf.set_text_color(255,255,255)
pdf.cell(text="Vishal Sagar Murthy")
pdf.output("varying_format.pdf")
