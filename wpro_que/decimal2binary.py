def decimal2binary(n):
    if n>1:
        decimal2binary(n//2)
    print(n%2),
    


n=int(input())
decimal2binary(n)
