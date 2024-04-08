from fpdf import FPDF


class PDF(FPDF):
    def __init__(self,name):
        self.pdf =FPDF(orientation="P", format="A4")
        self.pdf.add_page(format=(210,297))
        self.pdf.set_font("Times",style="B",size=30)
        self.pdf.cell(text="CS50 Shirtificate",center="True")
        self.pdf.ln(20)
        self.pdf.cell(8,50)
        self.pdf.image("shirtificate.png",h=240, w=175)
        self.pdf.set_font("Times",style="B",size=20)
        self.pdf.output("varying_format.pdf")



pdf = PDF()


