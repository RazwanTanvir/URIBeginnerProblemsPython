x = int(input())
if x%2==0:
    for i in range(1,7):
        print x+(2*i-1)
else :
    for i in range(1,7):
        print x
        x = x+2
        
