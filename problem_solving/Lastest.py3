arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
x = 0
count = 1
count2 = 0
while(x != len(arr2)):
	for i in range(1,int(arr2[x])+1):
		#print(i)
		if(i == arr[1]):
			count += 1
		if(i == count):
			count2 += 1
		
	x += 1
print(count2)