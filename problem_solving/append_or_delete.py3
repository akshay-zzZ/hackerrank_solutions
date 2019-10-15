s = input()
t = input()
k = int(input())
lens = len(s)
lent = len(t)
count = 0
if(s == t):
    print("Yes")
else:
    for i in range(min(lens,lent)):
    	if(s[i] != t[i]):
    		break
    	else :
    		count+=1
    lent= lent - count
    lens= lens - count
    print(count)
    if(k <=  lent + lens or (lens < lent and count % k != 0)):
        print("No")
    else :
        print("Yes")