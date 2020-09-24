import collections 
def minimumBox(arr, n):
    q = collections.deque([])
    arr.sort()
    q.append(arr[0])
    for i in range(1, n):
        now = q[0]
        if(arr[i] >= 2 * now):
            q.popleft()
        q.append(arr[i])
    return len(q)
    
  
n=int(input())
t=list(input().split(' '))
print(minimumBox(t, n)) 
