"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(None, head)      
        prev, cur = root, head
        
        while cur:
            if cur.next and cur.val==cur.next.val:
                while cur and cur.val == prev.next.val:
                    cur = cur.next
                prev.next = cur
            else:
                prev, cur = cur, cur.next
            
        return root.next
