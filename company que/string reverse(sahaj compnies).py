s= input()
w=4
Ns=''
for i in s:
    if i==" ":
        continue
    else:
        Ns=Ns+i
ele=[]
i=0
while(i<=len(Ns)):
    ele.append(list(Ns[i:i+4]))
    i+=4
flist=[]
print(ele)
j=0
ln=(len(max(ele)))
while(j<ln):
    st=''
    for i in range(ln):
        if len(ele[i])==0:
            continue
        else:
            st=st+ele[i].pop(0)
    flist.append(st)
    j+=1
print(flist)
for i in flist:
    print(i,end=" ")
        
        
    

    
