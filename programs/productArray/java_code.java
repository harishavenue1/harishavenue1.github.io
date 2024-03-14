package programs.productArray;

public class java_code 
{
    public static void main(String[] args) {
      int[] arr = {1, 2, 3, 4};
      int[] prodArray = productExceptSelf(arr);
      System.out.println("Prod Arr -> "+ Arrays.toString(prodArray));
      
      arr = new int[] {-1, 1, 0, -3, 3};
      prodArray = productExceptSelf(arr);
      System.out.println("Prod Arr -> "+ Arrays.toString(prodArray));
    }
    
    public static int[] productExceptSelf(int[] nums) {
      int len = nums.length;
      int[] answer = new int[len];
      int pre=1, post=1;
      
      for (int i=0; i<len; i++) {
        answer[i] = pre;
        pre *= nums[i];
      }
      
      for (int i=len-1; i>=0; i--) {
        answer[i] *= post;
        post *= nums[i];
      }
      return answer;
    }
}
