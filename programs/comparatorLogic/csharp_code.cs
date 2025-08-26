using System;
using System.Collections.Generic;
using System.Linq;

public class Person
{
    public string Name { get; set; }
    public int Age { get; set; }
    public int Score { get; set; }
    
    public Person(string name, int age, int score)
    {
        Name = name;
        Age = age;
        Score = score;
    }
    
    public override string ToString()
    {
        return $"{{Name='{Name}', Age={Age}, Score={Score}}}";
    }
}

public class Task
{
    public string Name { get; set; }
    public string Priority { get; set; }
    public int Timestamp { get; set; }
    
    public Task(string name, string priority, int timestamp)
    {
        Name = name;
        Priority = priority;
        Timestamp = timestamp;
    }
    
    public override string ToString()
    {
        return $"{{Name='{Name}', Priority='{Priority}', Timestamp={Timestamp}}}";
    }
}

// C#: Custom string comparer - length first, then alphabetical
public class CustomStringComparer : IComparer<string>
{
    public int Compare(string x, string y)
    {
        
        // Compare by length first
        if (x.Length != y.Length)
        {
            return x.Length.CompareTo(y.Length);
        }
        
        
        // C#: String.Compare for alphabetical comparison
        return string.Compare(x, y, StringComparison.Ordinal);
    }
}

// C#: Multi-criteria person comparer
public class PersonComparer : IComparer<Person>
{
    public int Compare(Person x, Person y)
    {
        
        // Compare by age first
        int ageComparison = x.Age.CompareTo(y.Age);
        if (ageComparison != 0)
        {
            return ageComparison;
        }
        
        
        // Compare by name if ages are equal
        int nameComparison = string.Compare(x.Name, y.Name, StringComparison.Ordinal);
        if (nameComparison != 0)
        {
            return nameComparison;
        }
        
        
        // C#: Compare by score (descending) if names are equal
        return y.Score.CompareTo(x.Score);
    }
}

// C#: Priority-based task comparer
public class TaskComparer : IComparer<Task>
{
    private readonly Dictionary<string, int> priorityOrder = new Dictionary<string, int>
    {
        { "high", 3 },
        { "medium", 2 },
        { "low", 1 }
    };
    
    public int Compare(Task x, Task y)
    {
        
        // Compare by priority first (higher priority first)
        int p1 = priorityOrder.ContainsKey(x.Priority) ? priorityOrder[x.Priority] : 1;
        int p2 = priorityOrder.ContainsKey(y.Priority) ? priorityOrder[y.Priority] : 1;
        
        if (p1 != p2)
        {
            return p2.CompareTo(p1);
        }
        
        
        // C#: Compare by timestamp if priorities are equal
        return x.Timestamp.CompareTo(y.Timestamp);
    }
}

public class ComparatorLogic
{
    public static List<string> SortStringsCustom(List<string> strings)
    {
        
        // C#: LINQ OrderBy with custom comparer
        return strings.OrderBy(s => s, new CustomStringComparer()).ToList();
    }
    
    public static List<Person> SortPeopleMultiCriteria(List<Person> people)
    {
        
        // C#: Sort using custom comparer
        var sorted = people.ToList();
        sorted.Sort(new PersonComparer());
        return sorted;
    }
    
    public static List<Task> SortTasksByPriority(List<Task> tasks)
    {
        
        // C#: Sort using priority-based comparer
        var sorted = tasks.ToList();
        sorted.Sort(new TaskComparer());
        return sorted;
    }
    
    public static T FindKthElement<T>(List<T> list, int k, IComparer<T> comparer = null)
    {
        
        // C#: Sort with custom comparer and return kth element
        var sorted = comparer != null 
            ? list.OrderBy(x => x, comparer).ToList()
            : list.OrderBy(x => x).ToList();
        
        if (k >= 1 && k <= sorted.Count)
        {
            return sorted[k - 1];
        }
        
        return default(T);
    }
    
    public static List<T> MergeSortedArrays<T>(List<T> arr1, List<T> arr2, IComparer<T> comparer = null)
    {
        
        // C#: Merge two sorted arrays using comparer
        var result = new List<T>();
        int i = 0, j = 0;
        
        var comp = comparer ?? Comparer<T>.Default;
        
        while (i < arr1.Count && j < arr2.Count)
        {
            if (comp.Compare(arr1[i], arr2[j]) <= 0)
            {
                result.Add(arr1[i]);
                i++;
            }
            else
            {
                result.Add(arr2[j]);
                j++;
            }
        }
        
        
        // C#: Add remaining elements using AddRange
        result.AddRange(arr1.Skip(i));
        result.AddRange(arr2.Skip(j));
        
        return result;
    }
    
    public static int BinarySearchWithComparer<T>(List<T> arr, T target, IComparer<T> comparer)
    {
        
        // C#: Binary search with custom comparer
        int left = 0, right = arr.Count - 1;
        
        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            int comparison = comparer.Compare(arr[mid], target);
            
            if (comparison == 0)
            {
                return mid;
            }
            else if (comparison < 0)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }
        
        return -1;
    }
    
    public static List<T> SortByMultipleCriteria<T>(List<T> data, params (Func<T, object> keySelector, bool descending)[] criteria)
    {
        
        // C#: Generic multi-criteria sorting using LINQ
        IOrderedEnumerable<T> query = null;
        
        for (int i = 0; i < criteria.Length; i++)
        {
            var (keySelector, descending) = criteria[i];
            
            if (i == 0)
            {
                query = descending 
                    ? data.OrderByDescending(keySelector)
                    : data.OrderBy(keySelector);
            }
            else
            {
                query = descending
                    ? query.ThenByDescending(keySelector)
                    : query.ThenBy(keySelector);
            }
        }
        
        return query?.ToList() ?? data.ToList();
    }
    
    public static Comparison<T> CreateComparison<T, TKey>(Func<T, TKey> keyExtractor, bool reverse = false) where TKey : IComparable<TKey>
    {
        
        // C#: Higher-order function to create comparison delegates
        return (x, y) =>
        {
            var result = keyExtractor(x).CompareTo(keyExtractor(y));
            return reverse ? -result : result;
        };
    }
    
    public static void Main(string[] args)
    {
        
        // Test string sorting with custom comparer
        var strings = new List<string> { "apple", "pie", "a", "longer", "cat" };
        var sortedStrings = SortStringsCustom(strings);
        Console.WriteLine("Custom sorted strings: [" + string.Join(", ", sortedStrings) + "]");
        
        
        // Test multi-criteria person sorting
        var people = new List<Person>
        {
            new Person("Alice", 30, 85),
            new Person("Bob", 25, 90),
            new Person("Charlie", 25, 95),
            new Person("Alice", 30, 80)
        };
        
        var sortedPeople = SortPeopleMultiCriteria(people);
        Console.WriteLine("\nSorted people:");
        sortedPeople.ForEach(person => Console.WriteLine($"  {person}"));
        
        
        // Test priority-based task sorting
        var tasks = new List<Task>
        {
            new Task("Task1", "low", 100),
            new Task("Task2", "high", 50),
            new Task("Task3", "medium", 75),
            new Task("Task4", "high", 25)
        };
        
        var sortedTasks = SortTasksByPriority(tasks);
        Console.WriteLine("\nSorted tasks by priority:");
        sortedTasks.ForEach(task => Console.WriteLine($"  {task}"));
        
        
        // Test kth element finding
        var numbers = new List<int> { 64, 34, 25, 12, 22, 11, 90 };
        var kthElement = FindKthElement(numbers, 3);
        Console.WriteLine($"\n3rd smallest element: {kthElement}");
        
        
        // Test merging sorted arrays
        var arr1 = new List<int> { 1, 3, 5, 7 };
        var arr2 = new List<int> { 2, 4, 6, 8 };
        var merged = MergeSortedArrays(arr1, arr2);
        Console.WriteLine($"\nMerged arrays: [{string.Join(", ", merged)}]");
        
        
        // Test generic multi-criteria sorting
        var employees = new List<dynamic>
        {
            new { Name = "John", Department = "IT", Salary = 75000, Experience = 5 },
            new { Name = "Jane", Department = "HR", Salary = 65000, Experience = 3 },
            new { Name = "Bob", Department = "IT", Salary = 80000, Experience = 7 },
            new { Name = "Alice", Department = "HR", Salary = 70000, Experience = 4 }
        };
        
        
        // C#: LINQ multi-criteria sorting
        var sortedEmployees = employees
            .OrderBy(e => e.Department)
            .ThenByDescending(e => e.Salary)
            .ThenByDescending(e => e.Experience)
            .ToList();
        
        Console.WriteLine("\nSorted employees by department, salary (desc), experience (desc):");
        sortedEmployees.ForEach(emp => Console.WriteLine($"  {emp}"));
    }
}