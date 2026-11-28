class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = heapq.heappop(heap) * -1
            second = heapq.heappop(heap) * -1

            if first == second:
                continue
            else:
                heapq.heappush(heap, second - first)
        
        if heap:
            return heapq.heappop(heap) * -1
        return 0