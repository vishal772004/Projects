from fpdf import FPDF


class PDF(FPDF):
    def __init__(self):
        pdf =FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_font("Times",style="B",size=25)
        pdf.cell(text="CS50 Shirtificate",center="True",new_x="LMARGIN", new_y="NEXT")
        pdf.image("shirtificate.png",h=145,w=105)
        pdf.output("varying_format.pdf")



pdf = PDF()


