package programs.reverseBits;

public class java_code {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int result = 0;
        int leastBit = 0;
        for (int i = 0; i < 32; i++) {
            // get rightMost bit of n and move to left most bit
            leastBit = (n & 1) << (31 - i);
            // or condition merge with result
            result |= leastBit;
            // remove recent used bit by moving 1step right
            n = n >> 1;
        }
        return result;
    }
}