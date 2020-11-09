n=raw_input()
ele=[int(i) for i in n]
if len(ele)%2==0:
    l=len(ele)
else:
    l=len(ele)-1
for i in range(0,l,2):
    ele[i],ele[i+1]=ele[i+1],ele[i]
s=''
for i in ele:
    s+=str(i)
print(int(s))
    
