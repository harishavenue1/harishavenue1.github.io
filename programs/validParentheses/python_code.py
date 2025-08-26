def isValid(s):
    
    # Python: List [] used as stack (LIFO with append/pop)
    stack = []
    
    # Python: Dictionary for closing -> opening bracket mapping
    mapping = {')': '(', '}': '{', ']': '['}
    
    
    # Python: Direct iteration over string
    for char in s:
        
        # Python: 'in' operator to check if key exists in dictionary
        if char in mapping:
            
            # Python: 'not stack' checks if list is empty, .pop() removes last element
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            
            # Python: .append() adds to end of list (top of stack)
            stack.append(char)
    
    
    # Python: 'not stack' returns True if list is empty
    return not stack