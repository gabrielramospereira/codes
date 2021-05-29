velocidade = int(input("Qual a velocidade do seu carro?"))
if velocidade <= 80:
    print("Dirija com segurança, bom dia!")
else:
    multa = 7*(velocidade-80)
    print("Você foi multado no valor de R${} reais".format(multa))
