using System;

class seaninhado{

    static void Main(){
        int nota=0;
        string resultado = "Reprovado";
        Console.Write("Diga a nota do aluno: ");
        nota = int.Parse(Console.ReadLine());
        if (nota >= 7){
            if(nota>=9){
                resultado = "Aprovado com louvor";
            }else{
                resultado ="Aprovado";
            }
        } else{
            if (nota>=4){
                resultado="Recuperação";
            }else{
            resultado = "Reprovado";
            }
        }
        Console.WriteLine("O candidato está {0}",resultado);

    }
}