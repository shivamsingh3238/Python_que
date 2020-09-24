def cal(n):
    count=0
    queue=[]
    for i in n:
        min=0
        max=0
        queue.append(i)
        queue.sort()
        if queue.index(i)==0 or queue.index(i)==(len(queue)-1):
            count+=1
        else:
            min=queue.index(i)+1
            max=len(queue)-(min-1)
            if min < max:
                count+= ((min-1)*2)+1
            else:
                count+= ((max-1)*2)+1
    return count
            
        
        


n=list(map(int,input().split()))
step=cal(n)
print(step)
