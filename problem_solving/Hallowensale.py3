p,d,m,s = list(map(int,input().split()))
#print(p,d,m,s)
li = []
li.append(p)
x = 0
while(x <= s):
	x = sum(li)
	p -= d
	if(p >= m and x <= s):
		li.append(p)
	else :
		if(x <= s):
			li.append(m)
	#x = sum(li)
li.pop()
print(len(li))
#print(x)
#print(s)