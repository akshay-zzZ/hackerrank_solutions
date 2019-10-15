n = int(input())
arr = list(map(int,input().split()))
d,m = list(map(int,input().split()))
count = 0
for i in range(0,n):
	x = 0
	for j in range(i,m):
		if(j < n):
			x += arr[j]
	if( x == d):
		count += 1
	m += 1
print(count)
    