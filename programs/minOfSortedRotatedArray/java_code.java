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
        int left = 0, right = nums.length - 1, mid = 0;
        while (left < right - 1) 
        {
            mid = (left + right) / 2;
            if (nums[mid] > nums[right])
                left = mid;
            else
                right = mid;        
        }
        
        return (nums[left] < nums[right] ? nums[left]: nums[right]);
    }
}
