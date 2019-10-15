t = int(input())
for i in range(t):
    N = int(input())
    tickets = list(map(int,input().split()))
    li =[]
    li2 =[]
    for x in tickets:
        i = tickets.index(x)+2
        for y in tickets[i:]:    
            li.append(str(y)+str(x))
            li2.append(x+y)
            if(i<len(tickets)):
                i+=1
        #print(li)
       # print(li2)
    p=(str(li[li2.index(max(li2))]))
    if(len(p)>1):
        p=p[2:]
        for f in p :
            print(f,end="")
    else:
        print(p)
        
    #print(len(str(li2[(li2.index(max(li2)))])))
    li =[]
    li2=[]
    


