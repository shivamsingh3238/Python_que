ele=raw_input().split()
a=int(ele[0])
sum=a
b=int(ele[len(ele)-1])
while(b!=1):
    sum+=int(ele[1])
    b-=1
print(sum)

