def groupAnagrams(strs):
    
    # Python: Import defaultdict for automatic list creation
    from collections import defaultdict
    
    
    # Python: defaultdict(list) creates empty list for new keys automatically
    anagram_map = defaultdict(list)
    
    
    # Python: Direct iteration over list
    for s in strs:
        
        # Python: sorted() returns sorted characters, ''.join() creates string key
        key = ''.join(sorted(s))
        
        # Python: .append() adds to list, no need to check if key exists
        anagram_map[key].append(s)
    
    
    # Python: .values() returns dict values, list() converts to list
    return list(anagram_map.values())