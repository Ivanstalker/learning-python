import os

path = input('введите путь к файлу: ')
word1 = input('введите слово для поиска: ')
word2 = input('введите слово для замены: ')

try:
	with open(path, 'r', encoding='utf-8') as f:
		file_content = f.read()
		file_content_new = file_content.replace(word1, word2)
		print(file_content)

	new_filename = path[:-4] + '_modified.txt'

	with open(new_filename, 'w', encoding='utf-8') as f:
		f.write(file_content_new)
		print(f'ваш файл сохранен в {new_filename}')
except FileNotFoundError:
	print('файл не найден!!')
except Exception as e:
	print(f'возникла ошибка({e}) !!')