using System;

class se{

    static void Main(){
        int nota=0;
        string resultado = "Reprovado";
        Console.Write("Diga a nota do aluno: ");
        nota = int.Parse(Console.ReadLine());
        if (nota >=6){
            resultado = "Aprovado";

        } 

    Console.WriteLine("O candidato está {0}",resultado);
    }
}
