#tutorial 38
#create multiple shapes

#reportlab graphics sub package to create multiple shapes

from reportlab.graphics import shapes
from reportlab.lib import colors
drawing_obj=shapes.Drawing(400,400)
drawing_obj.add(shapes.Rect(20,20,300,300,strokeColor=colors.green,fillColor=colors.green))
drawing_obj.add(shapes.Rect(20,20,200,200,strokeColor=colors.red))
drawing_obj.add(shapes.Circle(120,100,60,fillColor=colors.blue))
drawing_obj.save(formats=["pdf"],fnRoot="tutorial38")

