counter = 0
sums = 0
for i in range(6):
    a = float(input())
    if a>0:
        counter = counter+1
        sums += a
print counter,'valores positivos'
print "%.1f"%(sums/counter)
