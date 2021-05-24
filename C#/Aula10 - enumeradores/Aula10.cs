using System;

class enumeradores{
    enum DiasSemana{Domingo,Segunda,Terça,Quarta,Quinta,Sexta,Sábado};
    static void Main(){
        DiasSemana ds = DiasSemana.Segunda;
        Console.WriteLine(ds);

        DiasSemana ds2 = (DiasSemana)0;
        Console.WriteLine(ds2);

        int ds3 = (int)DiasSemana.Sexta;
         Console.WriteLine(ds3);
    }
}