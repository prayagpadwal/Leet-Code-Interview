# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        an_array = []

        while head: #while head is not NULL
            an_array.append(head.val)
            head = head.next
            

        l, r = 0 ,len(an_array) - 1
        # l and r are 2 pointers
        # l at 0 
        # r at end of array
        while l <= r:
            if an_array[l] != an_array[r]:
                return False
            l += 1
            r -= 1
        return True # True is executed when
                    # all the elements in
                    # the list are equal
                    # meaning: it's a palindrome
