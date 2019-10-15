T = int(input())
for i in range(T):
	n ,k= list(map(int,input().split()))
	arr = list(map(int,input().split()))
	
	arr.sort(reverse = True)
	a = 0
	for i in range(k):
		arr[a] =1 
		a+=1
	arr_sum = sum(arr)	
	arr_sq = [x*x for x in arr ]	
	if(sum(arr_sq) <= arr_sum):
		print('YES')
	else :
		print('NO')
