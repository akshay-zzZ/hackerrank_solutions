T = int(input())
for i in range(T):
	n ,k= list(map(int,input().split()))
	arr = list(map(int,input().split()))
	arr_sum = sum(arr)	
	arr_sq = [x*x for x in arr ]	
	arr_sq.sort(reverse = True)
	a = 0
	print(arr)
	print(arr_sum)
	print(arr_sq)
	for i in range(k):
		arr_sq[a] =1 
		a+=1
	print(arr_sq)
	print(sum(arr_sq))
	print(arr_sum)
	if(sum(arr_sq) <= arr_sum):
		print('YES')
	else :
		print('NO')