from fpdf import FPDF


class PDF(FPDF):
    def __init__(self):
        self.pdf =FPDF(orientation="P", format="A4")
        self.pdf.add_page(format=(210,297))
        self.pdf.set_font("Times",style="B",size=25)
        self.pdf.cell(text="CS50 Shirtificate",center="True")
        self.pdf.ln(20)
        self.set_x(-40)
        self.pdf.image("shirtificate.png",h=160,w=160,)
        self.pdf.output("varying_format.pdf")



pdf = PDF()


