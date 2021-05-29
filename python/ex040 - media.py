n1 = float(input('Informe primeira nota: '))
n2 = float(input('Informe segunda nota: '))
media =(n1+n2)/2

if media < 5:
    print('Aluno reprovado!')
elif media >=5 and media < 7:
    print('Aluno está recuperação!')
else:
    print('Aluno aprovado!!!')