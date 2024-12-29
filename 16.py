import calendar
from myFunc.printTask import print_task as p

p(1)

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print(calendar.month(year, month))

p(2)

print('введите год для проверки: ', end='')
a = int(input())

if calendar.isleap(a) == True:
	print('это високостный год!')
elif calendar.isleap(a) == False:
	print('это не високостный год!')

p(3)

print('введите год: ', end='')
b = int(input())
print('введите месяц: ', end='')
c = int(input())
print('введите число: ', end='')
d = int(input())

match calendar.weekday(b, c, d):
	case 0:
		print('Понедельник')
	case 1:
		print("вторник")
	case 2:
		print('Среда')
	case 3:
		print('Четверг')
	case 4:
		print('Пятница')
	case 5:
		print('Суббота')
	case 6:
		print('Воскресенье')