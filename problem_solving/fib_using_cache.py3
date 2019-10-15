from functools import lru_cache
import time

st = time.time()
#by default max size is 120
@lru_cache(maxsize = 1000)
def fib(n):
	if(type(n) != int):
		raise TypeError(" n must be a positive integer")
	if(n < 1):
		raise ValueError("n must be positive integer")
	if(n == 1):
		return 1
	elif(n == 2):
		return 2
	elif(n>2) :
		return fib(n-1) + fib(n-2)
	
x = int(input())
for n in range(1,x+1):
	print(n ,":",fib(n))
et = time.time()

print("total time %0.5f "%(et-st))
    