n = int(input())
s = input()
print(s)
print("Lipps_Asvph")
k = int(input())
li = []
li_3 = []
for i in s :
	li_3.append(ord(i))
print(li_3)
li_2 = []
for i in s:
	if(ord(i) > 96):
		li.append(ord(i) + k)
	elif(ord(i) == (91 or 92 or 93 or 94 or 95 or 96)):
		li.append(i)
	elif(ord(i) > 64 and ord(i) < 91):
		li.append(ord(i) + k)
	else:
		li.append(ord(i))
print(li)
for i in li :
	if(i > 122 ):
		i =(i - 122) + 96
		li_2.append(i)
	elif(i > 90 and i < 97):
		i = (i - 90) + 64
		li_2.append(i)
	elif(i == 44 or i == 45):
		li.append(i)
	else :
		li_2.append(i)
print(li_2)
for x in li_2 :
	print(chr(x),end = "")
#print(ord("_"))
#print(chr(90))
