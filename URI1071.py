a = int(input())
b = int(input())
sums=0
if a<b:
    a,b = b,a

for i in range(b+1,a):
    if i%2==1:
        sums = sums+i
print sums
        
