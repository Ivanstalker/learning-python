import math
print('первая задача:')



def fibonaci():
	t = int(input(' введите кол-во чисел фибоначи: '))
	a, b = 0, 1
	for _ in range(t):
		print(a, end=" ")
		a, b = b, a + b
	print('\n')
fibonaci()

print('вторая задача:')
number = int(input('введите число для проверки: '))
count = []
for i in range(2 , int(math.sqrt(number) + 1)):
	if number % i == 0:
		print(f'число {number} - не простое число,оно делиться на {i}')
		break
	else:
		print(f'число {number} - простое')
		break

print('третья задача: ')
import random

print('угадай число от 1 до 100(у тебя 7 попыток)')

d = 0
a = random.randint(1, 100)
while d != 7:
	print(a)
	p = int(input())
	if p > a:
		print("слишком много")
		d += 1
		print(f'кол-во попыток: {d}')
	elif p < a:
		print('слишком мало')
		d += 1
		print(f'кол-во попыток: {d}')
	elif p == a:
		print(f'вы угадали число за {d} попыток(-и) ')
		break
