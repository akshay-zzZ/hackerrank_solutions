n = int(input())
lst = list(map(int,input().split()))
x = (max(lst,key=lst.count))
count = 0
for i in lst :
	if(i == x):
		count += 1
print(len(lst)-count)