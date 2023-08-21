from guizero import *
from tkinter import pack

def update_writing():
    writing.set("World")
    app.after(200, update_writing)

app = App(height=480, width=800, bg="black")

writing = Text(app, text="One piece of trash at a time", color="white", size=40)
writing.pack(fill="none", expand=True)
app.after(200, update_writing)

app.display()
