s = input()
s_2 = len(s)//3 * 'SOS'
count = 0
for i in range(len(s)):
	if(s[i] != s_2[i]):
		count += 1
print(count)