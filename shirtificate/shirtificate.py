from fpdf import FPDF

pdf = FPDF()
pdf = FPDF(orientation="portrait", format="A4")
pdf.set_font("Helvetica")
pdf.set_page_background('shirtificate.png')
pdf.add_page(format=(210 , 297))
pdf.set_font("Times", size=36)
pdf.set_fill_color(0, 0, 0)
pdf.cell(text="VISHAL SAGAR MURTHY")
pdf.output("varying_format.pdf")
