import math

print("первая задача:")
print('введите несколько цифр(0 для окончания ввода): ')
a = []
b = float(input())

while b != 0:
    a.append(b)
    b = float(input())
print(f'{max(a)}')

print('вторая задача:')

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        a = math.pi * (self.radius ** 2)
        print(f'ваша площадь: {a}')
    def dlina(self):
        p = math.pi
        m = p * 2 * self.radius
        print(f'ваша длина: {m}')
d = float(input('введите радиус круга: '))
c = Circle(d)
c.area()
c.dlina()