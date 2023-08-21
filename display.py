from guizero import *

app = App(title = "Recycling Bin", height = 480, width = 800)
start_message = Text(app, text = "Please put one piece of trash at a time", size = 40)
app.display()
