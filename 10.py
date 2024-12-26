import os


def read_file(filename):
	data = list()
	with open(file= filename, mode= 'r', encoding= 'utf-8') as f:
		contents = f.read()
		i = 0
	for line in contents.splitlines():
		d = dict()
		line = line.split(',')
		d['name'] = line[0]
		d['age'] = line[1]
		d['city'] = line[2]
		data.append(d)
		i += 1
	return data
print(read_file('./work files/data.csv'))