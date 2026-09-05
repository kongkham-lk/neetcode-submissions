# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        offset, curr = head, head
        while n > 0: 
            offset = offset.next
            n -= 1
        
        if offset is None: 
            if head.next: return head.next
            else: return None

        prev = None
        while offset:
            prev = curr
            curr = curr.next
            offset = offset.next
        
        prev.next = curr.next
        return head