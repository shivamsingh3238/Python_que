result=[]
def prime(k):
    if k<1:
        result.append(k)
        return
    for i in range(2,k):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            result.append(i)



ele=raw_input().split()
for i in ele:
        prime(int(i))
print(result)
print(abs(max(result)+min(result)))
