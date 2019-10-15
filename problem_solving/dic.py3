n = int(input())
s = input()
special = "!@#$%^&*()-+"
count = 0
lower = 0
upper = 0
digit = 0
sp = 0
leng = 0
for x in s :
	if(x.isupper()):
		upper += 1
	elif(x.islower()):
		lower += 1
	elif(x.isdigit):
		digit += 1
	elif x in special:
		sp += 1
if(upper == 0):
	count += 1
if(lower == 0):
	count += 1
if(digit == 0):
	count += 1
if(sp == 0):
	count += 1
if((lower + upper + sp + digit+count) < 6):
	count = count +(6- (count+lower + upper + sp + digit))
print(count)