import tkinter
from tkinter import font
import random

def 

root = tkinter.Tk()
root.title("おみくじソフト")
root.resizable(False,False) #ウインドウのサイズ変更を不可にする
canvas = tkinter.Canvas(root,width=800,height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400,300, image =gazou)

label = tkinter.Label(root,text="？？", font=("Times News Roman",120),bg="white")
label.place(x=380,y=60)
button = tkinter.Button(root,text="おみくじを引く",font=("Times New Roman", 36), fg = "skyblue")
button.place(x=360,y= 400)
root.mainloop()