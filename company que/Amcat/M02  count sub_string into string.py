#find no of sub_string present into  string
def find(string , sub_s):
    m=len(string)
    n=len(sub_s)
    count=0
    for i in range(m-n+1):
        j=0
        while(j<n):
            if string[i+j] != sub_s[j]:
                break
            j+=1

        if j==n:
            count+=1
    return count
#--------------------------------- same using method-------------------
##def find(s , sub_s):
##    return s.count(sub_s)



if __name__ ==  '__main__':
    string=input()
    sub_s=input()
    no=find(string , sub_s)
    print(no)
