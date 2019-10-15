class Employee:

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first + self.last + '@company.com'
	
	def fullname(self):
		return self.first + self.last
		
	@classmethod
	def from_emp_str(cls,emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay)
		
	
emp_1 = Employee("Alfaiz","Mansuri",100000)
emp_2 = Employee("Man","Alf",50000)

#print(emp_1.fullname())

new_emp1 = 'Alfaiz-mansuri-10000'
new_emp2 = 'corey-schafer-20000'

str = Employee.from_emp_str(new_emp2)
print(str.email)
print(str.fullname())