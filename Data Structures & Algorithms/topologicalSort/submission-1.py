class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
        
        res = []
        visited = set()
        visiting = set()
        def dfs(node):
            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        
        res.reverse()
        return res
            
        

        
