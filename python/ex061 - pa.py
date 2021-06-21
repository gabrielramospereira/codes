print("======Gerador de PA=======")
first = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão"))
cont = 1
sum = first
while cont <= 10:
    if cont == 10:
        print("{}".format(sum), end="")
    else:
        print("{} -> ".format(sum), end="")
    cont+=1
    sum+=razao
