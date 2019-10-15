n = int(input())
li = []
li_2 = []
li_3 = []
li_4 = []
for i in range(n):
	s = input()
	s2 = s[::-1]
	#print(s,s2)
	for i in s :
		li.append(ord(i))
	x = 0
	y = 1
	for j in range(len(li)):
		li_2.append(abs(li[x]-li[y]))
		if(y < len(li_2)):
			x+= 1
			y+= 1
	#print(li)
	#print(li_2)
		
	for p in s2:
		li_3.append(ord(p))
	a = 0
	b = 1
	for q in range(len(li_3)):
		li_4.append(abs(li_3[a]-li_3[b]))
		if(b < len(li_4)):
			a+= 1
			b+= 1 	
	if(li_2 == li_4):
		print("Funny")
	else :
		print("Not Funny")
	li = []
	li_2 = []
	li_3 = []
	li_4 = []
	