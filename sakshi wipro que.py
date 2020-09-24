#how many student get 0 i aur full marks and prnt same no getting marks
dic={}
n=int(input())
for i in range(0,n):
    dic[i]=int(input())
zero=0
one=0
full=0
for i,j in dic.items():
    if j==0:
        zero+=1
    if j==1:
        one+=1
    if j==100:
        full+=1
res={}
temp=[]
for i,j in dic.items():
    temp.clear()
    for k,l in dic.items():
        if j==l:
            temp.append(k)
        res[j]=temp.copy()
print(res)
print(zero)
print(one)
print(full)
    
    
    
