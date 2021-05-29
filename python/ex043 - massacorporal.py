massa = float(input('Qual é o seu peso em kg?'))
altura = float(input('Qual é sua altura em m?'))
imc = massa / (altura ** 2)


if imc <= 18.5:
    print('Você está abaixo do peso!')
elif imc > 18.5 and imc <= 25:
    print('Peso ideal!')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif 30 < imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mordbida')

# python aceita a expressão matematica 1 <= x < 5