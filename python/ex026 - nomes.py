nome = str(input("Informe seu nome completo: "))
lista=nome.strip().split()
print("Seu primeiro nome é: {}".format(lista[0]))
print("Seu último nome é: {}".format(lista[len(lista)-1]))


