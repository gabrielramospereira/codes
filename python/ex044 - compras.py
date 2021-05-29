print ('############ Lojas G10 ###########')
preço = float(input('Informe o preço das compras:'))
print(''' FORMAS DE PAGAMENTO 
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
escolha = int(input('Qual a sua forma de pagamento?'))

if escolha == 1:
    print('O preço original é {} aplicado o desconto o preço será {}'.format(preço,preço-(preço*0.1)))
elif escolha == 2:
     print('O preço original é {} aplicado o desconto o preço será {}'.format(preço,preço-(preço*0.05)))
elif escolha == 3:
    print('O preço será {}'.format(preço))
elif escolha ==4:
    print('O preço original é {} aplicado os juros o preço será {}'.format(preço,preço+(preço*0.2)))
else:
    print('Inválido')
