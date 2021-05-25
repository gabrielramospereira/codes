n1 = float(input("Informe primeiro segmento: "))
n2 = float(input("Informe segundo segmento: "))
n3 = float(input("Informe terceiro segmento: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("\033[4;30;43mOs segmentos podem formar triângulo.\033[m")
else:
    print("\033[1;31;42mOs segmentos não podem formar triângulo.")


