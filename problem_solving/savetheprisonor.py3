t = int(input())
for i in range(t):
	pri,swe,num = list(map(int,(input().split())))
	counter = num - 1
	for i in range(num,swe+num):
		counter += 1
		if(counter == pri and i != swe+num):
			counter = 0
	print(counter)
	