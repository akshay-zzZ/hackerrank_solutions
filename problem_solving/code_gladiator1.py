t = int(input())
for i in range(t):
    counter=0
    N = int(input())
    vill = list(map(int,input().split()))
    player= list(map(int,input().split()))
    player.sort(reverse=True)
    vill.sort(reverse=True)
    for x,y in zip(player,vill):
        if(x-y>0):
            counter+=1
    if(counter==N):
        print('WIN')
    else:
        print('LOSE')
    





