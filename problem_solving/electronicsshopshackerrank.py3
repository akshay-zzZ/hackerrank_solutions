arr = list(map(int,input().split()))
keyboard = list(map(int,input().split()))
usb = list(map(int,input().split()))
li = []
li_2 = []
for i in keyboard:
	for j in usb :
		if(i+j < arr[0]):
			li.append(i+j)
		else :
			li_2.append(i+j)
if(len(li) == 0):
	print("-1")
else :
	print(max(li))