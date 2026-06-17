# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        for _ in range(n):
            right = right.next
        
        left = head
        if not right:
            return left.next
        
        while right and right.next:
            left = left.next
            right = right.next
        
        if not left.next:
            return 

        left.next = left.next.next

        return head
