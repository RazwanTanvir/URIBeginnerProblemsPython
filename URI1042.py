a,b,c = raw_input().split(" ")
'''a = int(a)
b = int (b)
c = int (c)'''
li = [a,b,c]
res = sorted(li,key=int)

print '\n'.join(res)+'\n'
print'\n'.join(li)
