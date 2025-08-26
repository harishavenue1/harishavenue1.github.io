public bool IsValid(string s) {

    // C#: Stack<T> generic collection for LIFO operations
    Stack<char> stack = new Stack<char>();

    // C#: Dictionary with collection initializer syntax
    Dictionary<char, char> map = new Dictionary<char, char> {
        {')', '('}, {'}', '{'}, {']', '['}
    };
    
    // C#: foreach loop for string iteration
    foreach (char c in s) {

        // C#: .ContainsKey() method to check if key exists
        if (map.ContainsKey(c)) {

            // C#: .Count property, .Pop() removes top element
            if (stack.Count == 0 || stack.Pop() != map[c]) {
                return false;
            }
        } else {

            // C#: .Push() adds to top of stack
            stack.Push(c);
        }
    }
    
    // C#: Check if stack is empty using .Count property
    return stack.Count == 0;
}