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
        if not head.next:
            return None

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        remove_pos = length - n
        if remove_pos == 0:
            return head.next
        
        curr = head
        for _ in range(remove_pos - 1):
            curr = curr.next
        
        curr.next = curr.next.next

        return head
        
        