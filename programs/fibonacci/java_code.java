package programs.fibonacci;

class java_code 
{
    public static void main(String[] args) {
		int n = 10;
		System.out.println("Fibo series "+ Arrays.toString(fiboSeries(n)));
	}

	public static int[] fiboSeries(int n) {
		
		// Java: Array initialization with specified size
		int[] arr = new int[n];
		
		// Java: Arrays.fill() initializes all elements to -1
		Arrays.fill(arr, -1);
		
		// Initialize first two Fibonacci numbers
		int a = 0, b = 1, temp = 0;
		
		// Java: Standard for-loop for iteration
		for (int i = 0; i < n; i++) {
			
			// Store current Fibonacci number
			arr[i] = a;
			
			// Calculate next Fibonacci number: F(n) = F(n-1) + F(n-2)
			temp = a;
			a = b;
			b = temp + b;
		}
		return arr;
	}
}
