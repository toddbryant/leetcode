/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode SwapPairs(ListNode head) {
        if(head==null)
            return head;
        
        ListNode handle = new ListNode(-1);
        handle.next = head;
        ListNode origHandle = handle;
        
        ListNode a, b, tail;
        while(handle.next != null && handle.next.next != null) {
            a = handle.next; // next node
            b = handle.next.next; // node after that
            tail = b.next; // the rest of the list

            // Rearrange pointers
            b.next = a;
            a.next = tail;
            handle.next = b;
            
            handle = a; // Advance two nodes (which is now a)
        }

        return origHandle.next;
    }
}
