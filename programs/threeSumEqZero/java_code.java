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
        
        // Java: Sort array for two-pointer technique
        Arrays.sort(nums);

        
        // Java: HashSet to store unique triplets (avoids duplicates)
        Set<List<Integer>> valuesSet = new HashSet<>();

        
        // Java: ArrayList to store final result
        List<List<Integer>> valuesList = new ArrayList<>();

        int sum = 0, leftIndex = 0, rightIndex = nums.length - 1;

        
        // Java: Outer loop fixes first element of triplet
        for (int i = 0; i < nums.length; i++) {
            
            // Start after current element
            leftIndex = i + 1;
            
            // Start from end
            rightIndex = nums.length - 1;
            
            
            // Java: Two-pointer approach for remaining two elements
            while (leftIndex < rightIndex) {
                sum = nums[i] + nums[leftIndex] + nums[rightIndex];
                
                if (sum > 0)
                    
                    // Decrease sum (array is sorted)
                    rightIndex--;
                else if (sum < 0)
                    
                    // Increase sum
                    leftIndex++;
                else {
                    
                    // Found triplet that sums to zero
                    valuesSet.add(Arrays.asList(nums[i], nums[leftIndex], nums[rightIndex]));
                    leftIndex++;
                    rightIndex--;
                }
            }
        }
        
        
        // Java: .addAll() converts Set to List
        valuesList.addAll(valuesSet);
        return valuesList;
    }
}