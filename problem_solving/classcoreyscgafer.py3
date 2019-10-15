class Employee :
	def __init__(self,first,last,Pay):
		self.first = first
		self.last = last
		self.Pay = Pay
		self.email = first + last + '@company.com'

	def fullname(self):
		return (self.first+self.last)

emp_1 = Employee("Alfaiz","Mansuri",10000)
emp_2 = Employee("abc","xyz",200000)

print(emp_1.fullname())
print(emp_1.email)
print(emp_1.Pay)