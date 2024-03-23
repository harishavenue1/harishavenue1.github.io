def countBits(n):
    arr = [0] * (n+1)
    for i in range(n+1):
        arr[i] = arr[i>>1] + (i & 1)
    return arr

num = 2
print('For Num:',num,'No of Bits are',countBits(num))
num = 5
print('For Num:',num,'No of Bits are',countBits(num))