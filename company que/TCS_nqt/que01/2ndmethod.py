count=1
t1=0
t2=0
t3=0
while(count<=9):
    x=int(input())
    if x >= 1 and x <= 100:
        if count%3==1:
            t1+=x
        elif count%3==2:
            t2+=x
        else:
            t3+=x
    count+=1
result=[]
result.append(t1/3)
result.append(t2/3)
result.append(t3/3)
mm=max(result)
if mm < 70:
    print("All are unfit")
else:
    for i in range(len(result)):
        if mm == result[i]:
            print("trainee number:"),
            print(i+1)
            
        
    
