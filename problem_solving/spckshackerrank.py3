from collections import Counter
from functools import reduce
n = int(input())
arr = list(map(int,input().split()))
z = Counter(arr)
s = z.values()
li = []
for i in s:
	if(i>=1):
		l = (i//2)
		li.append(l)
sum = reduce(lambda x,y:x+y,li)
print(sum)