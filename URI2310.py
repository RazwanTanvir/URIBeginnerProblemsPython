n = int(input())
ser=0
s=0
block=0
bl=0
attack=0
atc=0
for i in range(n):
    name = raw_input()
    #in [20]: a,b,c,d,e,f = raw_input().split()
    a,b,c =raw_input().split(" ")
    d,e,f = raw_input().split(" ")


    
    a = float(a)
    b = float(b)
    c =  float(c)
    d =  float(d)
    e =  float(e)
    f =  float(f)
    ser+=a
    s+=d
    block+=b
    bl+=e
    attack+=c
    atc+=f
ser = (s/ser)*100
blc = (bl/block)*100
at = (atc/attack)*100
print 'Pontos de Saque:',"%.2f"%ser,'%.'
print 'Pontos de Bloqueio:',"%.2f"%blc,'%.'
print 'Pontos de Ataque:',"%.2f"%at,'%.'

    
