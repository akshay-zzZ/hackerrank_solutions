n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
count = 100
i = 0
li = []
p = (i+k) % n
if(p == 0):
	count = count - 3
	print(count)
else:
	for j in range(0,n,p):
		li.append(j)

	c = [arr[x] for x in li]
	for y in c :
		if(y == 1):
			count = count - 3
		else:
			count = count -1
	print(count)
    