deltas = float(input("Qual a distância da sua viagem?"))
if deltas <= 200:
    print("O valor da viagem é R${}".format(deltas*0.5))
else:
    print("O valor da viagem é R${}".format(deltas*0.45))
    