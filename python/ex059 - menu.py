choice = -1
n1 = int(input("Entre com o primeiro valor: "))
n2 = int(input("Entre com o segundo valor: "))

while choice !=5:
   
    choice=int(input("Tecle [1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair do programa"))
    if choice == 1:
        print("A soma de {} e {} vale {}" .format(n1,n2,n1+n2))
    elif choice == 2:
        print("A multiplicação de {} e {} vale {}" . format(n1,n2,n1*n2))
    elif choice ==3:
        if n1<=n2:
            maior=n2
        else:
            maior=n1
        print("Entre {} e {} o maior número vale {}" .format(n1,n2,maior))
    elif choice ==4:
        n1 = int(input("Entre com o primeiro valor: "))
        n2 = int(input("Entre com o segundo valor: "))
    elif choice==5:
        print('FIM')
    else:
        print("Escolha inválida.")

        
            
          

