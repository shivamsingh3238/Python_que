#map implementation
import collections
dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

st= collections.ChainMap(dict1,dict2)
print(st)
a=(list(st.keys()))
print(a)
b=list(st.values())
print(b[1])
for i in b:
    print(i,end=' '*10)
