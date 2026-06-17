# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = iterr = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                iterr.next = list1
                list1 = list1.next
            else:
                iterr.next = list2
                list2 = list2.next
            iterr=iterr.next
        
        iterr.next = list1 or list2
        
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        merged = None

        for lst in lists: 
            merged = self.mergeTwoLists(merged, lst)
        
        return merged

