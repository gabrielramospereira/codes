sum=  -999
n = 0
cont=-1
while n != 999:
    n = int(input("Digite um número [999 para parar]: ")) 
    sum+= n
    cont+=1
    
print("Você digitou {} números e a soma deles foi {}" .format(cont, sum))
