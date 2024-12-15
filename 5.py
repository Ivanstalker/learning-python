import tkinter as tk

root = tk.Tk()
root.geometry('300x400')
root.title("Калькулятор")

textEntry = tk.StringVar()
entry1 = tk.Entry(root, textvariable=textEntry)
entry1.config(width=15, font=("Helvetica", 20))
entry1.pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=10)


def addB(button_text):
    current_text = textEntry.get()
    textEntry.set(current_text + button_text)


def clear_entry():
    textEntry.set("")


def calculate():
    try:
        expression = textEntry.get()
        if not expression:
            return
        expression = expression.replace('X', '*')
        result = eval(expression)
        textEntry.set(result)
    except (SyntaxError, NameError, ZeroDivisionError):
        textEntry.set("Ошибка")
    except Exception as e:
        textEntry.set(f"Неизвестная ошибка: {e}")


buttons = [
    ('7', lambda: addB('7')), ('8', lambda: addB('8')), ('9', lambda: addB('9')), ('/', lambda: addB('/')),
    ('4', lambda: addB('4')), ('5', lambda: addB('5')), ('6', lambda: addB('6')), ('*', lambda: addB('*')),
    ('1', lambda: addB('1')), ('2', lambda: addB('2')), ('3', lambda: addB('3')), ('-', lambda: addB('-')),
    ('0', lambda: addB('0')), ('C', clear_entry), ('=', calculate), ('+', lambda: addB('+')),
]

for i, (text, command) in enumerate(buttons):
    button = tk.Button(frame, text=text, command=command)
    button.config(font=("Helvetica", 20))
    button.grid(row=i // 4, column=i % 4, padx=5, pady=5)


root.mainloop()