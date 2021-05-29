n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O número {} é maior que o número {}'.format(n1,n2))
elif n1 < n2:
    print('O número {} é menor que o número {}'.format(n1,n2))
else:
    print('O número {} é igual ao número {}'.format(n1,n2))