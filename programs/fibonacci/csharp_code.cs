using System;

class Fibonacci
{
    static void Main()
    {
        int n = 10; // Change the value of n for different number of Fibonacci numbers
        
        // Initialize first two Fibonacci numbers
        int a = 0, b = 1, sum = 0;
        
        // C#: Console.WriteLine() for output with newline
        Console.WriteLine("Fibonacci Series:");
        
        // C#: Standard for-loop
        for (int i = 0; i < n; i++)
        {
            
            // C#: Console.Write() for output without newline
            Console.Write(a + " ");
            
            // Calculate next Fibonacci number: F(n) = F(n-1) + F(n-2)
            sum = a + b;
            a = b;
            b = sum;
        }
    }
}
