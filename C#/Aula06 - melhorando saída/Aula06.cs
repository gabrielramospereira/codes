using System;
class formatando{
    static void Main(){
        int n1=10,n2=20,n3=30;
        Console.WriteLine("n1={0},\nn2={1} e\nn3={2}",n1,n2,n3);

        double valorvenda= 5;
        double lucro = 0.1;
        Console.Write("Lucro: {0,1:p} \n",lucro);
        Console.Write("Valor venda: {0,1:c} ",valorvenda);

    }
}
