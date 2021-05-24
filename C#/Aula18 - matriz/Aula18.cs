using System;

class matriz{

    static void Main(){

        int [,] n = new int [3,5];

        n[0,0]=1;
        n[0,1]=2;
        n[0,2]=3;
        n[0,3]=4;
        n[0,4]=5;

        n[1,0]=6;
        n[1,1]=7;
        n[1,2]=8;
        n[1,3]=9;
        n[1,4]=10; 

        n[2,0]=11;
        n[2,1]=12;
        n[2,2]=13;
        n[2,3]=14;
        n[2,4]=15;

        Console.WriteLine(n[0,2]);


    }
}