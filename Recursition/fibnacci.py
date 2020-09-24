#fibonacci series using recursion
def fib(n):
    #0 1 1 2 3 5 8
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return (fib(n-1) + fib(n-2))
    



n=int(input())
for i in range(0,n+1):
    print(fib(i),end=" ")
