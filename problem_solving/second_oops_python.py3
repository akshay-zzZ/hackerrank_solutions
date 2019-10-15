class student:
	def __init__(self,name,age,marks):
		self.name = name
		self.age = age
		self.marks = marks
	
	def talk(self) :
		print('Hello my name is :', self.name)
		print('My age is :',self.age)
		print('My marks is :',self.marks)
s1=student('Al',20,90)
s1.talk()

s2=student('bb',23,95)
s2.talk()

s3=student ('shin',24,80)
s3.talk()