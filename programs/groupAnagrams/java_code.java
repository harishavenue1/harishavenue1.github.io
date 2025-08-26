public List<List<String>> groupAnagrams(String[] strs) {

    // Java: HashMap to group anagrams by sorted character key
    Map<String, List<String>> map = new HashMap<>();
    
    // Java: Enhanced for-loop for array iteration
    for (String str : strs) {

        // Java: .toCharArray() converts string to char array
        char[] chars = str.toCharArray();

        // Java: Arrays.sort() sorts character array in-place
        Arrays.sort(chars);

        // Java: String.valueOf() converts char array back to string
        String key = String.valueOf(chars);
        
        // Java: .computeIfAbsent() creates list if key doesn't exist, then adds
        map.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
    }
    
    // Java: new ArrayList<>(collection) creates list from map values
    return new ArrayList<>(map.values());
}