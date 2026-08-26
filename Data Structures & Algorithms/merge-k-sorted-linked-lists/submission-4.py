# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# use a min-heap to store the next node from all lists that has the lowest value
# store current head/current pointer of list with it's value in min-heap
# keep popping from min heap until there is nothing left inside
# when you pop from min heap, add that value to the result list, and if node has a next, add 
# node.next back into the heap

# (value, index of list in lists, node)

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = curr = ListNode()

        heap = []
        heapq.heapify(heap)

        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return res.next
        

