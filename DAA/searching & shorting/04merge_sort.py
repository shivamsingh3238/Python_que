def merge(ele):
    if len(ele) >1:
        r=len(ele)//2
        l=ele[:r]
        m=ele[r:]

        merge(l)
        merge(m)

        i=j=k=0
        while(i<len(l) and j<len(m)):
            if l[i]<m[j]:
                ele[k]=l[i]
                i+=1
            else:
                ele[k]=m[j]
                j+=1
            k+=1

        while(i<len(l)):
              ele[k]=l[i]
              i+=1
              k+=1
        
        while(j<len(m)):
              ele[k]=m[j]
              j+=1
              k+=1

if __name__ == '__main__':
    n=int(input())
    ele=[int(input()) for i in range(n)]
    merge(ele)
    print(ele)
