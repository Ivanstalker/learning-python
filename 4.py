import statistics
print('перва задача')
student = {'Имя': 'Иван',
           'Возраст': '13',
           'Математика' : [5,4,5,4,5,3],
           'Русский' : [5,4,4,3,5,3,4,5],
           'Биология' : [5, 5, 4, 5, 4]
}
print(f'средний  балл: {round(statistics.mean(student.get("Математика")+ student.get("Русский") + student.get("Биология")), 2)}')

print('вторая задача')
nums1 = {123, 34345, 45677, 11, 44}
nums2 = {4567382, 2123 , 3454, 466, 66}
print(f'{sorted(nums1)}\n{sorted(nums2)}')

print(f'обьединение: {nums1.union(nums2)}\nпересечение: {nums1.intersection(nums2)}\nразность: {nums1.difference(nums2)}')

print('третья задача')

class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def area(self):
		return self.width * self.height