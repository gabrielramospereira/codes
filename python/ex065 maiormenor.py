num=0
choice = " "
maior= menor = sum = cont = 0

while choice not in "nN":
    num = int(input("Digite um número: "))
    cont+=1
    if cont == 1:
        maior = num
        menor = num
        sum = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        sum = sum + num
    choice = str(input("Quer continuar [S/N]: ")).upper().strip()[0]

print("O maior valor da sequência {}, o menor {} e a média {}" . format(maior,menor,sum/cont))

