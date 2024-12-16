import tkinter as t


def change_label():
	label.config(text="кнопка нажата")

root = t.Tk()
root.title('задание 1')
root.geometry("150x100+800+400")

button = t.Button(text= 'нажми меня', command= change_label)
button.pack()

label = t.Label(text= '')
label.pack()

root.mainloop()


root1 = t.Tk()
root1.title('задание 1')
root1.geometry("+800+400")

buttons = [
    ('0,0'), ('0,1'), ('0,2'), ('1,0'), ('1,1'), ('1,2'),('2,0'),('2,1'), ('2,2')
]

for i, (text) in enumerate(buttons):
    button = t.Button(text=text)
    button.config(font=("Helvetica", 20))
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)

root1.mainloop()


root2 = t.Tk()
root2.title('задание 3')
root2.geometry('400x250+800+400')

button2 = t.Button(text='кнопка 1')
button2.pack()
button2.place(x=50, y=50)


button3 = t.Button(text= 'кнопка 2')
button3.pack()
button3.place(x=150, y=100)

button4 = t.Button(text= 'кнопка 3')
button4.pack()
button4.place(x=250, y=150)

root2.mainloop()