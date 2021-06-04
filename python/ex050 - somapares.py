soma= 0
for c in range(0,6):
    n = int(input('Entre com um número: '))
    if (n % 2 == 0):
        soma += n
print('A soma dos valores pares vale: {}'.format(soma))
