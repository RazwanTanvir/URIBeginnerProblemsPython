test = int(input())
for i in range(test):
    a,b,c = raw_input().split(" ")
    a = float(a)
    b = float(b)
    c = float(c)
    avg = (a*2+b*3+c*5)/10
    print "%.1f"%avg
