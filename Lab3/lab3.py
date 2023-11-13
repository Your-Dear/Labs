import tkinter as tk
from PIL import ImageTk,Image
from lib import gen_key
import pygame


def enter_listener():
    hex_num = entry.get()
    entry.delete(0, tk.END)
    tk.Label(window, text="Your activation code is:").place(x=170, y=140)
    result = tk.Label(window, text=gen_key(hex_num))
    result.place(x=169, y=160)
    
    
    def remove_text ():
        result.config(text = " ") 
    
    tk.Button(window, text = "Try another code", command = remove_text).place(x=310, y=145)
    result = tk.Label(window, text=" ")
     
window = tk.Tk()
window.title("Resident Evil 2 Remake KEYGEN")
window.geometry("504x204")
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\GGR\Desktop\1° Сем\Прог Лаб\Python Course\Labs\Lab3/re1_8bitmusic.mp3")
pygame.mixer.music.play()

image1 = Image.open(r"C:\Users\GGR\Desktop\1° Сем\Прог Лаб\Python Course\Labs\Lab3/re2.gif")
image1 = image1.resize((500, 200))
test = ImageTk.PhotoImage(image1)
label1 = tk.Label(image=test)
label1.image = test
label1.place (x=0, y=0) 

tk.Label(window, text="Welcome to the RE 2: Remake License code generator.").place(x=90, y=20)
tk.Label(window, text="Please insert a 5 digit HEX number to generate your activation code.").place(x=60, y=40)
tk.Label(window, text="5 digit HEX number:").place(x=180, y=80)

entry = tk.Entry(window, textvariable=tk.StringVar())
entry.insert(10, "10000")
entry.place(x=175, y=110)
tk.Button(window, text="Enter and Get Key!", command=enter_listener).place(x=310, y=105)


window.mainloop()
