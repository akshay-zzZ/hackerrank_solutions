def is_leap(y):
	leap = false 
	if y % 4 == 0 and (y % 400 == 0 or y  % 100 != 0)):
	return leap 

y = int(input())
print(is_leap(y))
