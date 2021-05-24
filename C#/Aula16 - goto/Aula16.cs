using System;

class vaiaonde{

    static void Main(){

        int tempo = 0;
        char escolha = ' ';
        
        inicio:
        Console.Clear();

        Console.WriteLine("Escolha o transporte: [a] para avião, [c] para carro, [o] para ônibus");
        escolha = char.Parse(Console.ReadLine());

        switch(escolha){
            case 'a':
                tempo=50;
                break;
            case 'c':
                tempo=400;
                break;
            case 'o':
                tempo=660;
                break;
            default:
                tempo=-1;
                break;
        }
        if (tempo<0){
            Console.WriteLine("Modo de transporte indisponível");

        } else{
            Console.WriteLine("O tempo de viagem é: {0}",tempo);
    }
    Console.WriteLine("Calcular outro transporte? [s] para sim [n] para não");
    escolha = char.Parse(Console.ReadLine());
    if(escolha=='s'|| escolha=='S'){
        goto inicio;
    } else{
        Console.Clear();
        Console.WriteLine("Fim do Programa");
    }
}
}

