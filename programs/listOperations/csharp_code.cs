using System;
using System.Collections.Generic;
using System.Linq;

class ListOperations
{
    static void Main()
    {
        // Create and initialize list
        List<string> fruits = new List<string> { "apple", "banana", "cherry" };
        Console.WriteLine($"Initial list: [{string.Join(", ", fruits)}]");
        
        // Add operations
        fruits.Insert(1, "orange");
        fruits.AddRange(new[] { "grape", "mango" });
        Console.WriteLine($"After adding: [{string.Join(", ", fruits)}]");
        
        // Access operations
        Console.WriteLine($"First item: {fruits[0]}");
        Console.WriteLine($"Index of banana: {fruits.IndexOf("banana")}");
        Console.WriteLine($"Contains apple: {fruits.Contains("apple")}");
        
        // Modify operations
        fruits[0] = "pineapple";
        Console.WriteLine($"After replacing: [{string.Join(", ", fruits)}]");
        
        // Remove operations
        fruits.Remove("banana");
        fruits.RemoveAt(0);
        Console.WriteLine($"After removing: [{string.Join(", ", fruits)}]");
        
        // Size and empty check
        Console.WriteLine($"Count: {fruits.Count}");
        Console.WriteLine($"Is empty: {fruits.Count == 0}");
        
        // Sort and reverse
        fruits.Sort();
        Console.WriteLine($"Sorted: [{string.Join(", ", fruits)}]");
        fruits.Reverse();
        Console.WriteLine($"Reversed: [{string.Join(", ", fruits)}]");
        
        // Convert List to Array
        string[] fruitsArray = fruits.ToArray();
        Console.WriteLine($"List to Array: [{string.Join(", ", fruitsArray)}]");
        
        // Convert Array to List
        string[] newArray = { "kiwi", "peach", "plum" };
        List<string> newList = newArray.ToList();
        Console.WriteLine($"Array to List: [{string.Join(", ", newList)}]");
        
        // Clear list
        fruits.Clear();
        Console.WriteLine($"After clear: [{string.Join(", ", fruits)}]");
    }
}