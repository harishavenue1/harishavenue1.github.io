using System;

class Fibonacci
{
    static void Main()
    {
        int n = 10; // Change the value of n for different number of Fibonacci numbers
        int a = 0, b = 1, sum = 0;
        Console.WriteLine("Fibonacci Series:");
        for (int i = 0; i < n; i++)
        {
            Console.Write(a + " ");
            sum = a + b;
            a = b;
            b = sum;
        }
    }
}
