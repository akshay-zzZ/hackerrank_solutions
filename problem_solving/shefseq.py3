T = int(input())
for i in range(T):
	n ,k= list(map(int,input().split()))
	arr = list(map(int,input().split()))
	arr_sum = sum(arr)	
	arr_sq = [x*x for x in arr ]	
	arr_sq.sort(reverse = True)
	a = 0
	for i in range(k):
		arr_sq[a] =1 
		a+=1
	if(sum(arr_sq) <= arr_sum):
		print('YES')
			
	else :
		print('NO')