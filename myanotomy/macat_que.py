
#take m and n input and n no od days or m no of production find max production in each day
n,m=map(int,input().split())
t=[]

for i in range(0,n):
    temp=list(map(int,input().split()))
    t.append(temp)
    #print(temp)
for i in t:
    print(max(i),end=' ')
