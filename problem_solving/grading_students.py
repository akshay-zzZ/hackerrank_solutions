''' ***
	 *
	*** '''
n = int(input())
while n:
	n=n-1
	num = int(input())
	if num<38 or (num%5)<3:
		print(num)
	else:
		print(num+(5-(num%5)))
