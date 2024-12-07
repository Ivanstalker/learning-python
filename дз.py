#задача №1
print('задача номер 1')
import math
figure = input('квадрат или круг: ')
if figure == "квадрат":
	r = float(input('введите сторону квадрата: '))
	print(r * r)
elif figure == 'круг':
	r = float(input('введите радиус круга: '))
	print(math.pi * r ** 2)
else:
	print('введите правильный ответ')

# задача №2
print('задача номер 2')
a = input('введите текст: ')
print(len(a))
print(a[:: -1])
print(a[ : 3])
print(a.upper())

#задача №3
print('задача номер 3')
print('валюта для конвертации: RUB')
n = float(input('введите сумму для конвертации: '))
convertation = input('выберите конвертимую валюту(USD , EUR): ')
v = {'USD' : '100', 'EUR' : '0.9'}
if convertation == 'USD':
	k = v.get('USD')
	print(f'при конвертации ваш счет будет состовлять: {float(k) * n} USD')
elif convertation == 'EUR':
	k = v.get('EUR')
	print(f'при конвертации ваш счет будет состовлять: {float(k) * n} EUR')