from fpdf import FPDF # for PDF Making
import pandas as pd # For CSV Files

pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv') # This will read the topics.csv

for index, row in df.iterrows(): # iterrows iter everything and make it easy for you
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=0,txt=row['Topic'], align='L', ln=1)

    pdf.line(10,21, 200,21)
    for i in range(row['Pages'] -1):
        pdf.add_page()
#This is where you will get your output
pdf.output('output.pdf')