using System;

class Jogador{  
   public int energia; 
   public bool vivo;
   public string nome;
   public int pelota;
   public Jogador(string n){
        energia=100;
        vivo=true;
        nome=n;
        pelota=0;
    }   
    public void golear(){
        pelota+=1;
        Console.WriteLine("Número de gols do atacante {0}: {1}",pelota, nome);
    }
}

class Aula29{
    static void Main(){
        string nome1;
        Console.WriteLine("Digite o nome do Jogador1: ");
        nome1=Console.ReadLine();
        Jogador j1 = new Jogador(nome1);
        j1.golear();
        j1.golear();
        j1.golear();
       

    }
}
