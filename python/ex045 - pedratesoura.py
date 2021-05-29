from random import randint
itens = ('Pedra','Papel','Tesoura')
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura ''')
computador = randint(0,2)
jogada=int(input('Informe sua jogada: '))
print('O computador escolheu {}'.format(itens[computador]))
print('Você escolheu {}'.format(itens[jogada]))

if computador == 0:   #computador jogou pedra
    if jogada == 0:
        print('Empate!')
    elif jogada ==1:
        print('Você venceu o computador.')
    elif jogada ==2:
        print('Você perdeu para o computador.')
elif computador == 1:  #computador jogou papel
     if jogada == 1:
        print('Empate!')
     elif jogada ==2:
        print('Você venceu o computador.')
     elif jogada ==0:
        print('Você perdeu para o computador.')
elif computador == 2:  #computador jogou tesoura
     if jogada == 2:
        print('Empate!')
     elif jogada ==0:
        print('Você venceu o computador.')
     elif jogada ==1:
        print('Você perdeu para o computador.')
