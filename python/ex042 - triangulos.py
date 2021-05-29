l1 = float(input('Informe o primeiro lado: '))
l2 = float(input('Informe o segundo lado: '))
l3 = float(input('Informe o terceiro lado: '))

if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('Triangulo existe')
    if l1 == l2 == l3:
        print('triangulo equilatero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('triangulo isosceles')
    else:
        print('triangulo escaleno')
else:
    print('Não forma triangulo')
