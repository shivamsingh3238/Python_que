n=input()
a=list(n)
s1=''
s2=''
even=''
odd=''
for i in a:
    if i.isalpha():
        if i.isalpha() and i.istitle():
            s1 = s1 + i
        else:
            s2 = s2 + i
for i in a:
     if i.isdigit():
         if i.isdigit() and int(i)%2==0:
             even=even+i
         else:
             odd=odd+i
print(s1+s2+even+odd)
        
        
        
        
