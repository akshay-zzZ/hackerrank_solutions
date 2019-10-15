n = int(input())
arr = sorted(list(map(int,input().split())))
print(len(arr))
while(len(arr) > 0):
	arr = [ x for x in arr if x != min(arr)]
	if(len(arr) == 0):
		break
	print(len(arr))
