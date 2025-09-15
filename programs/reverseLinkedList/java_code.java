class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class Solution {
    /**
     * Reverse a singly linked list iteratively
     */
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        
        while (current != null) {
            ListNode nextTemp = current.next;  // Store next node
            current.next = prev;               // Reverse the link
            prev = current;                    // Move prev forward
            current = nextTemp;                // Move current forward
        }
        
        return prev;  // prev is the new head
    }
}