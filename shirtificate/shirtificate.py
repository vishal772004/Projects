from fpdf import FPDF


class PDF(FPDF):
    def __init__(self):
        pdf =FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.cell(text="CS50 Shirtificate",)
        pdf.image("shirtificate.png")
        pdf.set_font("Times", size=12)


pdf = PDF()

pdf.output("varying_format.pdf")
