# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = temp = ListNode()

        c1, c2 = list1, list2

        while c1 and c2:
            if c1.val < c2.val:
                temp.next = ListNode(c1.val)
                temp = temp.next
                c1 = c1.next
            else:
                temp.next = ListNode(c2.val)
                temp = temp.next
                c2 = c2.next

        temp.next = c1 or c2

        return res.next
