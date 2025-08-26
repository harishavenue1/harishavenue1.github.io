def countBits(n):
    
    # Python: List comprehension to create array of zeros
    arr = [0] * (n+1)
    
    # Python: range(n+1) for inclusive iteration
    for i in range(n+1):
        
        # Python: Bit manipulation - count bits using DP
        # arr[i>>1] gets count for i/2, (i & 1) adds 1 if i is odd
        arr[i] = arr[i>>1] + (i & 1)
    
    return arr

num = 2
print('For Num:',num,'No of Bits are',countBits(num))
num = 5
print('For Num:',num,'No of Bits are',countBits(num))