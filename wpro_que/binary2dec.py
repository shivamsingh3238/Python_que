s=raw_input()[::-1]
ele=[int(i) for  i in s]
sum=0
for i in range(len(ele)):
    sum+= ele[i]*pow(2,i)
print(sum)
