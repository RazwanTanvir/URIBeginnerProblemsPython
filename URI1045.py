a,b,c = raw_input().split(" ")
a = float(a)
b = float(b)
c = float(c)
li= [a,b,c]
li = sorted(li,reverse=True)
if li[0]>=li[1]+li[2]:
    print 'NAO FORMA TRIANGULO'
else:
    if li[0]*li[0] == li[1]*li[1] + li[2]*li[2]:
        print 'TRIANGULO RETANGULO'
    if li[0]*li[0] > li[1]*li[1] + li[2]*li[2]:
        print 'TRIANGULO OBTUSANGULO'
    if li[0]*li[0] < li[1]*li[1] + li[2]*li[2]:
        print 'TRIANGULO ACUTANGULO'
    if li[0]==li[1] and li[1]==li[2]:
        print'TRIANGULO EQUILATERO'
    if (li[0]==li[1] and li[1]!=li[2]) or (li[2]==li[1] and li[0]!=li[2])or (li[0]==li[2] and li[1]!=li[0]):
        print 'TRIANGULO ISOSCELES'
