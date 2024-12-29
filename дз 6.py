from datetime import date, timedelta
import calendar

while True:
	print("\nВведите номер задачи(1 или 2): ", end='')
	choice = int(input())
	if choice == 1:
		def count_workdays(year, month, holidays=[]):
			total_workdays = 0
			days_in_month = calendar.monthrange(year, month)[1]

			for day in range(1, days_in_month + 1):
				current_date = date(year, month, day)
				if current_date.weekday() < 5 and current_date not in holidays:
					total_workdays += 1

			return total_workdays


		year = int(input('введите год: '))
		month = int(input('введите месяц: '))
		holidays = [date(2024, 3, 8), date(2024, 3, 21)]

		print(f"Количество рабочих дней в {month}/{year}: {count_workdays(year, month, holidays)}")
	elif choice == 2:
		def easter_date(year):
			a = year % 19
			b = year // 100
			c = year % 100
			d = b // 4
			e = b % 4
			f = (b + 8) // 25
			g = (b - f + 1) // 3
			h = (19 * a + b - d - g + 15) % 30
			i = c // 4
			k = c % 4
			l = (32 + 2 * e + 2 * i - h - k) % 7
			m = (a + 11 * h + 22 * l) // 451
			month = (h + l - 7 * m + 114) // 31
			day = ((h + l - 7 * m + 114) % 31) + 1
			return date(year, month, day)
		year = int(input('введите год: '))
		print(f"Дата Пасхи в {year}: {easter_date(year)}")
	else:
		print("Неверный номер задачи!")
