a = float(input())
profit =0

if a>=0 and a<=2000:
    print 'Isento'
else:
    if a>=2000.01 and a<=3000:
        a = a - 2000
        profit =  ((8*a)/100)
        print 'R$',"%.2f"%profit
    elif a>=3000.01 and a<=4500:
        profit = 80
        a = a - 3000
        profit = profit+ ((18*a)/100)
        print 'R$',"%.2f"%profit
        
    elif a>4500:
        profit = 350
        a = a - 4500
        profit = profit+ ((28*a)/100)
        print 'R$',"%.2f"%profit
   
        
        
