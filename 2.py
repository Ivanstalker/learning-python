class Сat:
	def __init__(self, name, color):
		self.name = name
		self.color = color

	def names(self):
		print(f' hi i`m {self.name}, and i`m {self.color}! ')

	def make_sound(self):
		print('Meow!')

	def sleep(self):
		print('cat is sleeping')


c = Сat('barsic', 'black')
c.names()
c.make_sound
c.sleep()


class animal:
	def __init__(self, name):
		self.name = name

	def speak(self):
		print('zvyki animal')


class bird(animal):
	def __init__(self, name):
		super().__init__(name)

	def fly(self):
		print('fly')

animal = animal('ww1')
animal.speak()

