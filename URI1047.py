H,M,h,m = raw_input().split(" ")
H = int(H)
M = int(M)
h = int (h)
m = int (m)
Hdiff = h-H
Mdiff = m-M
if h < H and m<M:
    mins =60-(M-m)
    hrs =24-H-h-1	
    print 'O JOGO DUROU',hrs, 'HORA(S) E',mins ,'MINUTO(S)'
elif h>H and m<M:
    mins =60-(M-m)
    hrs = h-H-1
    print 'O JOGO DUROU',hrs, 'HORA(S) E',mins ,'MINUTO(S)'

elif h < H and m>M:
    mins = m-M
    hrs = H+h+(24%H)
    print 'O JOGO DUROU',hrs, 'HORA(S) E',mins ,'MINUTO(S)'

elif h>H and m>M:
    mins =m-M
    hrs = h-H
    print 'O JOGO DUROU',hrs, 'HORA(S) E',mins ,'MINUTO(S)'
elif h==H and m==M:
    print 'O JOGO DUROU',24, 'HORA(S) E',0 ,'MINUTO(S)'
elif h==H and m>M:
    mins = m-M
    hrs = 0
    print 'O JOGO DUROU',hrs, 'HORA(S) E',mins ,'MINUTO(S)'
elif h==H and m<M:
    
   
    
    
