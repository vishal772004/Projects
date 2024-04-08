from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

pdf = PDF()
pdf.add_page()
pdf.image("shirtificate.png")
pdf.set_font("Times", size=12)
pdf.output("varying_format.pdf")
