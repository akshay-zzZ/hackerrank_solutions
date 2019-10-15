import math
i,j,k = list(map(int,input().split()))
li =[]
li_2 = []
for n in range(i,j+1):
	li_2.append(n)

	rev=0
	while(n>0):
		dig=n%10
		rev=rev*10+dig
		n=n//10
	li.append(rev)
C = [abs((a-b)/k) for a, b in zip(li, li_2)]
count = 0
for x in C :
	if(x - math.floor(x) == 0):
		count += 1
print(count)