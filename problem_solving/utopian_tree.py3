t = int(input())
for i in range(t):
	x = int(input())
	if( x == 0):
		print("1")
	elif( x == 1):
		print("2")			
	else:
		a = 1
		for i in range(1,x+1):
			if(i % 2 != 0):
				a = a*2
			else:
				a= a+1
		print(a)