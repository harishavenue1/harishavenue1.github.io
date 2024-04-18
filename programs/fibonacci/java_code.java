package programs.fibonacci;

class java_code 
{
    public static void main(String[] args) {
		int n = 10;
		System.out.println("Fibo series "+ Arrays.toString(fiboSeries(n)));
	}

	public static int[] fiboSeries(int n) {
		int[] arr = new int[n];
		Arrays.fill(arr, -1);
		int a = 0, b = 1, temp = 0;
		for (int i = 0; i < n; i++) {
			arr[i] = a;
			temp = a;
			a = b;
			b = temp + b;
		}
		return arr;
	}
}
