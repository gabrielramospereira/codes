soma = 0
velho =''
idadevelha = 0
cont = 0
for c in range (0,4,1):
    print('==== {} pessoa ==='.format(c+1))
    nome = str(input('Informe o nome: '))
    idade = int(input('Informe a idade: '))
    sexo = str(input('Informe o sexo: [M/F]'))
    soma += idade
    if c == 0 and sexo in 'Mm':
        velho = nome
        idadevelha = idade
    if sexo in 'Mm' and idade > idadevelha:
        velho = nome
        idadevelha = idade
    if sexo in 'Ff' and idade <18:
        cont+=1

media = soma/4
print('A media de idade do grupo é: {}'.format(media))
print('O homem mais velho é o {} e ele tem {} anos.'.format(velho, idadevelha))
print('O número de mulheres abaixo de 18 anos é: {}'.format(cont))