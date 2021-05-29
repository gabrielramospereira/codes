ano = int(input('Informe seu ano de nascimento: '))
from datetime import date
atual = date.today().year
idade = atual - ano
if idade <=9:
    print('Você tem {} anos e está na categoria MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos e está na categoria INFANTIL.'.format(idade))
elif idade >14 and idade <= 19:
    print('Você tem {} anos e está na categoria JUNIOR.'.format(idade))
elif idade > 19 and idade <= 25:
    print('Você tem {} anos e está na categoria MASTER.'.format(idade))
else:
    print('Você tem {} anos e está na categoria SENIOR.'.format(idade))