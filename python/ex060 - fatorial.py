n= int(input("Digite um número para calcular o seu fatorial: "))
mul = 1
while n!= 0:
    print("{}".format(n), end="")
    if(n==1):
        print(" = ", end="")
    else:
        print(" x ", end="")
    mul = mul * n
    n = n -1
print("{}" .format(mul))