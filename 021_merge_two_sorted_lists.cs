/**
 *
 * Merge two sorted linked lists and return it as a new list. 
 * The new list should be made by splicing together the nodes of the first two lists,
 *
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 * 
 * Another very basic LL problem.
 */
public class Solution {
    public ListNode MergeTwoLists(ListNode l1, ListNode l2) {
        if(l1==null)
            return l2;
        if(l2==null)
            return l1;
        
        ListNode result = new ListNode(-1);
        ListNode head = result;
        
        while(l1!=null && l2!=null) {
            if(l1.val < l2.val) {
                result.next = l1;
                l1 = l1.next;
            }
            else {
                result.next = l2;
                l2 = l2.next;
            }
            result = result.next;
        }
        result.next = l1 ?? l2;
        
        return head.next;
    }
}
