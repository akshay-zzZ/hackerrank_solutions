class String:
	def __init__(self,string):
	 	self.string = string
	 	print("All the best")

	def __repr__(self):
		return '{}'.format(self.string)

	def __add__(self,other):
		return self.string + other

String1 = String("Saala goli mar denge")
print(String1 + " Bihar se he")