# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # n=0 and n=1 trivial cases
        if not head or not head.next:
            return head
        
        # Find length of list so we can mod k
        length = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            length += 1
        k = k % length
        
        if k==0:
            return head
        
        # Make length-k-1 jumps to get to new tail
        tmp = head
        for _ in range(length-k-1):
            tmp = tmp.next
        new_head = tmp.next
        tmp.next = None
        
        # k more jumps
        tmp = new_head
        for _ in range(k-1):
            tmp = tmp.next
        tmp.next = head
        
        return new_head
        
        
