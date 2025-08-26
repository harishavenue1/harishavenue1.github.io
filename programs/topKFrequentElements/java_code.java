public int[] topKFrequent(int[] nums, int k) {
    
    // Java: HashMap to count frequency of each number
    Map<Integer, Integer> count = new HashMap<>();
    
    // Java: Enhanced for-loop for array iteration
    for (int num : nums) {
        
        // Java: .getOrDefault() provides 0 if key doesn't exist
        count.put(num, count.getOrDefault(num, 0) + 1);
    }
    
    
    // Java: PriorityQueue (max-heap) with custom comparator using lambda
    PriorityQueue<Integer> heap = new PriorityQueue<>(
        (a, b) -> count.get(b) - count.get(a)  // Sort by frequency descending
    );
    
    
    // Java: .addAll() adds all keys to priority queue
    heap.addAll(count.keySet());
    
    
    // Java: Array initialization with specified size
    int[] result = new int[k];
    for (int i = 0; i < k; i++) {
        
        // Java: .poll() removes and returns highest priority element
        result[i] = heap.poll();
    }
    
    return result;
}