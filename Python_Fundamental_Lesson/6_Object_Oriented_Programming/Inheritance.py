class Animal:
	def __init__(self, name, color):
		self.name = name
		self.color = color

class Cat(Animal):
	def voice(self):
		print("Purr...")

class Dog(Animal):
	def voice(self):
		print("Woof!")
	
fido = Dog("Fido", "brown")
print(fido.color)
fido.voice()

