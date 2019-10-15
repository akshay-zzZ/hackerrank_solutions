class student:
	def __init__(self):
		self.name = 'alfaiz'
		self.age = 18
		self.marks = 86
	
	def talk(self) :
		print('Hello my name is :', self.name)
		print('My age is :',self.age)
		print('My marks is :',self.marks)
s=student()
s.talk()