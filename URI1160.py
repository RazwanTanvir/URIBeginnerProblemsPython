Test = int(input())
for i in range(Test):
    
    PA,PB,G1,G2 = raw_input().split(" ")
    PA = int(PA)
    PB = int(PB)
    G1 = float(G1)
    G2 = float(G2)
    Pdiff = PB - PA
    Gdiff = G1 - G2
    growth = (PA/100)*Gdiff
    result = int((Pdiff+1)/growth)
    print result

