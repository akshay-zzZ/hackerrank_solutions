n,m =  list(map(int,input().split()))
arr_1 = list(map(int,input().split()))
arr_2 = list(map(int,input().split()))	
count = 0
for i in range(arr_1[-1],arr_2[0]+1):
	if all(i % j == 0 for j in arr_1) and all(k % i == 0 for k in arr_2):
		count += 1
print(count)