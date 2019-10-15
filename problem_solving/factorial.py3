import math
li = {}
def factorial(n):
	if(n==0):
		return 1
	else:
		fact = n*factorial(n-1)
		li=fact
		return fact
print(factorial(900))
print(li[3])
	