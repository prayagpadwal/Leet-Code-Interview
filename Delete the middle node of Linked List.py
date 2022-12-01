# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(next = head)
        d = dummy
        prev = curr = head

        while curr and curr.next:
            d = prev
            prev = prev.next
            curr = curr.next.next
        d.next = prev.next
        return dummy.next


# Solved this question in less than 6 minutes 
# My personal all time best