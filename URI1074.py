test = int(input())
for i in range(test):
    a = int(input())
    if a==0:
        print 'NULL'
    elif a<0 and a%2==0:
        print 'EVEN NEGATIVE'
    elif a>0 and a%2==0:
        print 'EVEN POSITIVE'
    elif a<0 and a%2!=0:
        print 'ODD NEGATIVE'
    elif a>0 and a%2!=0:
        print 'ODD POSITIVE'
    
