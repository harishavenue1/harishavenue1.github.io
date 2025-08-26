using System;

namespace MyCompiler
{
    class Program
    {
        public static void Main(string[] args)
        {
            int num = 2;
            int[] output = countBits(num);
            Console.WriteLine("For Num = " + num + ", bits are " + String.Join(",", output));

            num = 5;
            output = countBits(num);
            Console.WriteLine("For Num = " + num + ", bits are " + String.Join(",", output));
        }
        public static int[] countBits(int n)
        {
            
            // C#: Array initialization with specified size
            int[] arr = new int[n + 1];
            
            // C#: for-loop with <= for inclusive range
            for (int i = 0; i <= n; i++)
            {
                
                // C#: Bit manipulation - count bits using DP
                // arr[i >> 1] gets count for i/2, (i & 1) adds 1 if i is odd
                arr[i] = arr[i >> 1] + (i & 1);
            }
            
            return arr;
        }
    }
}