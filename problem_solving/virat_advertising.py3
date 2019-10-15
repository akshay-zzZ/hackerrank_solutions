n = int(input())
l = []
s = 5
s = 5 // 2
l.append(s)
for i in range(2,n+1):
	s = s * 3
	s = s // 2
	l.append(s)
print(sum(l))