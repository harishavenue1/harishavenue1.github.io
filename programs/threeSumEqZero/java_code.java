package programs.threeSumEqZero;

import java.util.*;

// The main method must be in a class named "Main".
class java_code {
    public static void main(String[] args) {
        int[] arr = { -1, 0, 1, 2, -1, -4 };
        List<List<Integer>> output = threeSumEqZero(arr);
        System.out.println("List of Values Equals to Zero " + output);
    }

    public static List<List<Integer>> threeSumEqZero(int[] nums) {
        // sort the array
        Arrays.sort(nums);

        // to store unique values
        Set<List<Integer>> valuesSet = new HashSet<>();

        // to store all possible values eq = 0
        List<List<Integer>> valuesList = new ArrayList<>();

        int sum = 0, leftIndex = 0, rightIndex = nums.length - 1;

        for (int i = 0; i < nums.length; i++) {
            leftIndex = i + 1;
            while (leftIndex < rightIndex) {
                sum = nums[i] + nums[leftIndex] + nums[rightIndex];
                if (sum > 0)
                    rightIndex--; // array is sorted, so rightIndex has highest value
                else if (sum < 0)
                    leftIndex++;
                else {
                    valuesSet.add(Arrays.asList(nums[i], nums[leftIndex], nums[rightIndex]));
                    leftIndex++;
                    rightIndex--;
                }
            }
        }
        valuesList.addAll(valuesSet);
        return valuesList;
    }
}