from random import randint
computador = randint(0,10)
guess=int(input('Sou seu computador. Acabo de pensar em um número de 0 a 10. Tente adivinhá-lo: '))
c=1
while guess != computador:
    if guess < computador:
        guess=int(input('Mais.. tente mais uma vez: '))
    else:
        guess=int(input('Menos.. tente mais uma vez: '))
    c+=1
print('Parabéns! O número pensado era o {}. Você adivinhou em {} tentativas.' .format(computador,c))