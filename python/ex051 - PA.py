print('='*10 + '10 TERMOS DE UMA PA' + '='*10)
first = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))

for c in range(first,first+(10*razao),razao):
    print(first, end = ' ')
    first = first + razao