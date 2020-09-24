#collection module
import collections
l=list(map(str,input().split()))
c=collections.Counter(l)
print(c)
#print(dir(c))
reverse_dic={j:i for (i,j) in c.items()}
print(reverse_dic)

    
