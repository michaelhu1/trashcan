from guizero import *

app = App(title = "Recycling Bin", height = 480, width = 800, layout = "grid")
start_message = Text(app, text = "One piece of trash at a time", size = 40, grid = [400,240])
app.display()
