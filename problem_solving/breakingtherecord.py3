n = int(input())
arr = list(map(int,input().split()))
high = arr[0]
low  = arr[0]
count_1 = 0
count_2 = 0
for i in arr :
	if(i > high):
		high = i
		count_1 += 1
for j in arr :
	if(j < low):
		low = j
		count_2 += 1
print(count_1,count_2)