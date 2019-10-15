n = int(input())
p = int(input())
if(p == 1 or p == n or p == n-1  ):
	print("0")

else:
	count = 0
	count_2 = 0
	for i in range(2,n,2):
		count += 1
		if(i == p or i+1 == p):
			break
	for j in range(n-2,0,-2):
		count_2 += 1
		if(j == p or j-1 ==p):
			break
	print(count)
	print(count_2)
	if(count < count_2):
		print(count)
	else :
		print(count_2)