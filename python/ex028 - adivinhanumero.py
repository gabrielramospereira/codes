import random
from time import sleep
print("Vou pensar em número entre 0 e 5. Tente adivinhar ")
lista = [1,2,3,4,5]
num = random.choice(lista)
meu = int(input("Tente adivinhar:"))
print("PROCESSANDO..")
sleep(3)
if meu == num:
    print("Parabéns, você acertou! Você pensou no número {} e eu no número {}".format(meu,num))
else:
    print("Que pena, você errou. Você pensou no número {} e eu no número {}".format(meu,num))


#from random import randint
#computador=randint{0,5}