n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
count = 0
r = 0
li =  []
for i in range(len(arr)):
	r+=1
	for j in range(r,len(arr)):
		l = arr[j]+arr[i] %k
		li.append(l)
for num in li :
	if (num%k == 0):
		count += 1
	
print(count)
    