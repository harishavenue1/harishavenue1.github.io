public uint reverseBits(uint n)
{
    
    // C#: Initialize result for reversed bits
    uint res = 0;
    
    // C#: Process all 32 bits
    for (int i = 0; i < 32; i++)
    {
        
        // C#: Extract least significant bit and place at correct position
        uint lsb = (n & 1) << (31 - i);
        
        // C#: OR operation to set bit in result
        res = res | lsb;
        
        // C#: Right shift to process next bit
        n = n >> 1;
    }
    
    return res;
}