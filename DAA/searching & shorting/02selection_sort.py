def sort(ele):
    for i in range(0,len(ele)):
        min=i
        for j in range(i+1,len(ele)):
            if ele[j]<ele[min]:
                min=j
        ele[i],ele[min]=ele[min],ele[i]

num=int(input())
ele=[int(input()) for i in range(num)]
sort(ele)
print(ele)
