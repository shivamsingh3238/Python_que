n,ss=input().split()
str=[]
f=[]
for i in range(int(n)):
    str.append(input().lower())
j=0
while(j<int(n)):
    s=''
    space=' '
    for i in str[j]:
        
        if i.isalpha():
            if i.isupper():
                a= ord(i)
                c=a-97
                s=s+ ss[c].upper()
            if i.islower():
                a= ord(i)
                c=a-97
                s=s+ss[c]
        else:
            s=s+space
    f.append(s)
    j+=1
for i in f:
    print(i)
    
        
