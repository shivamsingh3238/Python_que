def gcd(x,y):
    res=0
    while(y):
        x,y=y,x%y
    return x
        
    
n1=int(input())
n2=int(input())
temp=0
if n1 < n2:
    temp=n1
    n1=n2
    n2=temp
result=gcd(n1,n2)
print(result)
    
