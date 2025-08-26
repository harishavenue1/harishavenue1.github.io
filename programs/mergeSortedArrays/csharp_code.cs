using System;

namespace MyCompiler
{
    class Program
    {
        public static void Main(string[] args)
        {
            int[] arr1 = { 1, 3, 5, 7 };
            int[] arr2 = { 2, 4, 6, 8 };
            int[] arr3 = mergeSortedArrays(arr1, arr2);
            Console.WriteLine("Merged Array " + String.Join(",", arr3));
        }
        public static int[] mergeSortedArrays(int[] a, int[] b)
        {
            
            // C#: Get array lengths using .Length property
            int len1 = a.Length;
            int len2 = b.Length;
            
            // C#: Create result array with combined size
            int[] c = new int[len1 + len2];

            
            // C#: Three pointers for merging
            int i = 0, j = 0, k = 0;
            
            // C#: Merge while both arrays have elements
            while (i < len1 && j < len2)
            {
                
                // C#: Compare and add smaller element
                if (a[i] < b[j])
                    c[k++] = a[i++];
                else
                    c[k++] = b[j++];
            }

            
            // C#: Add remaining elements from first array
            while (i < len1)
                c[k++] = a[i++];

            
            // C#: Add remaining elements from second array
            while (j < len2)
                c[k++] = b[j++];

            return c;
        }
    }
}