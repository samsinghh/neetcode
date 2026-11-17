class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def search(node):
            q = deque([node])
            while q:
                i = q.popleft()
                seen.add(i)
                for nei in adj[i]:
                    if nei not in seen:
                        q.append(nei)
        
        res = 0 
        for i in range(n):
            if i not in seen:
                search(i)
                res += 1
        
        return res
