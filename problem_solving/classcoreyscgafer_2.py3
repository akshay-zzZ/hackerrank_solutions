class Employee :

	raise_amount = 1.04
	num_of_emps = 0
	
	def __init__(self,first,last,Pay):
		self.first = first
		self.last = last
		self.Pay = Pay
		self.email = first + last + '@company.com'
		Employee.num_of_emps += 1

	def fullname(self):
		return (self.first+self.last)
	
	def add_amount(self):
		self.Pay = (self.Pay * self.raise_amount)

emp_1 = Employee("Alfaiz","Mansuri",10000)
emp_2 = Employee("abc","xyz",200000)

print(emp_1.fullname())
print(emp_1.email)
print(emp_1.Pay)
emp_1.add_amount()
print(emp_1.Pay)

Employee.raise_amount = 1.05
emp_1.add_amount()
print(emp_1.Pay)
print(Employee.num_of_emps)

