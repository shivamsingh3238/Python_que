#python collection
#orderedDict
import collections
dic=collections.OrderedDict()
for _ in range(0,2):
    key=input()
    dic[key]=input('value enter')
print(dic)
for i,j in dic.items():
    print(i,j)

