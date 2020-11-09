ele=list(map(int,raw_input().split()))
##for i in range(len(ele)):
##    if ele[i] in ele[i+1:]:
##        print(ele[i])
##        print(i)
##        break
for i in range(len(ele)):
    if ele.count(ele[i])>=2:
        print(ele[i])
        break
