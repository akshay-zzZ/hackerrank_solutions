x1,v1,x2,v2 = list(map(int,input().split()))
for i in range(10000):
	x1 = x1 + v1
	x2 = x2 + v2
	if(x1 == x2):
		print("YES")
		break
else:
	print("NO")
