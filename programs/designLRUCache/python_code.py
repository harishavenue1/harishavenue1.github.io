class Node:
    def __init__(self, key=0, value=0):
        
        # Python: Initialize doubly linked list node
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        
        # Python: Initialize LRU cache with given capacity
        self.capacity = capacity
        
        # Python: Dictionary for O(1) key lookup
        self.cache = {}
        
        
        # Python: Create dummy head and tail nodes for easier manipulation
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node):
        
        # Python: Add node right after head (most recently used)
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        
        # Python: Remove node from doubly linked list
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _move_to_head(self, node):
        
        # Python: Move existing node to head (mark as recently used)
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        
        # Python: Remove least recently used node (before tail)
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node
    
    def get(self, key: int) -> int:
        
        # Python: Get value and mark as recently used
        node = self.cache.get(key)
        
        if node:
            
            # Move to head since it was accessed
            self._move_to_head(node)
            return node.value
        
        return -1
    
    def put(self, key: int, value: int) -> None:
        
        # Python: Put key-value pair, handle capacity constraints
        node = self.cache.get(key)
        
        if node:
            
            # Update existing node
            node.value = value
            self._move_to_head(node)
        else:
            
            # Create new node
            new_node = Node(key, value)
            
            if len(self.cache) >= self.capacity:
                
                # Remove LRU node
                tail = self._pop_tail()
                del self.cache[tail.key]
            
            
            # Add new node
            self.cache[key] = new_node
            self._add_node(new_node)

# Test the LRU Cache
if __name__ == "__main__":
    lru = LRUCache(2)
    
    lru.put(1, 1)
    lru.put(2, 2)
    print(f"Get 1: {lru.get(1)}")  # Returns 1
    
    lru.put(3, 3)  # Evicts key 2
    print(f"Get 2: {lru.get(2)}")  # Returns -1 (not found)
    
    lru.put(4, 4)  # Evicts key 1
    print(f"Get 1: {lru.get(1)}")  # Returns -1 (not found)
    print(f"Get 3: {lru.get(3)}")  # Returns 3
    print(f"Get 4: {lru.get(4)}")  # Returns 4