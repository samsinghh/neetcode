# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1, 2  3, 4
# ^     ^

#1, 2 
#4, 3

# 1, 4, 2, 3
# 1, 2, 3, 4, 5

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        temp = slow.next
        slow.next = None
        slow = temp

        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev, slow = slow, temp
        
        curr = head
        res = temp = ListNode()
        while curr or prev:
            if curr:
                temp.next = curr
                temp = temp.next
                curr = curr.next
            if prev:
                temp.next = prev
                temp = temp.next
                prev = prev.next
        
            
            


            


        