from datetime import date
atual = date.today().year
maior=0
menor=0

for cont in range(0,7,1):
    ano = int(input("Em que ano a {} pessoa nasceu?".format(cont+1)))
    dif = atual - ano
    if (dif >=18):
        maior +=1
    else:
        menor +=1

print('Tivemos {} maiores de idade e {} pessoas menores de idade'.format(maior,menor))