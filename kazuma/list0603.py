import tkinter

def click_btn():
    button["text"] = "クリックしました"
    
root = tkinter.Tk()
root.title("初めてのラベル")
font = ("System", 24)
label = tkinter.Label(root, text="ラベルの文字列")
label.place(x = 200, y =100)
button = tkinter.Button(root, text="ボタンの中の文字", font=(24), command=click_btn)
button.place(x = 300, y = 100)
root.geometry("800x600")
root.mainloop()