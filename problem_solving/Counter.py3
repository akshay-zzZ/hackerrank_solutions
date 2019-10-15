from collections import Counter
mylist = [1,2,2,1,3,2,1,3,4]
print(Counter(mylist))
print(Counter(mylist).items())
print(Counter(mylist).keys())
print(Counter(mylist).values())