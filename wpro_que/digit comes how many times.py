s=input()
c=dict()
for i in range(len(s)):
    if c.get(s[i]):
        c[s[i]]+=1
    else:
        c[s[i]]=1
print(c)
count=0
for i,j in c.items():
    if j==1:
        count+=1
        print(i,end="")
print(count)
