class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairs = []

        for x, y in points:
            distance = (x**2 + y**2)**(0.5)
            heapq.heappush(pairs, [-distance, [x, y]])
            if len(pairs) > k:
                heapq.heappop(pairs)
        
        res = []

        for _ in range(k):
            pair = heapq.heappop(pairs)[1]
            res.append(pair)
        
        return res

