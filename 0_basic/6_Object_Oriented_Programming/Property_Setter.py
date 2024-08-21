class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._flag_pineapple_allowed = False

    @property
    def flag_pineapple_allowed(self):
        return self._flag_pineapple_allowed

    @flag_pineapple_allowed.setter
    def flag_pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "zk137818":
                self._flag_pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")


pizza = Pizza(["cheese", "tomato"])
print(pizza.flag_pineapple_allowed)
pizza.flag_pineapple_allowed = True
print(pizza.flag_pineapple_allowed)
