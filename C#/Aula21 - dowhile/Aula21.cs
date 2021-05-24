using System;

class repeticao{
    static void Main(){
        string senha = "123";
        string teste;
       int cont=0;
        do{
            Console.Clear();
            Console.WriteLine("Informe a senha: ");
             teste = Console.ReadLine();
             cont++;
        }while(senha!= teste);

        Console.WriteLine("Senha correta, tentativas: {0}",cont);

        
    }
}