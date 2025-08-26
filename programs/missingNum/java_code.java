package programs.missingNum;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class java_code {

    public static void main(String[] args) {
        int[] arr = { 9, 6, 4, 2, 3, 5, 7, 0, 1 };
        missingNumber(arr);
        missingNum(arr);
    }

    public static void missingNumber(int[] nums) {

        // Java: Stream API approach - create expected range and find difference
        List<Integer> expected = IntStream.range(0, nums.length + 1)
                                         .boxed()
                                         .collect(Collectors.toList());
        System.out.println("Expected " + expected);
        
        // Java: Convert array to List using Arrays.stream()
        List<Integer> actual = Arrays.stream(nums)
                                    .boxed()
                                    .collect(Collectors.toList());
        System.out.println("Actual " + actual);
        
        // Java: .removeAll() finds set difference
        expected.removeAll(actual);
        System.out.println("Missing Number " + expected);
    }

    public static void missingNum(int[] nums) {

        // Java: Mathematical approach using sum formula
        int length = nums.length;
        
        // Sum of first n natural numbers: n*(n+1)/2
        int expected = ((length + 1) * length / 2);
        
        // Java: Arrays.stream().sum() calculates actual sum
        int actual = Arrays.stream(nums).sum();
        
        System.out.println("Missing Number " + (expected - actual));
    }
}
