s=raw_input()
count=0
for i in s:
    if not(i.isalpha() or i.isdigit()):
        count+=1
        print(i)
print(count)
        
