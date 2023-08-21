from guizero import *

app = App(title = "Recycling Bin", height = 480, width = 800)

def update_writing():
    writing.set("World")
    app.after(200, update_writing)

app = App(height=480, width=800, bgcolor="black")

writing = Text(app, text="One piece of trash at a time", color="red", size=110)

writing.pack(fill="none", expand=True)

app.after(200, update_writing)

app.display()
