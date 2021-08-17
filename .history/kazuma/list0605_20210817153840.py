import tkinter
from tkinter import font

root = tkinter.Tk()
root.title("おみくじソフト")
root.resizable(False,False) #ウインドウのサイズ変更を不可にする
canvas = tkinter.Canvas(root,width=800,height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400,300, image =gazou)

label = tkinter.Label(root,text="？？", font=("Times News Roman",120),bg="white")
label.place(x=380,y=60)
button 
root.mainloop()