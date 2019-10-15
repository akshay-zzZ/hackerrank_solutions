h = list(map(int,input().split()))
word = input()
li = [] 
for i in word:
	A =((ord(i)))
	li.append(A)
B= (max(li))
ch = B -96
print(max(h[:ch])*len(word))