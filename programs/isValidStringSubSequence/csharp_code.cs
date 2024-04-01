using System;

namespace MyCompiler
{
    class Program
    {
        public static void Main(string[] args)
        {
            String str1 = "gksr%ek@@@";
            String str2 = "geeksforge%eks@@@";
            bool isValid = isValidSubSequence(str1, str2);
            Console.WriteLine("Valid SubSequence " + isValid);
        }
        public static bool isValidSubSequence(String s1, String s2)
        {
            int m = s1.Length;
            int n = s2.Length;

            int j = 0;
            for (int i = 0; i < n && j < m; i++)
            {
                if (s1[j] == s2[i])
                    j++;
            }

            return j == m;
        }
    }
}