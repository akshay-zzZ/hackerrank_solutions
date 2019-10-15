n = int(input())
for i in range(n):
	s = input()
	#print(s)
	s_2 = 'hackerrank'
	#print(s_2)
	count = 0
	count_2 = -1
	for i in s_2 :
		for j in s :
			count_2 += 1
			#print(i,j)
			if(i == j):
				count += 1
				s = s[count_2:]
				count_2 = 0
				#print(s)
				break
	#print(count)
	if(count < 10 ):
		print("NO")
	else :
		print("YES")
