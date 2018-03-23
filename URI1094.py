test = int(input())
C=0
R=0
S=0
for i in range(test):
    a,b = raw_input().split(" ")
    a = float (a)
    b = str(b)
    if b =='C':
        C = C+a
    if b =='R':
        R = R+a
    if b =='S':
        S = S+a
T=C+R+S

print 'Total:',int(T),'cobaias'
print 'Total de coelhos:' ,int(C)
print 'Total de ratos:', int(R)
print 'Total de sapos:',int(S)
print 'Percentual de coelhos:',"%.2f"%((C/T)*100), '%'
print 'Percentual de ratos:',"%.2f"%((R/T)*100),'%'
print 'Percentual de sapos:',"%.2f"% ((S/T)*100),'%'
        
    
        
