a = int(input())
b = set(map(int,input().split()))
c = int(input())
d = set(map(int,input().split()))
r = b|d
print(len(r))