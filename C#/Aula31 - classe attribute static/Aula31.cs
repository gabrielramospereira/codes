using System;
 static public class Jogador{
    static int energia;
    static bool vivo;
    static string nome;

    static public void iniciar(string n){
        energia=100;
        vivo=true;
        nome=n;
    }
   
    static public void info(){
        Console.WriteLine("############################################");
        Console.WriteLine("Nome Jogador: {0}", nome);
        Console.WriteLine("Energia Jogador: {0}", energia);
        Console.WriteLine("Status Jogador: {0}", vivo);
    }
}

public class Inimigo{
   static public bool alerta;
   public string nome;

    public Inimigo(string n){
        static alerta=false;
        nome=n;
    }
    public void info(){
        Console.WriteLine("############################################");
        Console.WriteLine("Nome Inimigo: {0}. Em alerta: {1}", nome,alerta);
    }
}
class Aula31{
    static void Main(){

        Jogador.iniciar("Bruno");
        Jogador.info();

        Inimigo i1 = new Inimigo("Globin");
        Inimigo i2 = new Inimigo("Elfo");
        Inimigo i3 = new Inimigo("Pirata");
        Inimigo.alerta=true;
        i1.info();
        i2.info();
        i3.info();

    }
}