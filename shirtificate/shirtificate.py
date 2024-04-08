from fpdf import FPDF


class PDF(FPDF):
    def __init__(self):
        pdf =FPDF(orientation="P", format="A4")
        pdf.add_page(format=(210,297))
        pdf.set_font("Times",style="B",size=25)
        pdf.cell(text="CS50 Shirtificate",center="True",new_x="", new_y="NEXT")

        pdf.image("shirtificate.png",h=160,w=160)
        pdf.output("varying_format.pdf")



pdf = PDF()


