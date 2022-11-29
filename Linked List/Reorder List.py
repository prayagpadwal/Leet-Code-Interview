# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Setting pointers in then middle of the LL
        prev, curr = head, head.next
        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next
        
        # Reverse second half
        second = prev.next
        prev.next = None
        slow = None

        while second:
            nxt = second.next
            second.next = slow
            slow = second
            second = nxt

        # Join/ Merge the two LL
        first, second = head, slow
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2 


# Kinda crerpy question
# understood it for now, might create confuse later.