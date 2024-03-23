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
            int[] arr = new int[n + 1];
            for (int i = 0; i <= n; i++)
            {
                arr[i] = arr[i >> 1] + (i & 1);
            }
            return arr;
        }
    }
}