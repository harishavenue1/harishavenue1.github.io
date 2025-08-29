using System;
using System.Collections.Generic;
using System.Linq;

class SetOperations
{
    static void Main()
    {
        // Create and initialize sets
        HashSet<string> fruits = new HashSet<string> { "apple", "banana", "cherry" };
        fruits.Add("apple"); // Duplicate - won't be added
        Console.WriteLine($"Initial set: [{string.Join(", ", fruits)}]");
        
        // Add operations
        fruits.UnionWith(new[] { "grape", "mango", "banana" });
        Console.WriteLine($"After adding: [{string.Join(", ", fruits)}]");
        
        // Check operations
        Console.WriteLine($"Contains apple: {fruits.Contains("apple")}");
        Console.WriteLine($"Count: {fruits.Count}");
        Console.WriteLine($"Is empty: {fruits.Count == 0}");
        
        // Create second set for operations
        HashSet<string> citrus = new HashSet<string> { "orange", "lemon", "grape" };
        Console.WriteLine($"Citrus set: [{string.Join(", ", citrus)}]");
        
        // Set operations - Union
        HashSet<string> union = new HashSet<string>(fruits);
        union.UnionWith(citrus);
        Console.WriteLine($"Union: [{string.Join(", ", union)}]");
        
        // Set operations - Intersection
        HashSet<string> intersection = new HashSet<string>(fruits);
        intersection.IntersectWith(citrus);
        Console.WriteLine($"Intersection: [{string.Join(", ", intersection)}]");
        
        // Set operations - Difference
        HashSet<string> difference = new HashSet<string>(fruits);
        difference.ExceptWith(citrus);
        Console.WriteLine($"Difference (fruits - citrus): [{string.Join(", ", difference)}]");
        
        // Set operations - Symmetric Difference
        HashSet<string> symDiff = new HashSet<string>(fruits);
        symDiff.SymmetricExceptWith(citrus);
        Console.WriteLine($"Symmetric Difference: [{string.Join(", ", symDiff)}]");
        
        // Check subset/superset
        HashSet<string> subset = new HashSet<string> { "apple", "banana" };
        Console.WriteLine($"Is subset: {subset.IsSubsetOf(fruits)}");
        Console.WriteLine($"Is superset: {fruits.IsSupersetOf(subset)}");
        
        // Convert to array and list
        string[] fruitsArray = fruits.ToArray();
        Console.WriteLine($"Set to Array: [{string.Join(", ", fruitsArray)}]");
        
        List<string> fruitsList = fruits.ToList();
        Console.WriteLine($"Set to List: [{string.Join(", ", fruitsList)}]");
        
        // Check overlaps
        Console.WriteLine($"Overlaps with citrus: {fruits.Overlaps(citrus)}");
        Console.WriteLine($"Set equals citrus: {fruits.SetEquals(citrus)}");
        
        // Remove operations
        fruits.Remove("banana");
        Console.WriteLine($"After removing banana: [{string.Join(", ", fruits)}]");
        
        // Clear set
        fruits.Clear();
        Console.WriteLine($"After clear: [{string.Join(", ", fruits)}]");
    }
}