from random import randint

while True:
    n = int(input("Digite um valor: "))
    guess = str(input("Par ou Ímpar [P/I]: ")).upper().split()[0]
    computador = randint(0,10)
    if (n+computador) % 2 == 0:
        res= 'Par'
    else:
        res = 'Impar'
    print(f'Você jogou {n} e o computador {computador}, a soma deu: {n+computador} deu {res}')
    if guess in res:
        print("VOCE VENCEU, VAMOS JOGAR AGAIN")
    else:
        print("SUCH A LOSER")