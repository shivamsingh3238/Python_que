import time
def sort(ele):
    for i in range(len(ele)):
        swapped = True
        for j in range(0,len(ele)-i-1):
            if ele[j]>ele[j+1]:
                ele[j],ele[j+1]=ele[j+1],ele[j]
                swapped= False
        if swapped:
            break
    
#here using swapped to check all ele are sort or not if they are sorted then break 
start=time.time()#cal time taken by code
num=int(input())
ele=[int(input()) for i in range(num)]
sort(ele)
print(ele)
end=time.time()
print(end-start)
