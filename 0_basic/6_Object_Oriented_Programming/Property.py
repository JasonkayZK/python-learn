class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def flag_pineapple_allowed(self):
        return False


pizza = Pizza(["cheese", "tomato"])
print(pizza.flag_pineapple_allowed)
pizza.flag_pineapple_allowed = True
