def reverseBits(self, n: int) -> int:
    
    # Python: Initialize result for reversed bits
    result = 0
    
    # Python: Process all 32 bits
    for i in range(32):
        
        # Python: Extract least significant bit and place at correct position
        result |= (n & 1) << (31-i)
        
        # Python: Right shift to process next bit
        n >>= 1
    
    return result
