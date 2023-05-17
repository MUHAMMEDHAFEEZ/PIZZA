
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage ,Label ,messagebox ,Frame
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
import sqlite3
import time
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\pizzakhaled\build\assets\frame0")
def invo():
    win  = tk.Tk()
    
    
    win.geometry("950x320+350+100")
    #making a tree
    columns = ('desc', 'price', 'total')
    tree = ttk.Treeview(win, columns=columns, show="headings")
    tree.heading('desc', text='Description')
    tree.heading('price', text='Unit Price')
    tree.heading('total', text="Total")
    tree.pack()
    win.resizable(False,False)
    win.mainloop()

  
    

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1280x832+350+100")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    640.0,
    416.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    70.0,
    52.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1205.0,
    400.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    446.0,
    389.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    834.0,
    344.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    817.0,
    783.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    89.0,
    783.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    249.0,
    526.6622314453125,
    image=image_image_8
)

canvas.create_text(
    134.0,
    683.0,
    anchor="nw",
    text="230",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    160.0,
    619.0,
    anchor="nw",
    text="Cheese-Lovers",
    fill="#000000",
    font=("Inter", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=300.3022155761719,
    y=671.457763671875,
    width=92.69778442382812,
    height=42.524444580078125
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    647.0,
    532.2977905273438,
    image=image_image_9
)

canvas.create_text(
    532.0,
    683.0,
    anchor="nw",
    text="300",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    587.0,
    629.0,
    anchor="nw",
    text="Praw",
    fill="#000000",
    font=("Inter", 20 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=697.7422485351562,
    y=671.457763671875,
    width=92.25775146484375,
    height=42.524444580078125
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    647.0,
    107.1422119140625,
    image=image_image_10
)

canvas.create_text(
    532.0,
    262.0,
    anchor="nw",
    text="190",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    559.0,
    204.0,
    anchor="nw",
    text="Chicken-Supreme",
    fill="#000000",
    font=("Inter", 20 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=697.7422485351562,
    y=250.30221557617188,
    width=92.25775146484375,
    height=42.524444580078125
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    1045.0,
    107.1422119140625,
    image=image_image_11
)

canvas.create_text(
    929.0,
    262.0,
    anchor="nw",
    text="157",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    935.0,
    208.0,
    anchor="nw",
    text="Classic-Pepperoni",
    fill="#000000",
    font=("Inter", 20 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=1095.1822509765625,
    y=250.30221557617188,
    width=92.8177490234375,
    height=42.524444580078125
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    1042.0,
    528.2977905273438,
    image=image_image_12
)

canvas.create_text(
    929.0,
    673.0,
    anchor="nw",
    text="250",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    937.0,
    623.0,
    anchor="nw",
    text="MEAT-LOVERS",
    fill="#000000",
    font=("Inter", 20 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=1091.9111328125,
    y=661.6444702148438,
    width=96.0888671875,
    height=42.524444580078125
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: invo(),
    relief="flat"
)
button_6.place(
    x=1213.0,
    y=780.0,
    width=33.0,
    height=31.2288818359375
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("sdf"),
    relief="flat"
)
button_7.place(
    x=300.3022155761719,
    y=250.30221557617188,
    width=92.69778442382812,
    height=42.524444580078125
)

canvas.create_text(
    134.0,
    262.0,
    anchor="nw",
    text="210",
    fill="#000000",
    font=("Inter", 20 * -1)
)

canvas.create_text(
    129.0,
    202.0,
    anchor="nw",
    text="Classic BBQ Chicken Ranch",
    fill="#000000",
    font=("Inter", 20 * -1)
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    263.0,
    110.0533447265625,
    image=image_image_13
)
w = Frame( window)
# Create a photoimage object of the image in the path
w.place(x=0,y=0,width=1280,height=832)
image1 = Image.open('D:/pizzakhaled/build/assets/frame0\MacBook.png')
test = ImageTk.PhotoImage(image1)
LOGO = Label(w,image=test).pack()
#LOGO.image = test

window.after(2000,lambda:w.destroy())

window.resizable(False, False)
window.mainloop()
