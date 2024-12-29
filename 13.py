squares = [x**6 for x in range(10)]
print(squares)

even_numbers = [x for x in range(1, 20 + 1) if x % 2 == 0]
print(even_numbers)

[print(x) for x in range(5)]

names = ['Mike', 'Dennis', 'Rey']
ages = [12, 62, 34]

d = {a: b for a, b in zip(names, ages)}
print(d)