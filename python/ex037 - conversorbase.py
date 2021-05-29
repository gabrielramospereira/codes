num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases da conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Digite sua escolha: '))

if escolha == 1:
    print('{} convertido para BINÁRIO é igual a: {}'.format(num,bin(num)))
elif escolha == 2:
     print('{} convertido para OCTAL é igual a: {}'.format(num, oct(num)))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a: {}'.format(num, hex(num)))
else:
    print('Escolha inválida.')