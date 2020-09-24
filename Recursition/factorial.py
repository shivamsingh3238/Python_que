#factorial using recursion
def fact(n):
    print(n,end=" ")
    if n==0 or n==1:
        return 1
    else:
        
        return (n*(n-1))






n=int(input())
result=fact(n)
print(result)
