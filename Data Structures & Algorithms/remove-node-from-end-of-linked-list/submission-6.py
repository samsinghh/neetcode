# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1, 2, 3, 4] - length = 4, n = 2, length - n + 1 -> 4 -2 + 1 = 3
# [5] -> ListNode()
# if we are removing the first node, just return head.next

# get on the node before the one we have to remove
# that node.next equals its .next.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l, r = dummy, head

        while n > 0:
            r = r.next
            n -= 1
        
        while r:
            l, r = l.next, r.next
        
        l.next = l.next.next
        return dummy.next


# [1, 2, 3, 4, 5, 6] n = 2


        
        