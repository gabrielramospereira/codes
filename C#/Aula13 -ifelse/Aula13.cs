using System;

class senao{

    static void Main(){

        int nota=0;
        string resultado = "Reprovado";
        Console.Write("Diga a nota do aluno: ");
        nota = int.Parse(Console.ReadLine());
        if (nota < 4){
            resultado = "Reprovado";

        } else if(nota <7 ){
            resultado = "Recuperação";
        } else{
            resultado = "Aprovado";
        }
        Console.WriteLine("O candidato está {0}",resultado);

    }
}