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
            int len1 = a.Length;
            int len2 = b.Length;
            int[] c = new int[len1 + len2];

            int i = 0, j = 0, k = 0;
            while (i < len1 && j < len2)
            {
                if (a[i] < b[j])
                    c[k++] = a[i++];
                else
                    c[k++] = b[j++];
            }

            while (i < len1)
                c[k++] = a[i++];

            while (j < len2)
                c[k++] = b[j++];

            return c;
        }
    }
}