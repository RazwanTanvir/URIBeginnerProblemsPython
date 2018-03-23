N = float(input())
N+= 0.001
li=[100.00,50.00,20.00,10.00,5.00,2.00]
li2=[1.00,0.50,0.25,0.10,0.05,0.01]
print 'NOTAS:'
for item in li:
        r =int( N/item)
        N = float(N - item*r)
        print int(r),'nota(s) de R$',"%.2f" % item     
print 'MOEDAS:'
for item in li2:
        r = int(N/item)
        N = float(N - item*r)
        print int(r),'moeda(s) de R$',"%.2f" % item
        


