n = int(input())
for i in range(n):
	arr_1 = list(map(int,input().split()))
	if(abs(arr_1[2]-arr_1[1]) < abs(arr_1[2]-arr_1[0]) ):
		print('Cat B')
	if(abs(arr_1[2]-arr_1[1]) > abs(arr_1[2]-arr_1[0]) ): 
		print('Cat A')
	if(abs(arr_1[2]-arr_1[1]) == abs(arr_1[2]-arr_1[0]) ):
		print('Mouse C')
    