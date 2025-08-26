package programs.mergeSortedArrays;

import java.util.*;

class java_code {
    public static void main(String[] args) {
        int[] arr1 = { 1, 3, 5, 7 };
        int[] arr2 = { 2, 4, 6, 8 };
        int[] arr3 = mergeSortedArrays(arr1, arr2);
        System.out.println("Merged Array " + Arrays.toString(arr3));
    }

    public static int[] mergeSortedArrays(int[] a, int[] b) {
        
        // Java: Get array lengths
        int len1 = a.length;
        int len2 = b.length;
        
        // Java: Create result array with combined size
        int[] c = new int[len1 + len2];

        
        // Java: Three pointers for merging
        int i = 0, j = 0, k = 0;
        
        // Java: Merge while both arrays have elements
        while (i < len1 && j < len2) {
            
            // Java: Compare and add smaller element
            if (a[i] < b[j])
                c[k++] = a[i++];
            else
                c[k++] = b[j++];
        }

        
        // Java: Add remaining elements from first array
        while (i < len1)
            c[k++] = a[i++];

        
        // Java: Add remaining elements from second array
        while (j < len2)
            c[k++] = b[j++];

        return c;
    }
}