n,t = list(map(int,input().split()))
N = list(map(int,input().split()))
li = []
for i in range(t):
	a,b = list(map(int,input().split()))
	for val in N[int(a):int(b)+1]:
		li.append(val)
	print(min(li))
	li = []
	
