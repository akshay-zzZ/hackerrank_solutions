#		x_x		
n,m = input().split()
n = int(n)
m = int(m)
lis = [0]*n
while m:
	in = list(map(int,input().split()))
	lis[in[0]-1] = lis[in[0]-1] + in[k]
	lis[in[1]] = lis[in[1]] - in[k]
val = lis[0];
for i in range(1,n):
	val = val + lis[i]
	if val>max:
		max = val
print(max)
