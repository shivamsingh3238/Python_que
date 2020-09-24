def binary(arr ,start , end ,n):
    if end>= start:
        mid= (start+end)//2
        #base case 

        if arr[mid]==n:
            return mid
        elif arr[mid]>n:
            return binary(arr , start ,mid-1 ,n)
        else:
            return binary(arr ,mid+1 , end ,n)
    else:
        return -1
    





n=int(input())
arr= list(map(int,input().split()))
arr=sorted(arr)
res=binary(arr, 0, len(arr)-1 ,n)
if res!=-1:
    print(' possition is' ,res)
else:
    print('not present')

