n = int(input())
a = list(input())
 
A = [0]*26
B = [0]*26
 
j = n//2
for i in range(n//2):
    A[ord(a[i]) - ord("a")] += 1
    B[ord(a[j]) - ord("a")] += 1
    j+=1
 
def case1(a,b):
    A = list(a)
    B = list(b)
    ans = A[0]
    A[25]+=ans
    A[0] = 0
    for i in range(1,26):
        req = A[i]
        for j in range(i):
            if B[j]>=req:
                B[j]-=req
                req=0
            else:
                req-=B[j]
                B[j]=0
            if req==0: break
        ans+=req
    return ans
 
def case2(a,b):
    A = list(a)
    B = list(b)
    ans = A[25]
    A[0]+=ans
    A[25] = 0
    for i in range(24,-1,-1):
        req = A[i]
        for j in range(i+1,26):
            if B[j]>=req:
                B[j]-=req
                req=0
            else:
                req-=B[j]
                B[j]=0
            if req==0: break
        ans+=req
    return ans
 
def case3(a,b,n):
    ans =  n
    for i in range(26):
        ans-=2*min(A[i],B[i])
    return ans//2
 
c1 = case1(A,B)
c2 = case2(A,B)
c3 = case3(A,B,n)
print(min(c1,c2,c3))
