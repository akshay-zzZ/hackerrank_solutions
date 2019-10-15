s ="ABCDCDC"
s1="CDC"
count = 0
for i in range(len(s)):
	if(s[i:i+len(s1)]==s1):
		count+=1
print(count)