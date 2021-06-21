print("======Gerador de PA=======")
first = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))
cont = 0
sum = first
termos = 10
total=0
while termos != 0:
    print("{} -> ".format(sum), end="")
    cont+=1
    sum+=razao
    if cont == termos:
        print("PAUSA")
        termos = int(input("Quantos termos você quer mostrar a mais? "))
        total = total + cont
        cont=0
print("Numero total de termos {}" .format(total))
