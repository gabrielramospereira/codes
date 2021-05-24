import random
#from random import choice
n1=input("Informe o Primeiro aluno: ")
n2=input("Informe o Segundo aluno: ")
n3=input("Informe o Terceiro aluno: ")
n4=input("Informe o Quarto aluno: ")
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)   #choice(lista)
print("O aluno escolhido foi o: {}".format(escolhido))
