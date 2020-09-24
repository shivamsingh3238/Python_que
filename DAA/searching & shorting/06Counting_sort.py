def countsort(ele):
    output=[0]*len(ele)
    #array size max+1
    max_val=max(ele)+1
    dummy=[0]*max_val
    for i in ele:
        dummy[i]=dummy[i]+1
    #add consecutive numbers
    for i in range(1,len(dummy)):
        dummy[i]=dummy[i]+dummy[i-1]
    #put all the ele on right place
    for i in ele:
        output[dummy[i]-1]=i
        dummy[i]=dummy[i]-1
    return output
    
        
    





if __name__ == '__main__':
    n=int(input())
    ele=[int(input()) for i in range(0,n)]
    sort_ele=countsort(ele)
    print(sort_ele)
