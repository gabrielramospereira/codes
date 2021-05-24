using System;

class metodos{

    static void Main(){
        g10();
        soma(10,5);

    }
    static void g10(){
        Console.WriteLine("G10 na jogada");
    }

    static void soma(int n1,int n2){
        Console.WriteLine("A soma de {0} e {1} é {2}",n1,n2,n1+n2);
    }
}