from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 30)
        # Moving cursor to the right:
        self.cell(65)
        # Printing title:
        self.cell(text="CS50 Shirtificate",align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

pdf = PDF()
pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()
pdf.("shirtificate.png", h=pdf.eph, w=pdf.epw)
pdf.output("varying_format.pdf")
