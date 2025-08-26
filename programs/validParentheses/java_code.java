public boolean isValid(String s) {
    
    // Java: Stack<Character> for LIFO operations
    Stack<Character> stack = new Stack<>();
    
    
    // Java: Enhanced for-loop with .toCharArray()
    for (char c : s.toCharArray()) {
        
        // Push opening brackets onto stack
        if (c == '(' || c == '[' || c == '{') {
            
            // Java: .push() adds to top of stack
            stack.push(c);
        } else {
            
            // Java: .isEmpty() checks if stack is empty
            if (stack.isEmpty()) return false;
            
            
            // Java: .pop() removes and returns top element
            char top = stack.pop();
            
            // Check if closing bracket matches opening bracket
            if ((c == ')' && top != '(') ||
                (c == ']' && top != '[') ||
                (c == '}' && top != '{')) {
                return false;
            }
        }
    }
    
    
    // Valid if all brackets are matched (stack empty)
    return stack.isEmpty();
}