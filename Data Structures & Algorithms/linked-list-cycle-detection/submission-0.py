# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first, second = head, head.next

        while second:
            if first == second:
                return True
            if second.next == None:
                return False
            first = first.next
            second = second.next.next
        
        return False

