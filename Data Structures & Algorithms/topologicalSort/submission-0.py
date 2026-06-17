class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(n)}
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        q = deque([node for node in range(n) if indegree[node] == 0])
        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res if len(res) == n else []
