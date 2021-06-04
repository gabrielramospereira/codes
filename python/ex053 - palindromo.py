frase = input('Digite uma palavra: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
print ('Você digitou a frase: {}'.format(junto))
inverso = junto[::-1]
'''inverso = ''
for c in range(len(junto)-1,-1,-1):
    inverso += junto[c]'''
print(inverso)


