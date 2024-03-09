using System;

class Fibonacci
{
    static void Main()
    {
        int n = 10; // Change the value of n for different number of Fibonacci numbers
        int a = 0, b = 1;
        Console.WriteLine("Fibonacci Series:");
        for (int i = 0; i < n; i++)
        {
            Console.Write(a + " ");
            int temp = a;
            a = b;
            b = temp + b;
        }
    }
}
