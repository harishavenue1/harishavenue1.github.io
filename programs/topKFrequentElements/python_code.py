def topKFrequent(nums, k):
    
    # Python: Import Counter for frequency counting and heapq for heap operations
    from collections import Counter
    import heapq
    
    
    # Python: Counter automatically counts frequency of elements
    count = Counter(nums)
    
    # Python: heapq.nlargest() finds k largest elements using custom key function
    return heapq.nlargest(k, count.keys(), key=count.get)