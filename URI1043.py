a,b,c = raw_input().split(" ")
a = float(a)
b = float(b)
c = float(c)
li = [a,b,c]
res = sorted(li)
if res[0]+res[1] > res[2]:
    print 'Perimetro =',"%.1f" % sum(res)
else:
    print 'Area =', "%.1f" %(((li[0]+li[1])/2.0)*li[2])
    
