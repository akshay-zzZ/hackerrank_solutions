n = int(input())
s = input()
print(s)
k = int(input())
li = []
li_3 = []
li_2 =[]
for i in range(97,123):
	li.append(i)
for j in li :
	j+=k
	li_2.append(j)
for l in li_2:
	if(l > 122):
		l = l - 122
		li_3.append(l+97)
		#l = 97+l
	if(l > 96 and l < 123):
		li_3.append(l)
li_4 = []
li_5 =[]
for p in s :
	li_5.append(ord(p))
for y in s :
	if(ord(y)+k > 122):
		a= ord(y) - 122
		li_4.append(chr(a+97))
	else :
		li_4.append(chr(ord(y)))
print(li_4)
print(li_5)