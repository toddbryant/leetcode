/**
 * Given a linked list, reverse the nodes of a linked list 
 * k at a time and return its modified list.

 * k is a positive integer and is less than or equal to the length of the linked list.
 * If the number of nodes is not a multiple of k,
 * then left-out nodes in the end should remain as it is.
 */

public class Solution {
    // Returns the node k steps after head
    public ListNode NodePlusK(ListNode head, int k) {
        while(head != null && k > 0) {
            head = head.next;
            --k;
        }
        return k==0 ? head : null;
    }

    public ListNode ReverseKGroup(ListNode head, int k) {
       // Create dummy to point to list head 
       ListNode handle = new ListNode(-1);
       handle.next = head;
       
       // Save a copy of handle for return purposes;
       ListNode origHandle = handle;

       ListNode tail, remainder;
       ListNode prv, cur, temp;
       while((tail = NodePlusK(handle, k)) != null) {
           remainder = tail.next;

           prv = handle.next;
           cur = prv.next;

           // Reverse links within the next k nodes
           while(prv != tail)
           {
               temp = cur.next;
               cur.next = prv;

               prv = cur;
               cur = temp;
           } 

           // Adjust pointers to internally reversed list
           temp = handle.next;
           handle.next.next = remainder;
           handle.next = tail;

           // Advance handle pointer 
           handle = temp;
       }

       return origHandle.next;
    }
}
