n = int(input())
s = input()
count_1 = 0
valley = 0
for i in s :
	if(i == 'U'):
		count_1 += 1
	else:
		count_1 -= 1
	if(count_1 == 0 and i == 'U'):
		valley += 1
print(valley)