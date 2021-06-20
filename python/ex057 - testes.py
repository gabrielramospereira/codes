sexo = str(input("Informe seu sexo: [M/F]")).upper()
while sexo not in "MF":
    sexo = str(input("Dados inválidos. Informe seu sexo: [M/F]")).upper()
print("Sexo {}".format(sexo))
