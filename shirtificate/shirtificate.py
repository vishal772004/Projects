from fpdf import FPDF


class PDF(FPDF):
    def __init__(self):
        pdf =FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_font("Times",style="B")
        pdf.cell(text="CS50 Shirtificate",center=True)
        pdf.image("shirtificate.png")



pdf = PDF()

pdf.output("varying_format.pdf")
