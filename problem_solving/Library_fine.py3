#!/bin/python3
d2,m2,y2 = list(map(int,input().split()))
d1,m1,y1 = list(map(int,input().split()))
if(y1 != y2):
    if(y2 - y1 >= 0):
        print(10000 * (y2-y1))
    else:
        print("0")
elif(m2 != m1 ):
    if(m2-m1 >= 0):
        print(500*(m2 - m1))
    else:
        print("0")
else:
    if(d2-d1 >= 0):
        print(15 *(d2-d1))
    else:
        print("0")