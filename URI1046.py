a,b = raw_input().split(" ")
a = int(a)
b = int(b)
if a < b:
    print 'O JOGO DUROU',b-a,'HORA(S)'
elif a > b:
    print 'O JOGO DUROU', 24%(a-b),'HORA(S)'
else:
    print 'O JOGO DUROU', 24,'HORA(S)'
