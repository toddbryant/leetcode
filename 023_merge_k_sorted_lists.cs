/**
 * Merge k sorted linked lists and return it as one sorted list. 
 * Analyze and describe its complexity.
 *
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 * 
 * omg this is slow cause it doesn't use a priority queue
 * note to self review priority queues
 */
public class Solution {
    public int IndexOfMinNode(ListNode[] lists, int start) 
    {
        int bestIndex = -1;
        for(int i=start; i<lists.Length; ++i)
            if(lists[i] != null && (bestIndex==-1 || lists[i].val < lists[bestIndex].val))
                bestIndex = i;

        return bestIndex;
    }
    
    public ListNode MergeKLists(ListNode[] lists) {
        ListNode head = new ListNode(-1);
        ListNode ptr = head;
        
        int start = 0;
        while(start<lists.Length) {
            int i = IndexOfMinNode(lists, start);
            if(i == -1)
                return head.next;
            ptr.next = lists[i];
            ptr = ptr.next;
            lists[i] = lists[i].next;
            
            if(lists[i]==null) { // Swap out null node
                ListNode temp = lists[start];
                lists[start] = lists[i];
                lists[i] = temp;
                ++start;
            }
        }
        
        return head.next;
    }
}
