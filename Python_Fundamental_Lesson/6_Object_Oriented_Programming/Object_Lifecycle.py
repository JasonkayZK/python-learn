a = 42 # Create the object <42>
b = a # Increase ref.count of <42>
c = [a] # Increase ref.count of <42>

del a # Decrease ref.count of <42>
b = 100 # Decrease ref.count of <42>
c[0] = -1 # Decrease ref.count of <42>



