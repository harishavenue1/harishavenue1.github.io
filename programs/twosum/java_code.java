package programs.twosum;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class java_code 
{
    public static void main(String[] args) 
    {
        int[] array = new int[] { 1, 23, 4, 5, 6 };
        int target = 9;
        int[] output = twoSum(array, target);
        System.out.println(Arrays.toString(output)); // return index of twosum=target
    }

    public static int[] twoSum(int[] nums, int target) 
    {
        Map<Integer, Integer> numMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) 
        {
            int key = target - nums[i];
            if (numMap.containsKey(key)) 
            {
                return new int[] { numMap.get(key), i };
            }
            numMap.put(nums[i], i);
        }
        return new int[] {}; // No solution found
    }
}
