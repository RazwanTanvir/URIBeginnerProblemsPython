
N1,N2,N3,N4 =raw_input().split(" ")
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)


avg = (N1*2+N2*3+N3*4+N4*1)/10
print 'Media:',"%0.1f"% avg
if avg>=7:
    print 'Aluno aprovado.'
elif avg<5:
    print 'Aluno reprovado.'
elif avg>=5 and avg<=6.9:
    print 'Aluno em exame.'
    exam = float(input())
    print 'Nota do exame:',"%.1f"%exam
    avg = (avg+exam)/2
    if avg>=5:
        print 'Aluno aprovado.'
    elif avg<=4.9:
        print 'Aluno reprovado.'
    print 'Media final:',"%.1f"%avg
    
    
