class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        visited = set()

        for first, second in edges:
            adj[first].append(second)
            adj[second].append(first)
        
        
        def dfs(node, par):
            if node in visited:
                return 

            visited.add(node)

            for nei in adj[node]:
                if nei != par:
                    dfs(nei, node)
            
            
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1
        
        return res
