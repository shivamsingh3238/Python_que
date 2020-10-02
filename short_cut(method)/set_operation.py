#use this method can make all possibel set

import itertools
import sys
m=int(input())
arr=set(list(map(int,input().split())))
com=itertools.combinations(arr,m)
#print(dir(com))
##min=-sys.maxsize
##for obj in com:
##    pair=itertools.combinations(obj,2)
##    for x,y in pair:
##        dif==abs(x-y)
##        
for x,y in com:
    print(x,end="")
    print(y,end="")
    print()
