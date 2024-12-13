import random as r
symbols = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!_'

while True:
	a = int(input("введите длину нового пароля: "))
	password = ''
	for i in range(a):
	  password += r.choice(symbols)
	print(f'ваш пароль :{password} . хотите его сохранить? ')

	if input().lower() == "y":
		name = input('напишите имя:')
		with open('passwords.txt', 'a') as file:
			file.write(f'{name}: {password}\n')
			print(file)
