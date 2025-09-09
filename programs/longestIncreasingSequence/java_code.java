package programs.longestIncreasingSequence;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class java_code {

    public static void main(String[] args) {
        System.out.println("=== LONGEST INCREASING SUBSEQUENCE ALGORITHM ===");

        int[] arr = { 10, 9, 2, 5, 3, 7, 101, 18 };
        System.out.println("\nTest 1: " + Arrays.toString(arr));
        System.out.println("Result: " + longestSeq(arr));

        arr = new int[] { 0, 1, 0, 3, 2, 3 };
        System.out.println("\nTest 2: " + Arrays.toString(arr));
        System.out.println("Result: " + longestSeq(arr));

        arr = new int[] { 7, 7, 7, 7, 7, 7, 7 };
        System.out.println("\nTest 3: " + Arrays.toString(arr));
        System.out.println("Result: " + longestSeq(arr));
    }

    public static int longestSeq(int[] nums) {
        List<Integer> li = new ArrayList<>();
        for (int i : nums) {
            // add elements if current element is greater than last index of list
            if (li.size() == 0 || li.get(li.size() - 1) < i) {
                li.add(i);
            }
            // else find index to insert the lesser value element in mid of list using
            // binary search
            else {
                int indx = binSearch(li, i);
                li.set(indx, i);
            }
        }
        return li.size();
    }

    public static int binSearch(List<Integer> li, int numValue) {
        int left = 0, right = li.size() - 1;
        int mid = 0;
        while (left <= right) {
            mid = (left + right) / 2;
            if (li.get(mid) == numValue)
                return mid;
            else if (li.get(mid) > numValue)
                right = mid - 1;
            else
                left = mid + 1;
        }
        return left;
    }
}
