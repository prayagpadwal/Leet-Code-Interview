# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        dummy = ListNode()  # created dummy node
        dummy.next = list1  # dummy pointing at list1 (head of list1)
        prev = dummy        # could've used dummy instead of prev, but made a new pointer pointing at dummy
        curr = list1        # curr pointing at head of list1

        for i in range(a):  # prev is curr - 1 
            prev = prev.next# prev reaches a - 1     
            curr = curr.next# curr reaches a    

        for i in range(b-a+1):
            curr = curr.next# curr reaches b

        prev.next = list2   # prev attached list1 to list2

        while list2.next:   # while list2 is not null
            list2 = list2.next  # list2 is also a pointer that will reach at the last node
        
        list2.next = curr   # curr is at b+1 and now list2 pointer is attached with list1 at b+1 
        return list1        #attached list1 and list2 