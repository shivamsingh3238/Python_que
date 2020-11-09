n=int(input())
ele=list(map(int,raw_input().split()))
ele=sorted(ele)
a=ele[len(ele)-1]
b=ele[len(ele)-2]
print(a+b)
