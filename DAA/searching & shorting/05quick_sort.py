def partation(ele,start,end):
    pivot=ele[end]
    i=start-1
    for j in range(start,end):
        if ele[j] <=pivot:
            i+=1
            ele[i],ele[j]=ele[j],ele[i]
    ele[i+1],ele[end]=ele[end],ele[i+1]
    return i+1


def quicksort(ele,start,end):
    if start < end:
        pi=partation(ele,start,end)
        quicksort(ele,start,pi-1)
        quicksort(ele,pi+1,end)
    


if __name__== '__main__':
    n=int(input())
    ele=[int(input()) for i in range(n)]
    end=len(ele)
    quicksort(ele,0,end-1)
    print(ele)
