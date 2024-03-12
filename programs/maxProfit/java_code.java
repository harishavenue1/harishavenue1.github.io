package programs.maxProfit;

class java_code {
    public static int maxProfit(int[] prices) {
        int maxProfit = 0;
        int leftIndex = 0, rightIndex = 1;
        int currentProfit = 0;
        while (rightIndex < prices.length) {
            if (prices[rightIndex] > prices[leftIndex]) {
                currentProfit = prices[rightIndex] - prices[leftIndex];
                maxProfit = Math.max(currentProfit, maxProfit);
            }
            else {
                leftIndex = rightIndex;
            }
            rightIndex++;
        }
        return maxProfit;
    }
    public static void main(String[] args) {
        int profit = maxProfit(new int[] {7,6,4,3,1}); //[7,1,5,3,6,4] -> 5 && [7,6,4,3,1] --> 0
        System.out.println(profit);
    }
}
