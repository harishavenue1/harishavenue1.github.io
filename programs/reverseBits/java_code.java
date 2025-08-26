package programs.reverseBits;

public class java_code {

    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        
        // Java: Bit manipulation to reverse 32-bit integer
        int result = 0;
        int leastBit = 0;
        
        // Java: Process all 32 bits of integer
        for (int i = 0; i < 32; i++) {
            
            // Java: Extract rightmost bit using AND (&) with 1
            // Then shift it to correct position from left using << operator
            leastBit = (n & 1) << (31 - i);
            
            // Java: Merge bit into result using OR (|) operator
            result |= leastBit;
            
            // Java: Right shift to process next bit using >> operator
            n = n >> 1;
        }
        
        return result;
    }
}