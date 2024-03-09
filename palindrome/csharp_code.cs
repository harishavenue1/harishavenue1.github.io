using System;

class Program
{
    static bool IsPalindrome(string str)
    {
        char[] charArray = str.ToCharArray();
        Array.Reverse(charArray);
        string reversed = new string(charArray);
        return str.Equals(reversed);
    }

    static void Main(string[] args)
    {
        string str = "radar";
        if (IsPalindrome(str))
        {
            Console.WriteLine(str + " is a palindrome.");
        }
        else
        {
            Console.WriteLine(str + " is not a palindrome.");
        }
    }
}
