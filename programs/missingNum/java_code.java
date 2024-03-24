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
        List<Integer> expected = IntStream.range(0, nums.length + 1).boxed().collect(Collectors.toList());
        System.out.println("Expected " + expected);
        List<Integer> actual = Arrays.stream(nums).boxed().collect(Collectors.toList());
        System.out.println("Actual " + actual);
        expected.removeAll(actual);
        System.out.println("Missing Number " + expected);
    }

    public static void missingNum(int[] nums) {
        int length = nums.length;
        int expected = ((length + 1) * length / 2);
        int actual = Arrays.stream(nums).sum();
        System.out.println("Missing Number " + (expected - actual));
    }
}
