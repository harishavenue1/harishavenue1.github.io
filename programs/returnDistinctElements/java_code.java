import java.util.Arrays;

public class ReturnDistinctElements {
	
	public static void main(String[] args) {
		int[] arr = {0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 9};
		System.out.println("Returned distinct array is "+ Arrays.toString(returnDistinctElements(arr)));
	}
	
	public static int[] returnDistinctElements(int[] arr) {
		
		// Two-pointer technique: slow tracks unique elements, fast scans array
		int slow=0, fast=1;
		
		while (fast<arr.length) {
			if (arr[slow] != arr[fast]) {
				
				// Move to next position for unique element
				slow++;
				
				// Place unique element
				arr[slow] = arr[fast];
			}
			
			// Always move fast pointer
			fast++;
		}
		
		// Java: Arrays.stream() creates new array from range [0, slow+1)
		return Arrays.stream(arr, 0, slow+1).toArray();
	}
}
