class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings
	
	@staticmethod
	def validate_topping(topping):
		if topping == "pineapple":
			raise ValueError("No pineapples!")
		else:
			return True
	
ingrediants = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingrediants):
	pizza = Pizza(ingrediants)

print(pizza.toppings)

fault_ingrediants = ["cheese", "pineapple"]
if all(Pizza.validate_topping(i) for i in fault_ingrediants):
	fault_pizza = Pizza(fault_ingrediants)

print(fault_pizza.topping)

