# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        # get the mid node of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first = head
        second, prev = slow.next, None
        slow.next = None # completely split first half and second half

        # reverse all the second half of the list
        while second:
            temp = second
            second = second.next
            temp.next = prev
            prev = temp
        
        second = prev
        
        # l = []
        # s = first
        # while s:
        #     l.append(s.val)
        #     s = s.next
        # print(l)
        # l = []
        # s = second
        # while s:
        #     l.append(s.val)
        #     s = s.next
        # print(l)

        while first and second:
            temp = first
            first = first.next
            temp.next = second
            temp = temp.next
            second = second.next
            temp.next = first

            # l = []
            # s = head
            # while s:
            #     l.append(s.val)
            #     s = s.next
            # print(l)

        # while first :
        #     temp = first
        #     first = first.next
        #     temp.next = first

        #     l = []
        #     s = head
        #     while s:
        #         l.append(s.val)
        #         s = s.next
        #     print(l)
        
        
