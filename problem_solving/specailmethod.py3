class Employee:

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + last +"@"
	
	def fullname(self):
		return self.first + self.last
		
	def __repr__(self):
		return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
	
	def __str__(self):
		return '{} - {}'.format(self.fullname(),self.email)
	
	def __add__(self,other):
		return self.pay + other.pay

emp_1 = Employee("Alfaiz","Mansuri",10000)
emp_2 = Employee("badshah","khan",20000)

#print(str(emp_1))
#print(repr(emp_1))

#print(emp_1 + emp_2)