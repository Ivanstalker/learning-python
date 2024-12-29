import calendar

while True:
	print("\nВведите номер задачи: ", end='')
	choice = int(input())
	if choice == 1:
		data = {
			'11.11': 'Ivan',
			'23.07': 'Zhenya',
			'23.05': 'Irina',
			'13.03': 'Ira'
		}


		def birthday(year, month, data):
			cal = calendar.TextCalendar()
			cal_str = cal.formatmonth(year, month)
			for day, name in data.items():
				if day.split('.')[1] == str(month).zfill(2):  # проверка что день рождения в нужном месяце
					highlighted_day = day.split('.')[0].zfill(2)  # добавляем ведущий 0 если нужно
					print(highlighted_day)
					cal_str = cal_str.replace(
						f" {highlighted_day if highlighted_day[0] != '0' else highlighted_day[1]} ",
						f" *{highlighted_day if highlighted_day[0] != '0' else highlighted_day[1]}* ")
					cal_str = cal_str.replace(
						f"{highlighted_day if highlighted_day[0] != '0' else highlighted_day[1]} ",
						f"*{highlighted_day if highlighted_day[0] != '0' else highlighted_day[1]}* ")
					cal_str += f"{data.get(day)} "
			print(cal_str)
		print('введите год: ', end='')
		year = int(input())
		print('введите месяц: ', end='')
		month = int(input())

		birthday(year, month, data)
	elif choice == 2:
		pass
	elif choice == 3:
		pass
	else:
		print("Неверный номер задачи!")
