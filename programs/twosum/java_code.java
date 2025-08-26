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
        
        // Java: HashMap to store number -> index mapping for O(1) lookup
        Map<Integer, Integer> numMap = new HashMap<>();

        
        // Java: Standard for-loop with .length field
        for (int i = 0; i < nums.length; i++) 
        {
            
            // Calculate complement needed to reach target
            int key = target - nums[i];
            
            // Java: .containsKey() checks if complement exists in map
            if (numMap.containsKey(key)) 
            {
                
                // Java: Array literal syntax for return
                return new int[] { numMap.get(key), i };
            }
            
            // Java: .put() stores current number and its index
            numMap.put(nums[i], i);
        }
        return new int[] {}; // No solution found
    }
}
