dict={}
ls=list(map(str,input().split()))
for i in range(len(ls)):
    dict[ls[i]] = input('enter the value')
print(dict)
print('remove one item')
del dict[ls[0]]
print(dict)
dict.clear()
print('after clearing dictionary')
print(dict)
