from myFunc.printTask import print_task as p

p(2)

number = input('введите число для проверки: ')

def palindrome():
	global number
	if number.lower() == number.lower()[::-1]:
		print(f'число {number} - палиндром')
	else:
		print(f'число {number} -  не палиндром')

palindrome()

p(3)
import random as r

print('введите предмет(камень : 1, ножницы: 2, бумага: 3) ')

p = int(input())

h = r.randint(1, 3)

if p == h:
	print('ничья')
elif p == 1 and h == 2 :
	print('победа')
elif p == 1 and h == 3:
	print('поражение')
elif p == 2 and h == 1:
	print('поражение')
elif p == 2 and h == 3:
	print('победа')
elif p == 3 and h == 1:
	print('победа')
elif p == 3 and h == 2:
	print('поражение')
else:
	print('error 404')

print(h)