#tutorial 13
#textobject character spacing

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm


pdf=canvas.Canvas("output13.pdf")
pdf.translate(cm, cm)

content=pdf.beginText()
content.setTextOrigin(10, 800)

d="this is spacing example in reportlab"
x=0
for i in range(20):
    content.setCharSpace(x)
    content.textLine(d)
    x+=0.5
    
    
pdf.drawText(content)
pdf.save()

    
    
    
    
    
  
