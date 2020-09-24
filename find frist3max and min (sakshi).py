n=int(input())
list=[int(input()) for _ in range(0,n)]
list.sort()
length=len(list)
max=[]
min=[]
c=0
while(c!=3):
    c+=1
    min.append(list[c-1])
    max.append(list[length-c])
    
print(max)
print(min)
for i in range(0,len(max)):
    print( i+1,'min value is',min[i])
    print( i+1,'max value is',max[i])

   
