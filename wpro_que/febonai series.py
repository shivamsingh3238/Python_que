a=1
b=1
n=int(input())
for i in range(2,n):
    a,b=b+a,a
print(a)
