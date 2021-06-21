sum= 0
cont=1
barato = ''
print("====== LOJA SUPER BARATÃO =======")
while True:
    nome = str(input("Produto: "))
    valor = float(input("Preço: "))
    sum += valor
    if cont ==1:
        barato = nome
        baratissimo = valor
    else:
        if baratissimo > valor:
             barato = nome
             baratissimo = valor
    cont+=1
    choice = str(input("Quer continuar? [S/N]: ")).upper().split()[0]
    if choice == 'N':
        break


print(f"A soma foi {sum} e o mais barato foi {barato}")