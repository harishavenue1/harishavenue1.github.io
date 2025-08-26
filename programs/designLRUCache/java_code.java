import java.util.HashMap;

class Node {
    int key, value;
    Node prev, next;
    
    Node(int key, int value) {
        
        // Java: Initialize doubly linked list node
        this.key = key;
        this.value = value;
    }
}

public class LRUCache {
    private int capacity;
    
    // Java: HashMap for O(1) key lookup
    private HashMap<Integer, Node> cache;
    private Node head, tail;
    
    public LRUCache(int capacity) {
        
        // Java: Initialize LRU cache with given capacity
        this.capacity = capacity;
        this.cache = new HashMap<>();
        
        
        // Java: Create dummy head and tail nodes
        this.head = new Node(0, 0);
        this.tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
    }
    
    private void addNode(Node node) {
        
        // Java: Add node right after head (most recently used)
        node.prev = head;
        node.next = head.next;
        
        head.next.prev = node;
        head.next = node;
    }
    
    private void removeNode(Node node) {
        
        // Java: Remove node from doubly linked list
        Node prevNode = node.prev;
        Node nextNode = node.next;
        
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
    }
    
    private void moveToHead(Node node) {
        
        // Java: Move existing node to head (mark as recently used)
        removeNode(node);
        addNode(node);
    }
    
    private Node popTail() {
        
        // Java: Remove least recently used node
        Node lastNode = tail.prev;
        removeNode(lastNode);
        return lastNode;
    }
    
    public int get(int key) {
        
        // Java: Get value and mark as recently used
        Node node = cache.get(key);
        
        if (node != null) {
            
            // Move to head since it was accessed
            moveToHead(node);
            return node.value;
        }
        
        return -1;
    }
    
    public void put(int key, int value) {
        
        // Java: Put key-value pair, handle capacity constraints
        Node node = cache.get(key);
        
        if (node != null) {
            
            // Update existing node
            node.value = value;
            moveToHead(node);
        } else {
            
            // Create new node
            Node newNode = new Node(key, value);
            
            if (cache.size() >= capacity) {
                
                // Remove LRU node
                Node tail = popTail();
                cache.remove(tail.key);
            }
            
            
            // Add new node
            cache.put(key, newNode);
            addNode(newNode);
        }
    }
    
    public static void main(String[] args) {
        LRUCache lru = new LRUCache(2);
        
        lru.put(1, 1);
        lru.put(2, 2);
        System.out.println("Get 1: " + lru.get(1)); // Returns 1
        
        lru.put(3, 3); // Evicts key 2
        System.out.println("Get 2: " + lru.get(2)); // Returns -1
        
        lru.put(4, 4); // Evicts key 1
        System.out.println("Get 1: " + lru.get(1)); // Returns -1
        System.out.println("Get 3: " + lru.get(3)); // Returns 3
        System.out.println("Get 4: " + lru.get(4)); // Returns 4
    }
}