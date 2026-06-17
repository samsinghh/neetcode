class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            larger = -1 * heapq.heappop(maxHeap)
            smaller = -1 * heapq.heappop(maxHeap)

            if larger == smaller:
                continue
            else:
                larger -= smaller
                heapq.heappush(maxHeap, -larger)
        
        return -1 * maxHeap[0] if len(maxHeap) == 1 else 0