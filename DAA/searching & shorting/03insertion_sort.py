def selection(ele):
    for i in range(len(ele)):
        key=ele[i]
        j=i-1
        while(j>=0 and key<ele[j]):
            ele[j+1]=ele[j]
            j=j-1
            ele[j+1]=key



    
n=int(input())
ele=[int(input()) for i in range(n)]
selection(ele)
print(ele)
     
