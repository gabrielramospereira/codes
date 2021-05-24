from math import sqrt,pow,hypot
catoposto=float(input("Informe o comprimento do cateto oposto: "))
catadj=float(input("Informe o comprimento do cateto adjacente: "))
hipotenusa= sqrt(pow(catoposto,2)+pow(catadj,2))
print("A hipotenusa vale: {:.2f}" .format(hipotenusa))
print("A hipotenusa vale: {:.2f}" .format(hypot(catoposto,catadj)))