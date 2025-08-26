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
            
            // C#: Get string lengths using .Length property
            int m = s1.Length;
            int n = s2.Length;

            
            // C#: Pointer for subsequence string
            int j = 0;
            
            // C#: for-loop with compound condition
            for (int i = 0; i < n && j < m; i++)
            {
                
                // C#: Direct character comparison using indexing
                if (s1[j] == s2[i])
                    j++;  // Move subsequence pointer forward
            }

            
            // C#: Check if all characters of subsequence were found
            return j == m;
        }
    }
}