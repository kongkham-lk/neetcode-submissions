# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # Get the mid node of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        second, prev = slow.next, None
        slow.next = None # Completely split first half and second half

        # Reverse all the second half of the list
        while second:
            temp = second
            second = second.next
            temp.next = prev
            prev = temp
        
        second = prev
        # Merge 2 list into 1
        while first and second:
            temp = first
            first = first.next
            temp.next = second

            temp = temp.next
            second = second.next
            temp.next = first
        
        
