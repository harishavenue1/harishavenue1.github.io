using System;
using System.Collections.Generic;
using System.Linq;

class HashmapOperations
{
    static void Main()
    {
        // Create and initialize Dictionary
        Dictionary<string, int> fruits = new Dictionary<string, int>
        {
            {"apple", 5},
            {"banana", 3},
            {"cherry", 8}
        };
        Console.WriteLine($"Initial map: [{string.Join(", ", fruits.Select(kv => $"{kv.Key}={kv.Value}"))}]");
        
        // Add/Update operations
        fruits["apple"] = 10; // Update existing
        fruits["grape"] = 6; // Add new
        fruits.Add("mango", 4);
        Console.WriteLine($"After adding: [{string.Join(", ", fruits.Select(kv => $"{kv.Key}={kv.Value}"))}]");
        
        // Get operations
        Console.WriteLine($"Apple count: {fruits["apple"]}");
        Console.WriteLine($"Kiwi count: {fruits.GetValueOrDefault("kiwi", 0)}");
        
        // TryGetValue for safe access
        if (fruits.TryGetValue("banana", out int bananaCount))
        {
            Console.WriteLine($"Banana count (safe): {bananaCount}");
        }
        
        // Check operations
        Console.WriteLine($"Contains apple: {fruits.ContainsKey("apple")}");
        Console.WriteLine($"Contains value 8: {fruits.ContainsValue(8)}");
        Console.WriteLine($"Count: {fruits.Count}");
        Console.WriteLine($"Is empty: {fruits.Count == 0}");
        
        // LINQ operations
        var highValueFruits = fruits.Where(kv => kv.Value > 5).ToDictionary(kv => kv.Key, kv => kv.Value);
        Console.WriteLine($"High value fruits: [{string.Join(", ", highValueFruits.Select(kv => $"{kv.Key}={kv.Value}"))}]");
        
        // Update values
        if (fruits.ContainsKey("cherry"))
        {
            fruits["cherry"] = 15;
        }
        Console.WriteLine($"After updating cherry: [{string.Join(", ", fruits.Select(kv => $"{kv.Key}={kv.Value}"))}]");
        
        // Iteration methods
        Console.WriteLine($"Keys: [{string.Join(", ", fruits.Keys)}]");
        Console.WriteLine($"Values: [{string.Join(", ", fruits.Values)}]");
        
        // Iterate through entries
        Console.WriteLine("Iteration:");
        foreach (var kvp in fruits)
        {
            Console.WriteLine($"  {kvp.Key} = {kvp.Value}");
        }
        
        // Create second dictionary
        Dictionary<string, int> citrus = new Dictionary<string, int>
        {
            {"orange", 12},
            {"lemon", 3},
            {"lime", 5}
        };
        
        // Merge dictionaries
        Dictionary<string, int> combined = new Dictionary<string, int>(fruits);
        foreach (var kvp in citrus)
        {
            if (combined.ContainsKey(kvp.Key))
                combined[kvp.Key] += kvp.Value;
            else
                combined[kvp.Key] = kvp.Value;
        }
        Console.WriteLine($"Combined maps: [{string.Join(", ", combined.Select(kv => $"{kv.Key}={kv.Value}"))}]");
        
        // Remove operations
        fruits.Remove("banana");
        Console.WriteLine($"After removing banana: [{string.Join(", ", fruits.Select(kv => $"{kv.Key}={kv.Value}"))}]");
        
        // TryAdd (C# 6.0+)
        bool added = fruits.TryAdd("pear", 2);
        Console.WriteLine($"Pear added: {added}");
        
        // Clear dictionary
        fruits.Clear();
        Console.WriteLine($"After clear: [{string.Join(", ", fruits.Select(kv => $"{kv.Key}={kv.Value}"))}]");
    }
}