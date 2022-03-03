from fpdf import FPDF
pdf = FPDF('L', 'mm', 'A4')
pdf.add_page()
pdf.set_font("Arial",size=18)
pdf.cell(200, 10, txt = "Certificamos que  ministrou o curso projeto social graphic, ", ln = 1, align = 'C',fill='false')
pdf.cell(200, 10, txt = "como parte dos projetos de extensão do Instituto Federal de Educação, ", ln = 2, align = 'C',fill='false')
pdf.cell(200, 10, txt = "Ciência e Tecnologia do Ceará - campus Maracanaú, com carga horária de", ln = 3, align = 'C',fill='false')
pdf.cell(200, 10, txt = " 20 horas, no(s) dia(s) 09/01/2021 até 09/04/2021.", ln = 4, align = 'C',fill='false')
pdf.cell(200, 10, txt = "", ln = 5, align = 'C',fill='false')
pdf.cell(200, 10, txt = "", ln = 6, align = 'C',fill='false')
pdf.cell(200, 10, txt = "Maracanaú, 29 de julho de 2021.", ln = 6, align = 'R',fill='false')

pdf.output('/home/c1c3ru/PycharmProjects/pdf/Ace_Jones.pdf','F')

