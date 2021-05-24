using System;

class foror{

    static void Main(){
        int cont;
        int [] num = new int [10];
        for(cont=0;cont<10;cont++){
            Console.WriteLine("G10 na jogada {0}",cont);
            num[cont]=0;
        }
         for(cont=0;cont<num.Length;cont++){
             Console.WriteLine("Valor de num na posição {0}: {1}",cont,num[cont]);
         }
    }
}