def set_maker(ls,k):
    l=len(ls)
    t=[]
    for i in range(0,l):
        if i+k>l:
            continue
        else:
            t1=[]
            for j in range(i,i+k):
                t1.append(ls[j])
            t.append(t1)
    return t
        




ls=list(map(int,input().split()))
k=int(input())
patten=set_maker(ls,k)
for i in patten:
    print(i)
