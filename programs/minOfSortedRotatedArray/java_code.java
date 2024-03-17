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
        int leftIndex = 0, rightIndex = nums.length - 1, midIndex = 0;
        while (leftIndex < rightIndex - 1) 
        {
            midIndex = (leftIndex + rightIndex) / 2;
            if (nums[midIndex] > nums[rightIndex])
                leftIndex = midIndex;
            else
                rightIndex = midIndex;        
        }
        
        return (nums[leftIndex] < nums[rightIndex] ? nums[leftIndex]: nums[rightIndex]);
    }
}
