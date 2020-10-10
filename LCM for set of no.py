def find(num1 , num2):
    if num1 > num2:
        max=num1
        min=num2
    else :
        max = num2
        min = num1
    while(min):
        max,min=min, max%min
    #print(max)
    return ((num1*num2)// max)
    


ele=list(map(int,input().split()))
num1=ele[0]
num2=ele[1]
lcm=find(num1 , num2)
for i in range(2,len(ele)):
    lcm = find(lcm ,ele[i])
print(lcm)
