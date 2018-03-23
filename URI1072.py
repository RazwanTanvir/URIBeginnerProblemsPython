test = int(input())
inin = 0
out = 0
for i in range(test):
    num = int(input())
    if num>=10 and num<=20:
        inin = inin+1
    else:
        out = out+1
print inin,'in'
print out,'out'
