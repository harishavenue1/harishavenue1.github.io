class java_code 
{
    public static void main(String[] args) 
    {
        int[] arr = {3,4,5,1,2};
        int output = findMin_sorted_rotatedArray(arr);
        System.out.println("Minimum of Sorted and if rotated Array is "+ output);

        arr = new int[] {4,5,6,7,0,1,2};
        output = findMin_sorted_rotatedArray(arr);
        System.out.println("Minimum of Sorted and if rotated Array is "+ output);

        arr = new int[] {11,13,15,17};
        output = findMin_sorted_rotatedArray(arr);
        System.out.println("Minimum of Sorted and if rotated Array is "+ output);
    }

    public static int findMin_sorted_rotatedArray(int[] nums) 
    {
        
        // Java: Binary search pointers for rotated array
        int leftIndex = 0, rightIndex = nums.length - 1, midIndex = 0;
        
        // Java: Modified binary search to find minimum
        while (leftIndex < rightIndex - 1) 
        {
            
            // Java: Calculate middle index
            midIndex = (leftIndex + rightIndex) / 2;
            
            // Java: Compare middle with right to determine which half to search
            if (nums[midIndex] > nums[rightIndex])
                leftIndex = midIndex;  // Minimum is in right half
            else
                rightIndex = midIndex;  // Minimum is in left half
        }
        
        
        // Java: Return smaller of the two remaining elements
        return (nums[leftIndex] < nums[rightIndex] ? nums[leftIndex]: nums[rightIndex]);
    }
}
