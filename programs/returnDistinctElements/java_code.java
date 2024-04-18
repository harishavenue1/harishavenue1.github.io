import java.util.Arrays;

public class ReturnDistinctElements {
	
	public static void main(String[] args) {
		int[] arr = {0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 8, 9};
		System.out.println("Returned distinct array is "+ Arrays.toString(returnDistinctElements(arr)));
	}
	
	public static int[] returnDistinctElements(int[] arr) {
		int slow=0, fast=1;
		while (fast<arr.length) {
			if (arr[slow] != arr[fast]) {
				slow++;
				arr[slow] = arr[fast];
			}
			fast++;
		}
		return Arrays.stream(arr, 0, slow+1).toArray();
	}
}
