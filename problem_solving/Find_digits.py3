T = int(input())
for i in range(T):
	n = int(input())
	digits = [int(x) for x in str(n)]
	count = 0
	li =[]
	for i in digits :
		if( i != 0  and n % int(i) == 0):
			count += 1
			li.append(count)
	print(max(li)) 