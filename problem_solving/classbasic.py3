class Person :
	def __init__(self,fname,lname,age):
		self.x=fname
		self.y=lname
		self.z=age
	
	def full_name(self):
		return self.x + " " + self.y

A = Person("Alfaiz","Mansuri",24)
print(A.full_name())
