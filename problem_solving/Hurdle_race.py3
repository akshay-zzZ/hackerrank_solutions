n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
x = max(arr)
y = x - k
if(y > 0):
	print(y)
else :
	print("0")