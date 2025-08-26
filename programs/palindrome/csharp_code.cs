using System;

class Program
{
    static bool IsPalindrome(string str)
    {
        
        // C#: .ToCharArray() converts string to character array
        char[] charArray = str.ToCharArray();
        
        // C#: Array.Reverse() reverses the character array in-place
        Array.Reverse(charArray);
        
        // C#: new string(char[]) constructor creates string from char array
        string reversed = new string(charArray);
        
        
        // C#: .Equals() method for string comparison
        return str.Equals(reversed);
    }

    static void Main(string[] args)
    {
        string str = "radar";
        if (IsPalindrome(str))
            Console.WriteLine(str + " is a palindrome.");
        else
            Console.WriteLine(str + " is not a palindrome.");
    }
}
