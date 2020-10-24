def cal(ele,n):
   
    result=[]
    temp=[]
    print(ele)
    for i in range(0,len(ele)):
        if i%3==0 and i!=0:
            result.append(temp)
            del temp
            temp=[]
            temp.append(ele[i])
        else:
            temp.append(ele[i])
    result.append(temp)
    avg=[]
    
    print(result)
    for i in range(0,len(result)):
        A=0
        for j in range(0,3):
            A+=result[j][i]
        avg.append(A/3)
    return avg

n=int(input())
ele=[int(input()) for i in range(n)]
mn=min(ele)
mx=max(ele)
if (mn > 1 and mx > 100):
    print("INVALIDE INPUT")
else:
    ans=cal(ele,n)
    m=max(ans)
    if m < 70:
        print("All trannier unfit")
    else:
        for i in range(len(ans)):
            if m == ans[i]:
                print("Trainee Number:"),
                print(i+1)
        
