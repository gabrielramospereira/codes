cont = 0
num = int(input('Digite um número: '))
for c in range (1,num+1,1):
    if (num % c == 0):
        cont+=1

if cont>2:
    print('O número apresenta {} divisores e por isso não é primo'.format(cont))
else:
    print('O número apresenta {} divisores e por isso é primo'.format(cont))