import tkinter as tk
from PIL import ImageTk, Image
from lib import gen_key
import pygame

WIDTH = 504
HEIGHT = 204
MEDIA_PATH = "./media"


def refresh(window):
    window.nametowidget(".activatedKeyLabel").destroy()
    window.nametowidget(".keyLabel").destroy()
    window.nametowidget(".refreshButton").destroy()
    create_elements(window)


def removeGetWidgets(window):
    window.nametowidget(".petitionLabel").destroy()
    window.nametowidget(".numberLabel").destroy()
    window.nametowidget(".numberEntry").destroy()
    window.nametowidget(".getKeyButton").destroy()


def enter_listener(window, entry):
    hex_num = entry.get()
    entry.delete(0, tk.END)
    removeGetWidgets(window)

    tk.Label(
        window,
        text="Your activation code is:",
        name="activatedKeyLabel"
    ).place(x=170, y=140)
    
    tk.Label(
        window,
        text=gen_key(hex_num),
        name="keyLabel"
    ).place(x=169, y=160)
    
    tk.Button(
        window,
        text="Try another number!",
        name="refreshButton",
        command=lambda: refresh(window)
    ).place(x=310, y=145)


def create_elements(window):

    tk.Label(
        window,
        text="Please insert a 5 digit HEX number to generate your activation code.",
        name="petitionLabel"
    ).place(x=60, y=40)

    tk.Label(
        window,
        text="5 digit HEX number:",
        name="numberLabel"
    ).place(x=180, y=80)

    entry = tk.Entry(
        window,
        textvariable=tk.StringVar(),
        name="numberEntry"
    )
    entry.insert(10, "10000")
    entry.place(x=175, y=110)
    
    tk.Button(
        window,
        text="Enter and Get Key!",
        name="getKeyButton",
        command=lambda: enter_listener(window, entry)
    ).place(x=310, y=105)


window = tk.Tk()
window.title("Resident Evil 2 Remake KEYGEN")
window.geometry(f"{WIDTH}x{HEIGHT}")

pygame.mixer.init()
pygame.mixer.music.load(f"{MEDIA_PATH}/re1_8bitmusic.mp3")
pygame.mixer.music.play()

background = Image.open(f"{MEDIA_PATH}/re2.gif").resize((500, 200))
tk_image = ImageTk.PhotoImage(background)
tk.Label(image=tk_image).place(x=0, y=0) 

tk.Label(
    window,
    text="Welcome to the RE 2: Remake License code generator."
).place(x=90, y=20)

create_elements(window)
window.mainloop()

