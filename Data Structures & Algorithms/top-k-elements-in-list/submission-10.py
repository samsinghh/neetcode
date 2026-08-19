class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        heap = [(-count, num) for num, count in counts.items()]
        heapq.heapify(heap)

        res = []

        for _ in range(k):
            count, num = heapq.heappop(heap)
            res.append(num)
        
        return res
        
        

