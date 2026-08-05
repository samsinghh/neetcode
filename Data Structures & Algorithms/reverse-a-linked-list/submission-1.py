# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# a -> b -> c -> d

# prev -> none
# curr -> a

# store curr.next in a temp var
# make curr point at prev 
# move prev to curr, curr to temp

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        return prev

