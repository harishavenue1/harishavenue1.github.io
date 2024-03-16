package programs.maxProdArray;

class java_code
{
    public static void main(String[] args) 
    {
        int[] arr = {2,3,-2,4};
        int maxProd = maxProduct(arr);
        System.out.println("Max Product is "+ maxProd);

        arr = new int[] {-2,0,-1};
        maxProd = maxProduct(arr);
        System.out.println("Max Product is "+ maxProd);
    }

    public static int maxProduct(int[] nums) 
    {
        int arrLen = nums.length;
        int leftProd = 1, rightProd = 1;

        // default assigning to 1st value    
        int maxProd = nums[0];

        for (int i=0; i<arrLen; i++) 
        {
            // reset left or right prod if prod gets == 0
            leftProd = (leftProd==0 ? 1 : leftProd);
            rightProd = (rightProd==0 ? 1 : rightProd);

            leftProd *= nums[i];
            rightProd *= nums[arrLen - 1 - i];

            maxProd = Math.max(maxProd, Math.max(leftProd, rightProd));
        }
        return maxProd;
    }
}
