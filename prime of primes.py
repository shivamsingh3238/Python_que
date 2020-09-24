n=int(input())
t=[]
for i in range(2,n+1):
    flag = 1
    #print(i // 2 + 1)
    for j in range(2, i // 2 + 1):
        
        if (i % j == 0):
            flag = 0
            break
    if (flag == 1):
       t.append(i)
count=0
for i in t:
    l=list(map(int,str(i)))
    print(l)
    if 0 not in l and 1 not in l:
        count+=1
      
        
print(count)

         
  
