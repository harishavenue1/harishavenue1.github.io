public int[] TopKFrequent(int[] nums, int k) {
    
    // C#: Dictionary to count frequency of each number
    Dictionary<int, int> count = new Dictionary<int, int>();
    
    
    // C#: foreach loop for array iteration
    foreach (int num in nums) {
        
        // C#: .GetValueOrDefault() provides 0 if key doesn't exist
        count[num] = count.GetValueOrDefault(num, 0) + 1;
    }
    
    
    // C#: LINQ chain for sorting and selecting top k elements
    return count.OrderByDescending(x => x.Value)  // Sort by frequency descending
                .Take(k)                          // Take first k elements
                .Select(x => x.Key)               // Extract the numbers (keys)
                .ToArray();                       // Convert to array
}