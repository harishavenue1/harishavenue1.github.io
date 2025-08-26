using System;
using System.Linq;
using System.Text;

public class Program {
    public static void Main() {
        string str = "tomorrow";
        Console.WriteLine($"Replaced String {ReplacedString1(str)}");
        Console.WriteLine($"Replaced String {ReplacedString2(str)}");
        Console.WriteLine($"Replaced String {ReplacedString3(str)}");
    }
    
    public static string ReplacedString1(string str) {
        
        // C#: LINQ .Select() transforms each character, new string() from char array
        return new string(str.Select(c => c == 'o' ? '&' : c).ToArray());
    }
    
    public static string ReplacedString2(string str) {
        int count = 1;
        
        // C#: StringBuilder for efficient string building
        StringBuilder sb = new StringBuilder();
        
        // C#: foreach loop for string iteration
        foreach (char c in str) {
            if (c == 'o') {
                
                // C#: Enumerable.Range() + LINQ to generate number sequence
                sb.Append(string.Join("", Enumerable.Range(1, count).Select(i => i.ToString())));
                count++;
            } else {
                
                // C#: .Append() adds to StringBuilder
                sb.Append(c);
            }
        }
        
        // C#: .ToString() converts to string
        return sb.ToString();
    }
    
    public static string ReplacedString3(string str) {
        int count = 1;
        
        // C#: LINQ .SelectMany() flattens results, new string() constructor
        return new string(str.SelectMany(c => {
            
            // C#: char.ToLower() for case-insensitive comparison
            if (char.ToLower(c) == 'o') {
                
                // C#: new string(char, count) constructor for repetition
                return new string('&', count++);
            }
            
            // C#: .ToString() converts char to string
            return c.ToString();
        }).ToArray());
    }
}