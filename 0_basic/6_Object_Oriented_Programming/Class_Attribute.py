class Dog:
	legs = 4
	def __init__(self, name, color):
		self.name = name
		self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)

fido.legs = 7
print(fido.legs)
print(Dog.legs)

Dog.legs = 6
print(fido.legs)
print(Dog.legs)


