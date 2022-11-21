# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        first, last = None, head
        
        while last:
            nxt = last.next
            last.next = first
            first = last
            last = nxt
        return first
           