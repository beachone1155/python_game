import tkinter
root = tkinter.Tk()
root.title("初めてのラベル")#順不同始め
font = ("System", 24)
label = tkinter.Label(root, text="ラベルの文字列")
label.place(x = 200, y =100)
button = tkinter.Button(root, text="ボタンの中の文字", font=(24))
button.place(x = 300, y = 100)
root.geometry("800x600")#順不同終わり
root.mainloop()