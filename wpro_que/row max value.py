r,c=raw_input().split()
ele=[]
for i in range(int(r)):
    ele.append(list(map(int,raw_input().split())))
for i in range(len(ele)):
    print(max(ele[i])),
