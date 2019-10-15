b = [1,2,3,4,-3,-6]
print(b)
total = 0
i = 0
while True :
    total += b[i]
    i += 1
    if b[i] <= 0:
        break
print(total)