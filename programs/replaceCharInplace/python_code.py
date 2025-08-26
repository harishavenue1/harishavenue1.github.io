def replaced_string_1(s):
    
    # Python: list() converts string to list of characters
    chars = list(s)
    
    # Python: range() for index-based iteration
    for i in range(len(chars)):
        if chars[i] == 'o':
            
            # Python: Direct assignment to modify list element
            chars[i] = '&'
    
    # Python: ''.join() concatenates list elements into string
    return ''.join(chars)

def replaced_string_2(s):
    count = 1
    
    # Python: List to collect results
    result = []
    
    # Python: Direct iteration over string characters
    for c in s:
        if c == 'o':
            
            # Python: Generator expression with range() to create number sequence
            result.append(''.join(str(i) for i in range(1, count + 1)))
            count += 1
        else:
            
            # Python: .append() adds to list
            result.append(c)
    
    return ''.join(result)

def replaced_string_3(s):
    count = 1
    chars = list(s)
    
    for i in range(len(chars)):
        
        # Python: .lower() method for case-insensitive comparison
        if chars[i].lower() == 'o':
            
            # Python: * operator for string repetition
            chars[i] = '&' * count
            count += 1
    
    return ''.join(chars)

if __name__ == "__main__":
    s = "tomorrow"
    print(f"Replaced String {replaced_string_1(s)}")
    print(f"Replaced String {replaced_string_2(s)}")
    print(f"Replaced String {replaced_string_3(s)}")