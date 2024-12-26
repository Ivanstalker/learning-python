import tkinter as tk
from tkinter import messagebox
from tkinter import font


def add_task():
	task = task_entry.get()
	if task.strip():  # Проверяем, что задача не пустая
		# Получаем выбранную важность задачи
		priority = priority_var.get()
		priority_text = priority if priority else "Без приоритета"

		# Добавляем задачу с приоритетом
		task_with_priority = f"{task} ({priority_text})"
		tasks_listbox.insert(tk.END, task_with_priority)
		task_entry.delete(0, tk.END)  # Очищаем поле ввода
	else:
		messagebox.showwarning("Предупреждение", "Введите текст задачи!")


def delete_task():
	try:
		selected_task_index = tasks_listbox.curselection()[0]  # Получаем индекс выбранной задачи
		tasks_listbox.delete(selected_task_index)  # Удаляем задачу из списка
	except IndexError:
		messagebox.showwarning("Предупреждение", "Выберите задачу для удаления!")


# Создаём главное окно
root = tk.Tk()
root.title("To-Do List")

# Увеличиваем масштаб шрифтов
font_large = font.Font(size=14)
font_medium = font.Font(size=12)

# Поле для ввода новой задачи
task_entry = tk.Entry(root, width=50, font=font_medium)
task_entry.grid(row=0, column=0, padx=15, pady=15)

# Кнопка "Добавить"
add_button = tk.Button(root, text="Добавить", command=add_task, font=font_medium)
add_button.grid(row=0, column=1, padx=15, pady=15)

# Радиокнопки для выбора важности
priority_var = tk.StringVar(value="")  # Переменная для хранения выбранной важности

high_priority_check = tk.Radiobutton(
	root, text="Высокая важность", variable=priority_var, value="Высокая", font=font_medium
)
medium_priority_check = tk.Radiobutton(
	root, text="Средняя важность", variable=priority_var, value="Средняя", font=font_medium
)
low_priority_check = tk.Radiobutton(
	root, text="Низкая важность", variable=priority_var, value="Низкая", font=font_medium
)

high_priority_check.grid(row=1, column=0, sticky="w", padx=15)
medium_priority_check.grid(row=2, column=0, sticky="w", padx=15)
low_priority_check.grid(row=3, column=0, sticky="w", padx=15)

# Список задач
tasks_listbox = tk.Listbox(root, width=60, height=15, font=font_medium)
tasks_listbox.grid(row=4, column=0, columnspan=2, padx=15, pady=15)

# Кнопка "Удалить"
delete_button = tk.Button(root, text="Удалить", command=delete_task, font=font_medium)
delete_button.grid(row=5, column=0, columnspan=2, pady=15)

# Запуск приложения
root.mainloop()