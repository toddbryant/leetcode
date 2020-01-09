/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }


 * Problem:
 * Given a linked list, remove the n-th node from the end of list and return its head.
 *
 * This was a very straightforward linked list problem.
 */
public class Solution {
    public int RemoveNthFromEndHelper(ListNode head, int n)
    {
        if(head==null)
            return 0;
        int distanceToEnd = RemoveNthFromEndHelper(head.next, n);
        if(distanceToEnd == n) {
            head.next = head.next.next;
        }
        return distanceToEnd + 1;
    }
    
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        // Add a leading node to make removing the first item easy.
        ListNode padding = new ListNode(-1);
        padding.next = head;
        
        RemoveNthFromEndHelper(padding, n);
        return padding.next;
    }
}
