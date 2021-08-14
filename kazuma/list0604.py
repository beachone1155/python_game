import tkinter

def click_btn():
    button["text"] = "クリックしました"
    

root = tkinter.Tk()
root.title("初めてのキャンバス")

canvas = tkinter.Canvas(root, width= 600, height= 800, bg="skyblue")
canvas.pack()

font = ("System", 24)
label = tkinter.Label(root, text="ラベルの文字列")
label.place(x = 200, y =100)

button = tkinter.Button(root, text="ボタンの中の文字", font=(24), command=click_btn)
button.place(x = 200, y = 200)

picture = tkinter.PhotoImage(file="iroha.png")
canvas.create_image(200, 300, image= picture)

root.mainloop()