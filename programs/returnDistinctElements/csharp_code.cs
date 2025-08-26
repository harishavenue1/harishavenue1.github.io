using System;
using System.Linq;

public class ReturnDistinctElements {
    public static void Main(string[] args) {
        int[] arr = {0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 9};
        Console.WriteLine("Returned distinct array is " + string.Join(", ", returnDistinctElements(arr)));
    }
    
    public static int[] returnDistinctElements(int[] arr) {

        // Two-pointer technique: slow tracks unique elements, fast scans array
        int slow = 0, fast = 1;
        while (fast < arr.Length) {  // C#: .Length property (capital L)
            if (arr[slow] != arr[fast]) {
                slow++;  // Move to next position for unique element
                arr[slow] = arr[fast];  // Place unique element
            }
            fast++;  // Always move fast pointer
        }

        // C#: LINQ .Take() method + .ToArray() creates new array
        return arr.Take(slow + 1).ToArray();
    }
}