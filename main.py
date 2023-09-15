from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto = False, margin=0)

#Creating pages with main and supplement

for index, row in df.iterrows():

    pdf.add_page()
    pdf.set_font(family='Times',size=20, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align ='L', ln=1)
    pdf.line(10, 20 , 200, 20)

#Main page lines

    for i in range(30, 270, 10):
        pdf.line(10, i, 200, i)

# Main page footer

    pdf.ln(260)
    pdf.set_font(family='Times', size=10, style="I")
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    for i in range(row['Pages']-1):
        pdf.add_page()

#Supplement page lines

        for i in range(30, 270, 10):
            pdf.line(10, i, 200, i)

# Supplement footer

        pdf.ln(273)
        pdf.set_font(family='Times', size=10, style="I")
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

pdf.output('output.pdf')