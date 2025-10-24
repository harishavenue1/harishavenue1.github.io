def divisibility_check():
    num = 64
    print("Number:", num)
    
    # Traditional modulo approach
    if num % 32 == 0:
        print("abc")
    elif num % 16 == 0:
        print("b")
    elif num % 8 == 0:
        print("a")
    else:
        print("none")
    
    # Bitwise approach (tricky interview method)
    print("\nBitwise approach:")
    if (num & 31) == 0:
        print("abc")
    elif (num & 15) == 0:
        print("b")
    elif (num & 7) == 0:
        print("a")
    else:
        print("none")

divisibility_check()