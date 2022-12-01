# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # dummy = ListNode(next = head)
        # prev = curr = dummy     # placing both pointers at dummy
        prev = curr = head

        while curr and curr.next:
            prev = prev.next
            curr = curr.next.next
        return prev