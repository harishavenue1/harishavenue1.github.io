using System;
using System.Collections.Generic;
using System.Linq;

class StreamOperations
{
    static void Main()
    {
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        List<string> words = new List<string> { "apple", "banana", "cherry", "date", "elderberry" };
        
        Console.WriteLine($"Original numbers: [{string.Join(", ", numbers)}]");
        Console.WriteLine($"Original words: [{string.Join(", ", words)}]");
        
        // Where (Filter) operations
        var evenNumbers = numbers.Where(n => n % 2 == 0).ToList();
        Console.WriteLine($"Even numbers: [{string.Join(", ", evenNumbers)}]");
        
        // Select (Map) operations
        var squared = numbers.Select(n => n * n).ToList();
        Console.WriteLine($"Squared numbers: [{string.Join(", ", squared)}]");
        
        var upperWords = words.Select(w => w.ToUpper()).ToList();
        Console.WriteLine($"Uppercase words: [{string.Join(", ", upperWords)}]");
        
        // SelectMany (FlatMap) operations
        var nestedList = new List<List<int>>
        {
            new List<int> { 1, 2 },
            new List<int> { 3, 4 },
            new List<int> { 5, 6 }
        };
        var flattened = nestedList.SelectMany(list => list).ToList();
        Console.WriteLine($"Flattened: [{string.Join(", ", flattened)}]");
        
        // Aggregate (Reduce) operations
        int sum = numbers.Aggregate((a, b) => a + b);
        Console.WriteLine($"Sum: {sum}");
        
        int max = numbers.Max();
        Console.WriteLine($"Max: {max}");
        
        // Conversion operations
        var numberSet = numbers.ToHashSet();
        Console.WriteLine($"As HashSet: [{string.Join(", ", numberSet)}]");
        
        string joined = string.Join(", ", words);
        Console.WriteLine($"Joined: {joined}");
        
        // GroupBy operations
        var groupedByLength = words.GroupBy(w => w.Length)
            .ToDictionary(g => g.Key, g => g.ToList());
        Console.WriteLine("Grouped by length:");
        foreach (var group in groupedByLength)
        {
            Console.WriteLine($"  {group.Key}: [{string.Join(", ", group.Value)}]");
        }
        
        // Partitioning (using GroupBy)
        var partitioned = numbers.GroupBy(n => n > 5)
            .ToDictionary(g => g.Key, g => g.ToList());
        Console.WriteLine($"Partitioned (>5): True=[{string.Join(", ", partitioned.GetValueOrDefault(true, new List<int>()))}], False=[{string.Join(", ", partitioned.GetValueOrDefault(false, new List<int>()))}]");
        
        // OrderBy (Sorting)
        var sorted = words.OrderBy(w => w).ToList();
        Console.WriteLine($"Sorted words: [{string.Join(", ", sorted)}]");
        
        var sortedByLength = words.OrderBy(w => w.Length).ToList();
        Console.WriteLine($"Sorted by length: [{string.Join(", ", sortedByLength)}]");
        
        // Distinct
        var duplicates = new List<int> { 1, 2, 2, 3, 3, 4, 5 };
        var unique = duplicates.Distinct().ToList();
        Console.WriteLine($"Unique: [{string.Join(", ", unique)}]");
        
        // Take and Skip
        var taken = numbers.Take(5).ToList();
        Console.WriteLine($"Taken (5): [{string.Join(", ", taken)}]");
        
        var skipped = numbers.Skip(5).ToList();
        Console.WriteLine($"Skipped (5): [{string.Join(", ", skipped)}]");
        
        // Terminal operations
        long count = numbers.Where(n => n > 5).Count();
        Console.WriteLine($"Count > 5: {count}");
        
        bool any = numbers.Any(n => n > 8);
        Console.WriteLine($"Any > 8: {any}");
        
        bool all = numbers.All(n => n > 0);
        Console.WriteLine($"All > 0: {all}");
        
        int first = numbers.Where(n => n > 5).FirstOrDefault();
        Console.WriteLine($"First > 5: {first}");
        
        // Parallel LINQ (PLINQ)
        int parallelSum = numbers.AsParallel().Sum();
        Console.WriteLine($"Parallel sum: {parallelSum}");
        
        // Additional LINQ methods
        var reversed = numbers.Reverse().ToList();
        Console.WriteLine($"Reversed: [{string.Join(", ", reversed)}]");
        
        var zipped = numbers.Take(3).Zip(words.Take(3), (n, w) => $"{n}-{w}").ToList();
        Console.WriteLine($"Zipped: [{string.Join(", ", zipped)}]");
        
        // Set operations
        var list1 = new List<int> { 1, 2, 3, 4, 5 };
        var list2 = new List<int> { 4, 5, 6, 7, 8 };
        
        var union = list1.Union(list2).ToList();
        Console.WriteLine($"Union: [{string.Join(", ", union)}]");
        
        var intersect = list1.Intersect(list2).ToList();
        Console.WriteLine($"Intersect: [{string.Join(", ", intersect)}]");
        
        var except = list1.Except(list2).ToList();
        Console.WriteLine($"Except: [{string.Join(", ", except)}]");
    }
}