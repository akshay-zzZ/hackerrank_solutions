s = input()
n = int(input())
s = s[:n]*len(s) + s[:n%len(s)]
print(s)
count = 0
for char in s :
	if char == 'a':
		count += 1
print(count)
		

	