n = int(input())
arr = list(map(int,input().split()))
#print(arr)
li =[]
for i in range(1,n+1):
	count = 0
	for j in arr:
		count += 1
		if(i == j):
			break
	li.append(count) 	
#print(li)
for k in li:
	count_2 = 0
	for l in arr :
		count_2 += 1
		if(k == l):
			break
	print(count_2)