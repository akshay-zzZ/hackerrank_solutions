T = int(input())
for i in range(T):
	n,k = list(map(int,input().split()))
	count = 0
	li = []
	for i in range(1,50):
		for j in range(1,50):
			if(i+j == n):
				count += 1
				a = (i*i-i)
				b = (j*j-j)
				li.append(a*b)
				if(count == k):
					print(a*b)
				if(count == 0):
					print("-1")
				
				
						