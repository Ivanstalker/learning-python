import datetime as dt
from myFunc.printTask import print_task as p
import random as rd

p(1)


def day_left(date):
	return (date - dt.datetime.now()).days


print('введите дату: ', end='')

data = dt.datetime.strptime(input(), '%Y-%m-%d')
print(day_left(data))

p(2)
print('я загадал число от 1 до 100, сможешь отгадать??')

robot = rd.randint(1, 100)
user = int(input('введите ваши предположения: '))

while robot != user:
	if robot > user:
		print(f'ваше предположение: {user}')
		print('слишком мало!')
		user = int(input('введите ваши предположения: '))
	elif robot < user:
		print(f'ваше предположение: {user}')
		print('слишком много!')
		user = int(input('введите ваши предположения: '))
	else:
		print('error 404 :(')

if user == robot:
	print('вы угадали число!')

p(3)

def time_to_seconds(hours, minutes, seconds):
	return "общее количество секунд: " + str(hours * 60 * 60 + minutes * 60 + seconds)

print('введите часы: ', end='')
hours = int(input())
print('введите минуты: ', end='')
minutes = int(input())
print('введите секунды: ', end='')
seconds = int(input())

print(time_to_seconds(hours, minutes, seconds))

p(4)

print('введите цело число: ', end='')

num = str(input())

a = 0
for i in num:
	a += int(i)
print(f'общая сумма цифр числа {num}: {a}')