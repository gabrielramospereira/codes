using System;
class escopo{
    static int num=10;
    static void Main(){
       Console.WriteLine(num);

    }
    void teste(){
        
        Console.WriteLine(num);
    }
}