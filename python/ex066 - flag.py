sum = cont = num = 0
while True:
    num = int(input("Digite um número (999 para parar): "))
    if num == 999:
        break
    cont+=1
    sum+=num
print(f"Foram lidos {cont} números e a soma foi {sum}")