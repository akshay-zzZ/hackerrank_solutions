class Employee :
	
	raise_amt = 1.04
	
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + last + "@gmail.com"

	def full_name(self):
		return self.first + self.last

	def add_amt(self):
		self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
	raise_amt = 100
	
	def __init__(self,first,last,pay,lan):
		super().__init__(first,last,pay)
		self.lan = lan
		
class Manager(Employee):

	def __init__(self,first,last,pay,employees = None):
		super().__init__(first,last,pay)
		if employees is None :
			self.employees = []
		else :
			self.employees = employees
			
	
	def add(self,emp):
		if emp not in self.employees :
			self.employees.append(emp)
			
			
	
	def remove(self,emp):
		if emp in self.employees :
			self.employees.remove(emp)
	
	
	
	def print_emps(self):
		for emp in self.employees:
			print("-->",emp.full_name())
			
	
	
emp_1 = Developer("Alf","Mans",100,"Python")
emp_2 = Developer("ab","sjsh",27272,"java")

mgr_1 = Manager("corey","schafrr",90000,[emp_1])
print(mgr_1.email)

mgr_1.print_emps()
mgr_1.add(emp_2)