class A:
	def spam(self):
		print(1)

class B(A):
	def spam(self):
		print(2)
	def superspam(self):		
		super().spam()

B().spam()
B().superspam()


