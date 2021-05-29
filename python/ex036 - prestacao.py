valor = int(input("Qual o valor da casa?"))
salary = int(input('Qual o salário do comprador?'))
year = int(input('Quantos anos pretende pagar?'))
prestacao = valor/(year*12)

if prestacao >= 0.3*salary:
    print('Empréstimo negado')
else:
    print('Empréstimo concedido no valor de {:.2f} cada parcela'.format(prestacao))


