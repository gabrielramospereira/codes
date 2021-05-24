using System;

public class Jogador{  // é pública, pois declarou nada.
   public int energia=100;  // é pública, pois declarou nada.
  public bool vivo=true;   // é pública, pois declarou nada.

// essa classe tem duas propriedades so far.
}

class Aula28{
    static void Main(){
        Jogador j1 = new Jogador();
        Jogador j2 = new Jogador();
        Jogador j3 = new Jogador();
        j1.energia = 50;
        Console.WriteLine("Energia do jogador 1: {0}",j1.energia);
        Console.WriteLine("Energia do jogador 2: {0}",j2.energia);

    }
}