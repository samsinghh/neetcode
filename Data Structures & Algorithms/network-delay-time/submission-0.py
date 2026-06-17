class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i : [] for i in range(1, n+1)}

        for u, v, w in times:
            adj[u].append((v, w))
        
        min_heap = [(0, k)]
        min_length = [float('inf')] * (n+1)
        min_length[k] = 0
        min_length[0] = 0
        while min_heap:
            curLength, node = heapq.heappop(min_heap)

            for nei, time in adj[node]:
                if curLength + time < min_length[nei]:
                    min_length[nei] = curLength + time
                    heapq.heappush(min_heap, (curLength+time, nei))

        return max(min_length) if max(min_length) != float('inf') else -1