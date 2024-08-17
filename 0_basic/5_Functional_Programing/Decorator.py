def decor(func):
	def wrap():
		print("===================")
		func()
		print("===================")
	return wrap

def decor2(func):
	def wrap():
		print("*******************")
		func()
		print("*******************")
	return wrap

def print_text():
	print("Hello world!")

print_text = decor(print_text)
print_text()

@decor
@decor2
def print_str():
	print("Hello World2!")

print_str()

@decor2
@decor
def print_str2():
	print("Hello world3!")

print_str2()

