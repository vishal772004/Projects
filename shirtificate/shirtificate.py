from fpdf import FPDF


class PDF(FPDF):
    def __init__(self):
        pdf =FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_font("Times",style="B",size=25)
        pdf.cell(text="CS50 Shirtificate",center=True,new_x=XPos.RIGHT, new_y=YPos.TOP)
        pdf.image("shirtificate.png" ,h=pdf.eph, w=pdf.epw)
        pdf.output("varying_format.pdf")



pdf = PDF()


