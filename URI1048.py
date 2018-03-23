S = float(input())
if S>=0 and S<=400:
    bonus = S*(0.15)
    print 'Novo salario:',"%.2f"% (S+bonus)
    print 'Reajuste ganho:', "%.2f"%bonus
    print 'Em percentual: 15 %'
if S>=400.01 and S<=800:
    bonus = S*(0.12)
    print 'Novo salario:',"%.2f"% (S+bonus)
    print 'Reajuste ganho:',"%.2f"% bonus
    print 'Em percentual: 12 %'
if S>=800.01 and S<=1200:
    bonus = S*(0.1)
    print 'Novo salario:',"%.2f"% (S+bonus)
    print 'Reajuste ganho:',"%.2f"% bonus
    print 'Em percentual: 10 %'
if S>=1200.01 and S<=2000:
    bonus = S*(0.07)
    print 'Novo salario:',"%.2f"% (S+bonus)
    print 'Reajuste ganho:',"%.2f"% bonus
    print 'Em percentual: 7 %'
if S>2000:
    bonus = S*(0.04)
    print 'Novo salario:',"%.2f"% (S+bonus)
    print 'Reajuste ganho:',"%.2f"% bonus
    print 'Em percentual: 4 %'
