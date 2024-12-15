print('перва задача \n')
import statistics
student = {'Имя': 'Иван',
           'Возраст': '13',
           'Математика' : [5,4,5,4,5,3],
           'Русский' : [5,4,4,3,5,3,4,5],
           'Биология' : [5, 5, 4, 5, 4]
}
print(f'средний  балл: {round(statistics.mean(student.get("Математика")+ student.get("Русский") + student.get("Биология")), 2)}')
print('\n')

print('вторая задача \n')
nums1 = {123, 34345, 45677, 11, 44}
nums2 = {4567382, 2123 , 3454, 466, 66}
print(f'{sorted(nums1)}\n{sorted(nums2)}')

print(f'обьединение: {nums1.union(nums2)}\nпересечение: {nums1.intersection(nums2)}\nразность: {nums1.difference(nums2)}')
print('\n')

print('третья задача \n ')

class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def area(self):
		return self.width * self.height
	def perimeter(self):
		return 2 * self.width + 2 * self.height
	def __str__(self):
		return f'прямоугольник со сторонами: ширина = {self.width}, высота = {self.height}'

r = Rectangle(5, 14)
print(r)
print('площадь = ', r.area())
print('\n')
print('четвертая задача \n')
import random

my_list = ['banana', 'malina', 'apple']
random.shuffle(my_list)
not_list = random.choice(my_list)
print(my_list)
print(not_list)

print('\n')

print('пятая задача \n')
import datetime as dt

now = dt.datetime.now()
print(now)

print('\n')
print('шестая задача \n')

