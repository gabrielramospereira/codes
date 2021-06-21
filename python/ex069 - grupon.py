maior = h = m = 0
while True:
    print("====== CADASTRE UMA PESSOA =======")
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper().split()[0]
    choice = str(input("Quer continuar? [S/N]: ")).upper().split()[0]
    if idade <18:
        maior += 1
    if sexo == 'M':
        h+=1
    else:
        m+=1
    if choice == 'N':
        break

print(f"Temos {maior} menores de idade. Temos {h} homens e {m} mulheres")