from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade < 18:
    print("Ainda faltam {} anos para você se alistar. você deve se alistar em {}".format(18-idade, atual+(18-idade)))
elif idade >18:
    print('Seu alistamento foi há {} anos atrás em {}'.format(idade-18, atual-(idade-18)))
else:
    print('Você deve se alistar imediatamente!!')