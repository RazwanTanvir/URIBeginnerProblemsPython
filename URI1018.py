N = int(input())
li = [100,50,20,10,5,2,1]
print N
for item in li:
    a = N/item
    print str(a)+' nota(s) de R$ '+str(item)+',00'
    N = N - (a*item)

    
