using System;

class parametros{

    static void Main(){
        soma(10,20,30,4,4,5,4,5,6);

    }
    static void soma(params int[]vetor){
        int res=0;
        if(vetor.Length<1){
            Console.WriteLine("Não existem valores para serem somados");
        } else if(vetor.Length<2){
            Console.WriteLine("um valor passado: {0}",vetor[0]);
        } else{
            for(int i=0;i<vetor.Length;i++){
                res+=vetor[i];
            }
             Console.WriteLine("A soma dos valores é: {0} ",res);
        }
       
    }
}