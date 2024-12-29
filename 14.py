def nom_to_rim(num):
	d = {
		1: 'I',
		4: 'IV',
		5: 'V',
		9: 'IX',
		10: 'X',
		40: 'XL',
		50: 'L',
		90: 'XC',
		100: 'C',
		400: 'XD',
		500: 'D',
		900: 'CM',
		1000: 'M',
	}
	nums = list(d)
	symbols = list(d.values())

	i = 12
	result = ''
	while num != 0:
		if nums[i] <= num:
			result += symbols[i]
			num -= nums[i]
		else:
			i -= 1
	return result

def rome_to_num(num):
	n = {
	'I': 1,
	'IV': 4,
	'V': 5,
	'IX': 9,
	'X': 10,
	'XL': 40,
	'L': 50,
	'XC': 90,
	'C': 100,
	'XD': 400,
	'D': 500,
	'CM': 900,
	'M': 1000
	}
	result = 0
	prev_value = 0

	for char in reversed(num):
		value = n[char]
		if value < prev_value:
			result -= value
		else:
			result += value
		prev_value = value
	return result

print(nom_to_rim(2024))
print(rome_to_num('MMXXIV'))
print(rome_to_num('MCMXCIV'))