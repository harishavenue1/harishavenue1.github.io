public IList<IList<string>> GroupAnagrams(string[] strs) {
    
    // C#: Dictionary to group anagrams by sorted character key
    Dictionary<string, IList<string>> map = new Dictionary<string, IList<string>>();
    
    
    // C#: foreach loop for array iteration
    foreach (string str in strs) {
        
        // C#: .ToCharArray() converts string to char array
        char[] chars = str.ToCharArray();
        
        // C#: Array.Sort() sorts character array in-place
        Array.Sort(chars);
        
        // C#: new string(char[]) constructor creates string from char array
        string key = new string(chars);
        
        
        // C#: .ContainsKey() checks existence, indexer creates new list
        if (!map.ContainsKey(key)) {
            map[key] = new List<string>();
        }
        
        // C#: .Add() method adds element to list
        map[key].Add(str);
    }
    
    
    // C#: Constructor creates list from dictionary values
    return new List<IList<string>>(map.Values);
}