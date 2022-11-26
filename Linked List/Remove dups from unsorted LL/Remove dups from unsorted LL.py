class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        hashmap = collections.defaultdict(int)
        curr = head
        dummy = ListNode(0 ,head)
        prev = dummy

        while curr.next is not None:
            if curr.next.data in hashmap:
                curr.next = curr.next.next
            





        




