class Node {
    constructor(key = 0, value = 0) {
        
        // JavaScript: Initialize doubly linked list node
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    constructor(capacity) {
        
        // JavaScript: Initialize LRU cache with given capacity
        this.capacity = capacity;
        
        // JavaScript: Map for O(1) key lookup
        this.cache = new Map();
        
        
        // JavaScript: Create dummy head and tail nodes
        this.head = new Node();
        this.tail = new Node();
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }
    
    _addNode(node) {
        
        // JavaScript: Add node right after head (most recently used)
        node.prev = this.head;
        node.next = this.head.next;
        
        this.head.next.prev = node;
        this.head.next = node;
    }
    
    _removeNode(node) {
        
        // JavaScript: Remove node from doubly linked list
        const prevNode = node.prev;
        const nextNode = node.next;
        
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
    }
    
    _moveToHead(node) {
        
        // JavaScript: Move existing node to head (mark as recently used)
        this._removeNode(node);
        this._addNode(node);
    }
    
    _popTail() {
        
        // JavaScript: Remove least recently used node
        const lastNode = this.tail.prev;
        this._removeNode(lastNode);
        return lastNode;
    }
    
    get(key) {
        
        // JavaScript: Get value and mark as recently used
        const node = this.cache.get(key);
        
        if (node) {
            
            // Move to head since it was accessed
            this._moveToHead(node);
            return node.value;
        }
        
        return -1;
    }
    
    put(key, value) {
        
        // JavaScript: Put key-value pair, handle capacity constraints
        const node = this.cache.get(key);
        
        if (node) {
            
            // Update existing node
            node.value = value;
            this._moveToHead(node);
        } else {
            
            // Create new node
            const newNode = new Node(key, value);
            
            if (this.cache.size >= this.capacity) {
                
                // Remove LRU node
                const tail = this._popTail();
                this.cache.delete(tail.key);
            }
            
            
            // Add new node
            this.cache.set(key, newNode);
            this._addNode(newNode);
        }
    }
}

// Test the LRU Cache
const lru = new LRUCache(2);

lru.put(1, 1);
lru.put(2, 2);
console.log(`Get 1: ${lru.get(1)}`); // Returns 1

lru.put(3, 3); // Evicts key 2
console.log(`Get 2: ${lru.get(2)}`); // Returns -1

lru.put(4, 4); // Evicts key 1
console.log(`Get 1: ${lru.get(1)}`); // Returns -1
console.log(`Get 3: ${lru.get(3)}`); // Returns 3
console.log(`Get 4: ${lru.get(4)}`); // Returns 4