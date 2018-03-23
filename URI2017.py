li=[]
b = int(input())
result = 151
for i in range(b):
    a = raw_input()    
    if a not in li:
        result = result -1
        li.append(a)
print 'Falta(m)', result, 'pomekon(s).'
