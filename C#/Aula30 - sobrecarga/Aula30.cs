using System;
class Jogador{
    protected int energia;
    protected bool vivo;
    protected string nome;

    public Jogador(){
        energia=100;
        vivo=true;
        nome="Jogador";
    }
    public Jogador(int e, string n){
        energia=e;
        vivo=true;
        nome=n;
    }
    public Jogador(string n, int e){
        energia=100;
        vivo=true;
        nome=n;
    }
    public Jogador(string n,int e, bool v){
        energia=e;
        vivo=v;
        nome=n;
    }
    ~ Jogador(){
        Console.Write("Jogador {0} foi destruido\n", nome);
    }
    public void info(){
        Console.WriteLine("############################################");
        Console.WriteLine("Nome Jogador: {0}", nome);
        Console.WriteLine("Energia Jogador: {0}", energia);
        Console.WriteLine("Status Jogador: {0}", vivo);
    }
}
class Aula30{
    static void Main(){

        Jogador j1 = new Jogador();
        Jogador j2 = new Jogador(70,"G10");
        Jogador j3 = new Jogador("Allanzinho",10);
        Jogador j4 = new Jogador("Allanzinho",10,false);

        j1.info();
        j2.info();
        j3.info();
        j4.info();

    }
}