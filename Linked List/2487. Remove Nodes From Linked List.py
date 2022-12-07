# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next

        ans = []
        for x in reversed(arr):
            if len(ans) == 0 or x >= ans[-1]:
                ans.append(x)
        ans.reverse()

        newHead = ListNode(-1)
        current = newHead
        for x in ans:
                current.next = ListNode(x)
                current = current.next
        return newHead.next