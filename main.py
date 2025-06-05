from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfgen import canvas

def create_pdf(filename):
    c=canvas.Canvas(filename, pagesize=A4)
    witdh, height =A4

    c.setFont("Helvetica", 12)
    c.drawString(100, height -100, "Hello this is a PDF document created using ReportLab")

    c.line(100,height - 110, 500, height -110)

    c.save()

    if __name__=="__main__":
        create_pdf("example.pdf")