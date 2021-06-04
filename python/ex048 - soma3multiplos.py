num = 0
qtd = 0
for c in range (1,501,2):
    if (c % 3 == 0):
        num += c
        qtd += 1
print ('A soma vale: {} dos {} números'.format(num, qtd))
