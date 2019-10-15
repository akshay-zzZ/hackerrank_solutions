n = int(input())
arr = list(map(int,input().split()))
count = -1
count_2 = -1
li = []
for i in arr :
	count += 1
	for j in arr :
		count_2 += 1
		if(i == j ):
			li.append(abs(count_2 - count))
			#print(li)
		if(count_2 == len(arr)-1):
			count_2 = -1
x = (set(li))
a = list(x)
a.sort()
if(len(a) == 1):
	print("-1")
else :
	print(a[1])