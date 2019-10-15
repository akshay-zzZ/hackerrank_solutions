n,k,q = list(map(int,input().split()))
arr = list(map(int,input().split()))
li_2 = []
for x in range(q):
	a  = int(input())
	li_2.append(a)	
for i in range(k):
	a = arr.pop()
	arr.insert(0,a)
for i in li_2:
	print(arr[i])