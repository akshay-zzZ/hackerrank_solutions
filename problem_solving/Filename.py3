import time
st = time.time()
fib_cache = {}
def fib(n):
	if(n in fib_cache):
		return fib_cache[n]
	if(n == 1):
		value =  1
	if(n == 2):
		value =  2
	elif(n>2):
		value =  fib(n-1) + fib(n-2)
		
	fib_cache[n] = value
	return value

x = int(input())
for n in range(1,x+1):
	print(n , ":",fib(n))
et = time.time()
print("total time %0.05f"%(et-st))
    