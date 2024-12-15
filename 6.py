import os

path = input('введите путь к файлу для проверки: ')

wordCount = dict()

with open(path, 'r', encoding='utf-8') as f:
	file_content = f.read().splitlines()
	for line in file_content:
		line = line.split(' ')
		for word in line:
			wordCount[word] = wordCount.get(word, 0) + 1

for i in sorted(wordCount, key=wordCount.get, reverse=True):
	print(f'{i}: {wordCount[i]}')