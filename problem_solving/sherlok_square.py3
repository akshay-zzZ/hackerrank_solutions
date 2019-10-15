import math
t = int(input())
for i in range(t):
	a,b = list(map(int,input().split()))
	count = (math.floor(math.sqrt(b))- math.ceil(math.sqrt(a))) + 1
	print(count)